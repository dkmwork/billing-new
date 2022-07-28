jQuery(function(){
    //Sales
    // set the state code afterselecting the state  
    jQuery('#id_sales_state').change(function(){
        var cstate_name=jQuery(this).val()
        test_function('state_code_id',cstate_name,"set_state_code")
        // jQuery.ajax({
        //     type:"GET",
        //     url:"set_state_code",
        //     data:{
        //         state_name:cstate_name
        //     },
        //     success:function(response){
        //         jQuery('#state_code_id').val(response)
        //     }
        // })
    })
    //Sales
    //set the contact number after selecting the customer
    jQuery('#id_customer').blur(function(){

        itemid=jQuery(this).val()
       
        test_function('mobile_no_id',itemid,"get_contactno")

        // var customer=jQuery(this).val()
        // jQuery.ajax({
        //     type:"GET",
        //     url:"get_contactno",
        //     data:{
        //         customer_name:customer
        //     },
        //     success:function(response){
        //         jQuery('#mobile_no_id').val(response)
        //     }
        // })

    })
    function test_function(controlid,itemid,urlstring){

       // var customer=jQuery(this).val()
        jQuery.ajax({
            type:"GET",
            url:urlstring,
            data:{
                commonid:itemid
            },
            success:function(response){
                jQuery('#'+controlid).val(response)
            }
        })
    }
    //Sales
    // function for checking duplicate  item and prevent it from adding in the sales item bridge
function check_duplicate_item(citemid,controlname){
    
        const item_refs=Array.from(document.querySelectorAll(`select[name$="-sales_item"]`))
        const filterred_item_refs=item_refs.filter(x=>x.name!=controlname)
        for(item of filterred_item_refs){
            if (!item.name.includes('prefix')){
                if(item.value==citemid){
                    alert("Item already exists!!!")
                    return true
                }
            }
        }
    }
    //Sales
    //function for small grid(gst_wise table)

    function delete_gameboard(tablename){
        let table=null
        if(tablename=='sales'){
         table=document.getElementById('id_sales_gst_summary')
        }
    
        else{
         table = document.getElementById("id_purchase_gst_summary");   
        }
        while (table.rows.length > 1) {
        table.deleteRow(1);
    }
    }

function update_gst_table(){
    //alert("hi")
    const tax_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_tax"]`));
    const taxable_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_taxable"]`))
    const sgst_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_SGSTamnt"]`));
    const cgst_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_CGSTamnt"]`));
    const igst_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_IGSTamnt"]`));
    const amount_refs=Array.from(document.querySelectorAll(`input[name$="salesitem_amnt"]`));
    var formsetlist=[];
    //console.log(tax_refs)
    for (const item of tax_refs){
        //console.log(item)
        const index=item.name.split('-')[1]
        //alert("hi")
        if (index!='__prefix__'){
            console.log("hi")
            var objtax=tax_refs.find(x=>x.name.includes(index))
            var tax=objtax.value
            var objtaxable=taxable_refs.find(x=>x.name.includes(index))
            var taxable=objtaxable.value
            var objsgst=sgst_refs.find(x=>x.name.includes(index))
            var sgst=objsgst.value
            var objcgst=cgst_refs.find(x=>x.name.includes(index))
            var cgst=objcgst.value
            var objigst=igst_refs.find(x=>x.name.includes(index))
            var igst=objigst.value
            var objamnt=amount_refs.find(x=>x.name.includes(index))
            var amnt=objamnt.value
            var dict={"tax":tax,"taxable":taxable,"sgst":sgst,"cgst":cgst,"igst":igst,"amount":amnt}
            formsetlist.push(dict)
            //console.log(formsetlist)
        }
    }
create_html_for_smallgrid(formsetlist)
}

function create_html_for_smallgrid(formsetlist){
    //alert("hi")
    var gst_table=document.getElementById("id_sales_gst_summary")
    var sales_result=[];
    formsetlist.reduce(function(res,value){
        if(!res[value.tax]){

            res[value.tax] = {tax:value.tax,taxable: 0,cgst: 0,sgst:0,igst:0 ,amount:0 };
            sales_result.push(res[value.tax])
            
        }
        res[value.tax].taxable=parseFloat(res[value.tax].taxable)+parseFloat(value.taxable);
        res[value.tax].cgst=parseFloat(res[value.tax].cgst)+parseFloat(value.cgst);
        res[value.tax].sgst=parseFloat(res[value.tax].sgst)+parseFloat(value.sgst);
        res[value.tax].igst=parseFloat(res[value.tax].igst)+parseFloat(value.igst);
        res[value.tax].amount=parseFloat(res[value.tax].amount)+parseFloat(value.amount);
        return res;
    },{});
    delete_gameboard('sales')

    console.log(sales_result)
    for (const row of sales_result){
        console.log(row)
        if (row.tax!=''){
            
            let new_row=gst_table.insertRow(-1)
            let new_cell=new_row.insertCell(0)
            let newText=document.createTextNode(row.tax)
            new_cell.append(newText)
            new_cell=new_row.insertCell(1)
            newText=document.createTextNode(row.taxable)
            new_cell.append(newText)
            
            new_cell=new_row.insertCell(2)
            newText=document.createTextNode(row.cgst)
            new_cell.append(newText)
            new_cell=new_row.insertCell(3)
            newText=document.createTextNode(row.sgst)
            new_cell.append(newText)
            new_cell=new_row.insertCell(4)
            newText=document.createTextNode(row.igst)
            new_cell.append(newText)
            new_cell=new_row.insertCell(5)
            newText=document.createTextNode(row.amount)
            new_cell.append(newText)

            
        }
    }
    sales_result=[];
}
    //Sales
    // set the item code, hsn and tax according to the change of item field, both in create mode and edit mode
    jQuery('#sales_formsetid').on('change','select[name$="-sales_item"]',function(){
    var urlstring=""
    // this step helps to go to purchaselist_edit mode instead of create purchase
    // property returns the URL of the current page.
    if(window.location.href.includes('saleslist_edit')){
        urlstring='../sales_hsn_gst_select'
    }
    //the else side acts the normal create purchase
    else {
        urlstring="sales_hsn_gst_select"
        
    }
    var citemid=jQuery(this).val()
    var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1];
    jQuery(`input[name$="${digit_part}-salesitem_disc]`).val(0)
    
    if (check_duplicate_item(citemid,object[0].name)==true){
        
        jQuery(this).prop('selectedIndex',0);
    }
    else {
        jQuery.ajax({
            type:"GET",
            url:urlstring,
            data:{
                itemid:citemid
            },
            success:function(response){
                //alert(response.item_code)
                jQuery(`input[name$="${digit_part}-sales_item_code"`).val(response.item_code)
                jQuery(`input[name$="${digit_part}-sales_item_code"`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_hsncode"]`).val(response.hsn_code)
                jQuery(`input[name$="${digit_part}-salesitem_hsncode"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_tax"]`).val(response.gst_percent)
                //jQuery(`input[name$="${digit_part}-salesitem_tax"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_taxable"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_CGST"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_SGST"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_IGST"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_CGSTamnt"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_SGSTamnt"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_IGSTamnt"]`).prop('readonly','readonly')
                jQuery(`input[name$="${digit_part}-salesitem_amnt"]`).prop('readonly','readonly')
                jQuery('#id_sales_taxableamount').prop('readonly','readonly')
                jQuery('#id_sales_CGSTAmnt').prop('readonly','readonly')
                jQuery('#id_sales_SGSTAmnt').prop('readonly','readonly')
                jQuery('#id_sales_IGSTAmnt').prop('readonly','readonly')
                jQuery('#id_sales_subtotal').prop('readonly','readonly')
                jQuery('#id_sales_GTotal').prop('readonly','readonly')
                update_gst_table()
            }
        })
    }
    
    })
//Sales
// function for checking item to be filled befor calculation sales item bridge
function check_item_to_be_filled(digit_part){
if (jQuery (`input[name$="${digit_part}-sales_item"]`).val()==''){
    alert("Item field must be filled")
    return true
}
else{
    return false
}
}
//Sales
//Calculate sales item bridge according to the selected rate
jQuery('#sales_formsetid').on('change',"input[name$='salesitem_rate']",function(){
    //alert("hi")
    var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1]
    if (check_item_to_be_filled(digit_part)==true){
        jQuery(this).val('')
    }
    else{
        calculation(digit_part)
        sales_summary_caluclations()
        update_gst_table()
    }
})

//Sales
//Calculate sales item bridge according to the selected quantity
jQuery('#sales_formsetid').on('change',"input[name$='salesitem_quantity']",function(){
    //alert("hi")
    var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1]
    if (check_item_to_be_filled(digit_part)==true){
        jQuery(this).val('')
    }
    else{
        calculation(digit_part)
        sales_summary_caluclations()
        update_gst_table()
    }
})
//Sales
//Calculate sales item bridge according to the selected discount

jQuery('#sales_formsetid').on('change',"input[name$='salesitem_disc']",function(){
    var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1]
    if (check_item_to_be_filled(digit_part)==true){
        jQuery(this).val('')
    }
    else{
        calculation(digit_part)
        sales_summary_caluclations()
        update_gst_table()
    }
})

function calculation(digit_part){
    var quantity=jQuery(`input[name$="${digit_part}-salesitem_quantity"]`).val()
    var rate=jQuery(`input[name$="${digit_part}-salesitem_rate"]`).val()
    var disc=jQuery(`input[name$="${digit_part}-salesitem_disc"]`).val()
    var state_code=jQuery('#custom_value_state_code').val()
    //alert(disc)
    var taxable=(quantity *rate)-disc
    //alert(taxable)
    jQuery(`input[name$="${digit_part}-salesitem_taxable"]`).val(taxable)
    var st=jQuery(`input[name$="${digit_part}-salesitem_tax"]`).val()
    var amount=taxable*st/100
    //alert(amount)
    var total_amnt=parseInt(taxable)+amount
    jQuery(`input[name$="${digit_part}-salesitem_amnt"]`).val(total_amnt)
    if (jQuery('#state_code_id').val()==state_code){
        jQuery(`input[name$="${digit_part}-salesitem_IGST"]`).val(0)
        jQuery('#salesitem_igstpercent').val(0)
        //alert(amount/2)
        jQuery(`input[name$="${digit_part}-salesitem_CGSTamnt"]`).val(amount/2)
        jQuery(`input[name$="${digit_part}-salesitem_CGST"`).val(st/2)
        jQuery(`input[name$="${digit_part}-salesitem_SGSTamnt"]`).val(amount/2)
        jQuery(`input[name$="${digit_part}-salesitem_SGST"`).val(st/2)
        
    }
    else {
        jQuery(`input[name$="${digit_part}-salesitem_SGST"]`).val(0)
        jQuery('#salesitem_sgstpercent').val(0)
        jQuery(`input[name$="${digit_part}-salesitem_CGST"]`).val(0)
        jQuery('#salesitem_cgstpercent').val(0)
        jQuery(`input[name$="${digit_part}-salesitem_IGSTamnt"]`).val(amount)
        jQuery(`input[name$="${digit_part}-salesitem_IGST"]`).val(st)
    }
}
//Update the Sales bottom table according to the change of quantity, discount,rate and item

function sales_summary_caluclations(){
    adding_sales_subtotal()
    adding_sales_txblamnt()
    adding_sales_cgst()
    adding_sales_sgst()
    adding_sales_igst()
    adding_sales_gtotal()
    
}
// function for calculating sub total according to the change of quantity, discount,rate and item
function adding_sales_subtotal(){
    const refs=Array.from(document.querySelectorAll(`input[name$="salesitem_amnt"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    //alert(sum)
    //jQuery('#id_sales_subtotal').val(sum)
    const sub_total=document.getElementById('id_sales_subtotal');
    sub_total.value=sum;
}
// function for calculating total taxable amount according to the change of quantity, discount,rate and item

function adding_sales_txblamnt(){
    const refs=Array.from(document.querySelectorAll(`input[name$="salesitem_taxable"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    console.log(sum)
    const taxable_amnt=document.getElementById('id_sales_taxableamnt');
    taxable_amnt.value=sum;
}

// function for calculating total CGST according to the change of quantity, discount,rate and item
function adding_sales_cgst(){
    const refs=Array.from(document.querySelectorAll(`input[name$="salesitem_CGSTamnt"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    const total_cgst=document.getElementById('id_sales_CGSTAmnt');
    total_cgst.value=sum;
}
// function for calculating total SGST according to the change of quantity, discount,rate and item
function adding_sales_sgst(){
    const refs=Array.from(document.querySelectorAll(`input[name$="salesitem_SGSTamnt"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    const total_sgst=document.getElementById('id_sales_SGSTAmnt');
    total_sgst.value=sum;
}
// function for calculating total IGST according to the change of quantity, discount,rate and item
function adding_sales_igst(){
    const refs=Array.from(document.querySelectorAll(`input[name$="salesitem_IGSTamnt"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const igst_sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    //console.log(igst_sum)
    //jQuery('#id_sales_IGSTAmnt').val(sum)
    const total_igst=document.getElementById('id_sales_IGSTAmnt');
    total_igst.value=igst_sum;
}
//calculate the G total according to the change of discount.

jQuery('#id_sales_Discount').blur(function(){
    //alert(jQuery(this).val())
    adding_sales_gtotal()
})

// function for calculating total G Total according to the change of quantity, discount,rate and item
function adding_sales_gtotal(){
    
    const refs= document.getElementById('id_sales_subtotal');
    const sub_total=refs.value
    //alert(sub_total)
    const disc=document.getElementById('id_sales_Discount');
    const dis_amnt=disc.value
    //alert(dis_amnt)
    if (dis_amnt>0){
        alert('hi')
        const g_total=sub_total-dis_amnt
        alert(g_total)
        const g_totalamnt=document.getElementById('id_sales_GTotal');
        g_totalamnt.value=g_total
        //jQuery('#id_sales_GTotal').val(g_total)
    }
    else{
        const g_totalamnt=document.getElementById('id_sales_GTotal');
        g_totalamnt.value=sub_total
    }
}

jQuery('#sales_addmore_btn').click(function(){
    var form_index=$('#id_sales_items_bridge-TOTAL_FORMS').val();  
    if (check_addmore_table_values(form_index)==true){  
    jQuery('#sales_formsetid').append(jQuery('#empty_sales_form_id').html().replace(/__prefix__/g,form_index));
    jQuery('#id_sales_items_bridge-TOTAL_FORMS').val(parseInt(form_index)+1);
    }
})


// fill the upper part of the form accoriding to the invoice number selection.

jQuery('#id_return_salesinvoiceno').change(function(){
    var invno=jQuery(`#id_return_salesinvoiceno option:selected`).text()
    //var invno=jQuery('#id_return_salesinvoiceno').val()
    //alert(invno)
    jQuery.ajax({
        type:"GET",
        url:"salesreturninfo",
        data:{
            invoice_no:invno,
        },
        success:function(response){
            //
            state=response['sales_details']['sales_state__state_name']
            //console.log(state)
            customer=response['sales_details']['customer__party_name']
            //console.log(customer)
            invoice_date=response['sales_details']['invoice_date']
            sales_type=response['sales_details']['sales_type']
            
            sales_credit=response['sales_details']['sales_credit']
            //console.log(sales_credit)
            sales_discount=response['sales_details']['sales_Discount']
            sales_paymode=response['sales_details']['sales_Paymode__payment_method']
            //console.log(sales_paymode)
            // jQuery('#id_sales_type option').each(function(){
            //     if(jQuery(this).text()==sales_type){
                    
            //         jQuery(this).prop('selected','selected')
            //     }
            // })
            // jQuery('#id_sales_type').prop('readonly','readonly')
            jQuery('#id_sales_type option').each(function(){
                if (jQuery(this).text()==sales_type){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_sales_type option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=sales_type){
                   
                    options[i].disabled = true;
                }   
              }
            // jQuery('#id_sales_state option').each(function(){
            //     if(jQuery(this).text()==state){
            //         jQuery(this).prop('selected','selected')
            //     }
            // })
            // jQuery('#id_sales_state').prop('readonly','readonly')
            jQuery('#id_sales_state option').each(function(){
                if (jQuery(this).text()==state){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_sales_state option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=state){
                   
                    options[i].disabled = true;
                }   
              }

            jQuery('#id_invoice_date').val(invoice_date)
            jQuery('#id_invoice_date').prop('readonly','readonly')
            // jQuery('#id_sales_credit option').each(function(){
            //     if(jQuery(this).text()==sales_credit){
                    
            //         jQuery(this).prop('selected','selected')
            //     }

            // })
            // jQuery('#sales_return_credit').prop('readonly','readonly')
            jQuery('#id_sales_credit option').each(function(){
                if (jQuery(this).text()==sales_credit){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_sales_credit option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=sales_credit){
                   
                    options[i].disabled = true;
                }   
              }
            // jQuery('#id_customer option').each(function(){
            //     if(jQuery(this).text()==customer){
            //         jQuery(this).prop('selected','selected')
            //     }
            // })
            // jQuery('#id_customer').prop('readonly','readonly')
            jQuery('#id_customer option').each(function(){
                if (jQuery(this).text()==customer){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_customer option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=customer){
                   
                    options[i].disabled = true;
                }   
              }

            jQuery('#sales_Discount').val(sales_discount)
            jQuery('#sales_Discount').prop('readonly','readonly')
            // jQuery('#id_sales_Paymode option').each(function(){
            //     if(jQuery(this).text()==sales_paymode){
            //         jQuery(this).prop('selected','selected')
            //     }
            //  })
            jQuery('#id_sales_Paymode option').each(function(){
                if (jQuery(this).text()==sales_paymode){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_sales_Paymode option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=sales_paymode){
                   
                    options[i].disabled = true;
                }   
              }

            jQuery('#id_sales_returns_items_bridge-0-sales_item').empty()
            items_length=Object.entries(response['item_details']).length
            document.getElementById('sales_return_addmore_btn').setAttribute('data-itemlength',items_length)
            jQuery('#id_sales_returns_items_bridge-0-sales_item').append("<option value ='0'>--------</option>")
            jQuery.each(response['item_details'],function(i,item){
                jQuery('#id_sales_returns_items_bridge-0-sales_item').append(`<option value = ${i}>${item}</option>`)
            })
        }
    })
})
//id_sales_returns_items_bridge-0-sales_item
jQuery('#sales_return_formsetid').on('blur',"select[name$='sales_item']",function(){
    
    objects=jQuery(this)
    var currentrow = (objects[0]).closest("tr")
    current_item=jQuery(this).val()
    var inv_no=jQuery(`#id_return_salesinvoiceno option:selected`).text()
    const digit_part=(objects[0].name).split("-")[1];
    if (check_duplicate_item(current_item,objects[0].name)==true){
        
        jQuery(this).prop('selectedIndex', 0);
    }
    else {
        //alert("hi")
        jQuery.ajax({
            type:"GET",
            url:"salesitem_bridge_fields",
            data:{
                item:current_item,
                invoice_no:inv_no
            },
            success: function(response){
                //alert("hi")
                jQuery.each(response,function(i,item){
                    item_code=response['item_code']
                    hsn=response['hsn_code']
                    quantity=response['quantity']
                    rate=response['rate']
                    uom=response['uom']
                    disc=response['disc']
                    taxable=response['taxable']
                    tax=response['tax']
                    cgst=response['CGST']
                    cgstamnt=response['CGSTamnt']
                    sgst=response['SGST']
                    sgstamnt=response['SGSTamnt']
                    igst=response['IGST']
                    igstamnt=response['IGSTamnt']
                    amount=response['amount']
                    
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-sales_item_code`).val(item_code)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-sales_item_code`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_hsncode`).val(hsn)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_hsncode`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_quantity`).val(quantity)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_quantity`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_rate`).val(rate)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_rate`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-sales_uom option:selected`).text(uom)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-sales_uom`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-alesitem_disc`).val(disc)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-alesitem_disc`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_taxable`).val(taxable)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_taxable`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_tax`).val(tax)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_tax`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_CGST`).val(cgst)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_CGST`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_CGSTamnt`).val(cgstamnt)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_CGSTamnt`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_SGST`).val(sgst)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_SGST`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_SGSTamnt`).val(sgstamnt)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_SGSTamnt`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_IGST`).val(igst)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_IGST`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_IGSTamnt`).val(igstamnt)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_IGSTamnt`).prop('readonly','readonly')
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_amnt`).val(amount)
                    jQuery(`#id_sales_returns_items_bridge-${digit_part}-salesitem_amnt`).prop('readonly','readonly')
                   
                    sales_summary_caluclations()
                    update_gst_table() 
                    
                })
            }
        })
    }
})


})