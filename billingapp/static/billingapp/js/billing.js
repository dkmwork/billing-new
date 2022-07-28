purchase_combo_itemlist=[];
jQuery(function(){
    jQuery('#id_state_code').blur(function(){
        var code=jQuery(this).val()
        // console.log(code.toString().length)
        if (((code.toString().length)>2)==true)
        {
            jQuery('#id_state_code').val('')
            jQuery('#id_state_code').focus()
            alert("Invalid code !!! State code must be two digits")
        }
    })
    jQuery('#year_formset_add').click(function(){
        var form_index=jQuery('#id_form-TOTAL_FORMS').val()
        jQuery('#year_formset').append(jQuery('#empty_form').html().replace(/__prefix__/g,form_index));
        jQuery('#id_form-TOTAL_FORMS').val(parseInt(form_index) + 1);
    })
function commonfunction(arg,key_no,controlid){
    key_no=key_no
    current_value=arg
    jQuery.ajax({
        type:"GET",
        url:"check_duplicate",
        data:{
            value:current_value,
            check_no:key_no,
        },
        success:function(response){
            console.log(response)
            if (response!=0){
                alert(current_value + " already exists")
                jQuery('#'+controlid).val('')

            }
        }
    })
}
function validate_contact(arg){
    var phone_no=arg
    var phone=jQuery.trim(phone_no)
    intRegex = /^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/
    if((intRegex.test(phone)==false))
    {
        alert('Please enter a valid cintact_number')
    }
}
function validate_email(arg){
    var email=arg
    var re = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ((re.test(email)==false))
    {
        alert("Please enter a valid email address")
    }
}
    jQuery('#id_state_name').change(function(){
        current_state=jQuery(this).val()
        controlid=jQuery(this).attr("id")
        key_no=0
        commonfunction(current_state,key_no,controlid)  
    })
    jQuery('#id_state_code').change(function(){
        current_code=jQuery(this).val()
        controlid=jQuery(this).attr("id")
        key_no=1
        commonfunction(current_code,key_no,controlid)
    })
    jQuery('#id_state_shortname').blur(function(){
        current_shrtname=jQuery(this).val()
        key_no=2
        commonfunction(current_shrtname,key_no)  
    })
    jQuery('#id_city_name').change(function(){
        current_city=jQuery(this).val()
        key_no=3
        commonfunction(current_city,key_no)
    })
    jQuery('#id_city_shortname').change(function(){
        current_shrtname=jQuery(this).val()
        key_no=4
        commonfunction(current_shrtname,key_no)
    })
    jQuery('#id_gst_percent').blur(function(){
        current_gst=jQuery(this).val()
        key_no=5
        commonfunction(current_gst,key_no)
    })
    jQuery('#id_unit_shortname').change(function(){
        current_sunitname=jQuery(this).val()
        key_no=6
        commonfunction(current_sunitname,key_no)
    })
    jQuery('#id_unit_longname').blur(function(){
        current_lunitname=jQuery(this).val()
        key_no=7
        commonfunction(current_lunitname,key_no)
    })
    jQuery('#id_form-0-finacial_year').blur(function(){
        current_year=jQuery(this).val()
        key_no=8
        commonfunction(current_year,key_no)
    })
    jQuery('#id_company_name').change(function(){
        current_company=jQuery(this).val()
        key_no=9
        commonfunction(current_company,key_no)
    })
    jQuery('#id_company_email').change(function(){
        current_cemail=jQuery(this).val()
        key_no=10
        commonfunction(current_cemail,key_no)
    })
    jQuery('#id_company_url').change(function(){
        current_curl=jQuery(this).val()
        key_no=11
        commonfunction(current_curl,key_no)
    })
    jQuery('#id_product_name').change(function(){
        current_product=jQuery(this).val()
        key_no=12
        commonfunction(current_product,key_no)
    })
    jQuery('#id_product_code').change(function(){
        current_pcode=jQuery(this).val()
        key_no=13
        commonfunction(current_pcode,key_no)
    })
    jQuery('#id_party_name').change(function(){
        current_party=jQuery(this).val()
        key_no=14
        commonfunction(current_party,key_no)
    })
    jQuery('#id_contact_no').blur(function(){
        var mobile_no=jQuery(this).val()
        validate_contact(mobile_no)
    })
    jQuery('#id_poc_contact_no').blur(function(){
        var mobile_no=jQuery(this).val()
        validate_contact(mobile_no)
    })
    jQuery('#id_user_contact_no').blur(function(){
        var mobile_no=jQuery(this).val()
        validate_contact(mobile_no)
    })
    jQuery('#id_company_email').blur(function(){
        var email_adrs=jQuery(this).val()
        validate_email(email_adrs)
    })
    jQuery('#id_user_email').blur(function(){
        var email_adrs=jQuery(this).val()
        validate_email(email_adrs)
    })
    jQuery('#id_party_email').blur(function(){
        var email_adrs=jQuery(this).val()
        validate_email(email_adrs)
    })
    
    jQuery('#id_tounit').blur(function(){
        var from_unit=jQuery('#id_fromunit').val()
        var to_unit=jQuery(this).val()
        if(from_unit==to_unit){
            jQuery(this).val('')
            alert("Please enter different units")
        }
    })
function createpaginationcontrols(count,linktobeattached){
    
    jQuery("#"+linktobeattached).empty()
    console.log(count)
    for(var i=0;i<count/2;i++){
        var anchortag=document.createElement('a')
        anchortag.className="pagination"
        anchortag.textContent=i+1
        anchortag.value=i+1
        anchortag.style.display="inline-block"
        anchortag.style.padding="3px"
        jQuery('#'+linktobeattached).append(anchortag) 
    }
}
    jQuery('#state_links').on('click','a',function(event){
        // console.log("i'm")
        var cstatename=jQuery('#stateinfo').val()
        // console.log(cstatename)
        var cstatecode=jQuery('#state_codeinfo').val()
        var cstateshortname=jQuery('#state_shortnameinfo').val()
        var pagenum=jQuery(this).val()
        pagenum=jQuery(this).val()
        jQuery.ajax({
            type:"GET",
            url:"statesearch",
            data:{
                page:pagenum,
                statename:cstatename,
                statecode:cstatecode,
                stateshortname:cstateshortname,
            },
            success:function(response){
                jQuery('#statelist tbody').empty()
                jQuery.each(response,function(i,item){
                    if (i!='total_count'){
                        var new_statename=item.statename
                        var new_statecode=item.statecode
                        var new_stateshortname=item.stateshortname
                        var markup="<tr><td>"+new_statename+"</td><td>"+new_statecode+"</td><td>"+new_stateshortname+"</td></tr>"
                        jQuery('#statelist tbody').append(markup)
                    }
                    else {counter=item.queryset_count}
            })
            }
        })
        event.preventDefault()
        return false
    })
    jQuery('#stateget').click(function(){
        var cstatename=jQuery('#stateinfo').val()
        var cstatecode=jQuery('#state_codeinfo').val()
        var cstateshortname=jQuery('#state_shortnameinfo').val()
        jQuery.ajax({
            type:"GET",
            url:"statesearch",
            data:{
                statename:cstatename,
                statecode:cstatecode,
                stateshortname:cstateshortname,
            },
            success:function(response){
                // console.log(response)
                jQuery('#statelist tbody').empty()
                var counter=0
                jQuery.each(response,function(i,item){
                    console.log(i)
                    console.log(item)
                    if(i!='total_count'){
                        var new_statename=item.statename
                        var new_statecode=item.statecode
                        var new_stateshortname=item.stateshortname
                        var markup="<tr><td>"+new_statename+"</td><td>"+new_statecode+"</td><td>"+new_stateshortname+"</td></tr>"
                        jQuery('#statelist tbody').append(markup)
                    }
                    else {counter=item.queryset_count}
                })
createpaginationcontrols(counter,'state_links')
            }
        })
    })
    jQuery('#category_list').on('click','a',function(event){
        var ccategoryname=jQuery('#categoryinfo').val()
        var cgstpercent=jQuery('#gstinfo').val()
        var chsncode=jQuery('#hsninfo').val()
        var cfinancialyear=jQuery('#financialyearinfo').val()
        pagenum=jQuery(this).val()
        jQuery.ajax({
            type:'GET',
            url:"categorysearch",
            data:{
                categoryname:ccategoryname,
                gstpercent:cgstpercent,
                hsncode:chsncode,
                financialyear:cfinancialyear,
                page:pagenum,
            },
            success:function(response){
                // console.log(response)
                jQuery('#category_table_list tbody').empty()
                jQuery.each(response,function(i,item){
                    if (i!='total_count'){
                        var new_categoryname=item.categoryname
                        var new_gstpercent=item.gstpercent
                        var new_hsncode=item.hsncode
                        var new_financialyear=item.financialyear
                        var markup="<tr><td>"+new_categoryname+"</td><td>"+new_gstpercent+"</td><td>"+
                        new_hsncode+"</td><td>"+new_financialyear+"</td></tr>"
                        jQuery("#category_table_list tbody").append(markup);
                    }
                    else {counter=item.queryset_count}
                })
            }
        })
        event.preventDefault()
        return false
    })
    jQuery('#categoryget').click(function(){
        console.log("here")
        var ccategoryname=jQuery('#categoryinfo').val()
        var cgstpercent=jQuery('#gstinfo').val()
        var chsncode=jQuery('#hsninfo').val()
        var cfinancialyear=jQuery('#financialyearinfo').val()
        jQuery.ajax({
            type:'GET',
            url:"categorysearch",
            data:{
                categoryname:ccategoryname,
                gstpercent:cgstpercent,
                hsncode:chsncode,   
                financialyear:cfinancialyear,
            },
            success:function(response){
                // console.log(response)
                jQuery('#category_table_list tbody').empty()
                var counter=0
                jQuery.each(response,function(i,item){
                    if (i!='total_count'){
                        var new_categoryname=item.categoryname
                        var new_gstpercent=item.gstpercent
                        var new_hsncode=item.hsncode
                        var new_financialyear=item.financialyear
                        var markup="<tr><td>"+new_categoryname+"</td><td>"+new_gstpercent+"</td><td>"
                        +new_hsncode+"</td><td>"+new_financialyear+"</td></tr>"
                        jQuery("#category_table_list tbody").append(markup);
                    }
                    else {counter=item.queryset_count}
                    console.log('hi')
                })
                // console.log(counter)
                createpaginationcontrols(counter,"category_list")
            }
        })
    })
    jQuery('#product_links').on('click','a',function(event){
        
        var ccategory=jQuery('#pcategoryinfo').val()
        var cproductname=jQuery('#productinfo').val()
        var cproductcode=jQuery('#codeinfo').val()
        var cbaseunit=jQuery('#unitinfo').val()
        pagenum=jQuery(this).val()
        jQuery.ajax({
            type:"GET",
            url:"productsearch",
            data:{
                pcategory:ccategory,
                productname:cproductname,
                productcode:cproductcode,
                baseunit:cbaseunit,
                page:pagenum,
            },
            success:function(response){
                jQuery('#productlist tbody').empty()
                jQuery.each(response,function(i,item){
                    if (i!='total_count'){
                        var pcate=item.pcategory
                        var pname=item.productname
                        var pcode=item.productcode
                        var pbase=item.baseunit
                        var markup="<tr><td>"+pcate+"</td><td>"+pname+"</td><td>"+pcode+"</td><td>"+pbase+"</td></tr>"
                        jQuery('#productlist').append(markup);
                    }
                    else {counter=item.queryset_count}
                })
            }
        })
        event.preventDefault()
        return false
    })

    jQuery('#productget').click(function(){
        var ccategory=jQuery('#pcategoryinfo').val()
        console.log(ccategory)
        var cproductname=jQuery('#productinfo').val()
        var cproductcode=jQuery('#codeinfo').val()
        var cbaseunit=jQuery('#unitinfo').val()
        jQuery.ajax({
            type:"GET",
            url:"productsearch",
            data:{
                pcategory:ccategory,
                productname:cproductname,
                productcode:cproductcode,
                baseunit:cbaseunit,
            },
            success:function(response){
                // console.log(response)
                jQuery('#productlist tbody').empty()
                var counter=0
                jQuery.each(response,function(i,item){
                    if (i!='total_count'){
                        var pcate=item.pcategory
                        var pname=item.productname
                        var pcode=item.productcode
                        var pbase=item.baseunit
                        var markup="<tr><td>"+pcate+"</td><td>"+pname+"</td><td>"+pcode+"</td><td>"+pbase+"</td></tr>"
                        jQuery('#productlist').append(markup)
                    }
                    else {counter=item.queryset_count}
                    
                })
                console.log(counter)
                createpaginationcontrols(counter,"product_links")
            }
        })
    })
    jQuery('#partylist_links').on('click','a',function(event){
        console.log("hi")
        var cpartyname=jQuery('#partyinfo').val()
        
        var ccontactnumber=jQuery('#contact_numberinfo').val()
        
        pagenum=jQuery(this).val()  
        jQuery.ajax({
            type:"GET",
            url:"partysearch",
            data:{
                partyname:cpartyname,
                
                contactnumber:ccontactnumber,
                
                page:pagenum,
            },
            success:function(response){
                
                jQuery('#partylist tbody').empty()
                jQuery.each(response,function(i,item){
                    if(i!='total_count'){
                        var pname=item.partyname
                        var pstreet=item.partystreet
                        var pcity=item.partycity
                        var pstate=item.partystate
                        var pcontactnumber=item.contactnumber
                        var pemail=item.partyemail
                        var pgst=item.gst
                        var pcategory=item.partycategory
                        var ptype=item.partytype
                        var markup=`<tr><td>${pname}</td><td>${pstreet}</td><td>${pcity}</td><td>${pstate}</td><td>${pcontactnumber}
                        </td><td>${pemail}</td><td>${pgst}</td><td>${pcategory}</td><td>${ptype}`
                        jQuery('#partylist tbody').append(markup)
                    }
                    else{counter=item.queryset_count}
                })
            }
        })
        event.preventDefault()
        return false
    })
    jQuery('#partyget').click(function(){
        var cpartyname=jQuery('#partyinfo').val()
        
        var ccontactnumber=jQuery('#contact_numberinfo').val()
        
        jQuery.ajax({
            type:"GET",
            url:"partysearch",
            data:{
                partyname:cpartyname,
                contactnumber:ccontactnumber,
            },
            success:function(response){
                // console.log(response)
                jQuery('#partylist tbody').empty()
                var counter=0
                jQuery.each(response,function(i,item){
                    console.log(i)
                    console.log(item)
                    if(i!='total_count'){
                        
                        var pname=item.partyname
                        var pstreet=item.partystreet
                        var pcity=item.partycity
                        var pstate=item.partystate
                        var pcontactnumber=item.contactnumber
                        var pemail=item.partyemail
                        var pgst=item.gst
                        var pcategory=item.partycategory
                        var ptype=item.partytype
                        // var markup=`<tr><td>${pname}</td><td>${pstreet}</td><td>${pcity}</td><td>${pstate}</td><td>${pcontactnumber}</td><td>${pemail}</td><td>${pgst}</td><td>${pcategory}</td><td>${ptype}</td></tr>`
                        var markup="<tr><td>"+pname+"</td><td>"+pstreet+"</td><td>"+pcity+"</td><td>"+pstate+"</td><td>"+pcontactnumber+"</td><td>"+pemail+"</td><td>"+pgst+"</td><td>"+pcategory+"</td><td>"+ptype+"</td></tr>"
                        // alert(markup)
                        jQuery('#partylist tbody').append(markup)
                    }
                    else {counter=item.queryset_count}
                })
                // console.log(counter)
                createpaginationcontrols(counter,'partylist_links')
            }
        })
    })
    jQuery('#id_category').change(function(){
        //alert("hi")
        var ccategoryname=jQuery(this).val()
        jQuery.ajax({
            type:"GET",
            url:"gst_and_hsn_select",
            data:{
                categoryname:ccategoryname,
            },
            success:function(response){
                jQuery.each(response,function(i,item){
                jQuery('#gst_percent_id').val(item.gst)
                jQuery('#hsn_code_id').val(item.hsn)
                })  
            }
        })
    })
// jQuery('#purchase_formsetid').on('change','select[name$="-item"]',function(){
//     var object=jQuery(this)
//     console.log(object[0].name)
//     const digit_part=(object[0].name).split("-")[1];
//     var 
// })
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
function update_footer_table_after_del(digit_part,check_value){
    let total_taxable_amnt=document.getElementById('id_purchase_taxableamnt').value
    let total_cgst_amnt=document.getElementById('id_purchase_CGSTAmnt').value 
    let total_sgst_amnt=document.getElementById('id_purchase_SGSTAmnt').value 
    let total_igst_amnt=document.getElementById('id_purchase_IGSTAmnt').value  
    let stotal_amnt=document.getElementById('id_purchase_subtotal').value 
    let gtotal_amnt=document.getElementById('id_purchase_GTotal').value  
    let purchase_discount=document.getElementById('id_purchase_Discount').value 
    const taxable_amnt=document.getElementById(`id_purchade_items_bridge-${digit_part}-item_taxable`).value
    const cgst_amnt=document.getElementById(`id_purchade_items_bridge-${digit_part}-item_CGST`).value  
    const sgst_amnt=document.getElementById(`id_purchade_items_bridge-${digit_part}-item_SGST`).value 
    const igst_amnt=document.getElementById(`id_purchade_items_bridge-${digit_part}-item_IGST`).value 
    const total_amnt=document.getElementById(`id_purchade_items_bridge-${digit_part}-item_amnt`).value
    if (check_value==1){
    total_taxable_amnt=parseFloat(total_taxable_amnt)-parseFloat(taxable_amnt)
    total_cgst_amnt=parseInt(total_cgst_amnt)-parseInt(cgst_amnt)
    total_sgst_amnt=parseInt(total_sgst_amnt)-parseInt(sgst_amnt)
    total_igst_amnt=parseInt(total_igst_amnt)-parseInt(igst_amnt)
    stotal_amnt=parseInt(stotal_amnt)-parseInt(total_amnt)
    gtotal_amnt=parseFloat(stotal_amnt)-parseFloat(purchase_discount)
   
}
else if(check_value==0){
    total_taxable_amnt=parseInt(total_taxable_amnt)+parseInt(taxable_amnt)
    total_cgst_amnt=parseInt(total_cgst_amnt)+parseInt(cgst_amnt)
    total_sgst_amnt=parseInt(total_sgst_amnt)+parseInt(sgst_amnt)
    total_igst_amnt=parseInt(total_igst_amnt)+parseInt(igst_amnt)
    stotal_amnt=parseInt(stotal_amnt)+parseInt(total_amnt)
    gtotal_amnt=parseFloat(stotal_amnt)-parseFloat(purchase_discount)
}
    document.getElementById('id_purchase_taxableamnt').value=total_taxable_amnt
    document.getElementById('id_purchase_CGSTAmnt').value=total_cgst_amnt
    document.getElementById('id_purchase_SGSTAmnt').value=total_sgst_amnt
    document.getElementById('id_purchase_IGSTAmnt').value=total_igst_amnt
    document.getElementById('id_purchase_subtotal').value=stotal_amnt
    document.getElementById('id_purchase_GTotal').value=gtotal_amnt
}
function update_gst_table(){
    
    const tax_refs=Array.from(document.querySelectorAll(`input[name$="item_tax"]`));
    const sgst_refs=Array.from(document.querySelectorAll(`input[name$="item_SGST"]`));
    const cgst_refs=Array.from(document.querySelectorAll(`input[name$="item_CGST"]`));
    const igst_refs=Array.from(document.querySelectorAll(`input[name$="item_IGST"]`));
    const amount_refs=Array.from(document.querySelectorAll(`input[name$="item_amnt"]`));
    const delete_refs=Array.from(document.querySelectorAll(`input[name$="-DELETE"]`));
    var formsetlist=[];
    
    for(const item of tax_refs){
        //console.log(item)
        const index=item.name.split('-')[1]
        // console.log(index)
        var delete_val=delete_refs.find(x=>x.name.includes(index))
        //console.log(delete_val.checked)
        if (index!='__prefix__'){
            if (delete_val.checked==false){
       var objtax=tax_refs.find(x=>x.name.includes(index))
       var tax=objtax.value
    //    console.log(tax)
       var objsgst=sgst_refs.find(x=>x.name.includes(index))
       var sgst=objsgst.value
       var objcgst=cgst_refs.find(x=>x.name.includes(index))
       var cgst=objcgst.value
       var objigst=igst_refs.find(x=>x.name.includes(index))
       var igst=objigst.value
       var objamnt=amount_refs.find(x=>x.name.includes(index))
       var amnt=objamnt.value
    //    console.log(amnt)
       var dict={"tax":tax,"sgst":sgst,"cgst":cgst,"igst":igst,"amount":amnt}
       formsetlist.push(dict)
    //    console.log(dict)
}
    }
}
// console.log(list)
// function for groupping and adding values according to taxes.

create_html_for_smallgrid(formsetlist) 
}
function create_html_for_smallgrid(formsetlist){
    var gst_table=document.getElementById("id_purchase_gst_summary")
    var result = [];
formsetlist.reduce(function(res, value) {
	// console.log(value)
  if (!res[value.tax]) {
	
    res[value.tax] = { tax: value.tax, cgst: 0,sgst:0, igst:0 ,amount:0 };
    result.push(res[value.tax])
  }
  res[value.tax].cgst=parseFloat(res[value.tax].cgst)+parseFloat(value.cgst);
  res[value.tax].sgst=parseFloat(res[value.tax].sgst)+parseFloat(value.sgst);
  console.log(value.igst)
  
  res[value.tax].igst=parseFloat(res[value.tax].igst)+parseFloat(value.igst);
  //console.log(res[value.tax].igst)
  res[value.tax].amount=parseFloat(res[value.tax].amount)+parseFloat(value.amount);
//   console.log(res[value.tax].amount)
  
  return res; // back to if condition
}, {});
delete_gameboard('purchase')
//console.log(result)

for (const row of result){
    if (row.tax!=''){
    
    let new_row=gst_table.insertRow(-1);
    
    let new_cell=new_row.insertCell(0)
    let newText=document.createTextNode(row.tax)
    new_cell.append(newText)
    new_cell=new_row.insertCell(1)
    newText=document.createTextNode(row.cgst)
    new_cell.append(newText)
    new_cell=new_row.insertCell(2)
    newText=document.createTextNode(row.sgst)
    new_cell.append(newText)
    new_cell=new_row.insertCell(3)
    //console.log(row.igst)
    newText=document.createTextNode(row.igst)
    new_cell.append(newText)
    new_cell=new_row.insertCell(4)
    newText=document.createTextNode(row.amount)
    new_cell.append(newText)
    
}
}
result=[];
}
function update_purchase_combo_itemlist(){
    const item_refs=Array.from(document.querySelectorAll(`select[name$="-item"]`))
    for (item of item_refs){
        if (!item.name.includes('prefix')){
       // alert(item.value)
        purchase_combo_itemlist.push(item.value)
    }
    }
    //console.log(purchase_combo_itemlist)
}
function check_duplicate_item(citemid,controlname){
    //alert(citemid)
    //console.log(controlname)
    // make an array of the list form querySelectorAll using Array.from
    const item_refs=Array.from(document.querySelectorAll(`select[name$="-item"]`))
    //console.log(item_refs)
    //filter(lambda expression) to filter a value from a list
    const filtered_item_refs=item_refs.filter(x=>x.name!=controlname)
    for (item of filtered_item_refs){
        //console.log(item.value)
        // includes() to check for a particular string in a string
         if (!item.name.includes('prefix')){
             if (item.value == citemid){
               alert("Item already exists !!")
               return true
            }
         }
    }
}

// function check_dupliacte_items(citemid){
//     update_purchase_combo_itemlist()
//     console.log(purchase_combo_itemlist)
//     if(purchase_combo_itemlist.includes(citemid)==false){
//     purchase_combo_itemlist.push(citemid)
//     //console.log(purchase_combo_itemlist)
// }
// else{
//     alert("Item already exists !!")
//     return true;
// }  
// }
// function update_footer_table_checkeddel(digit_part){
// const taxbleamnt_refs=Array.from(document.querySelectorAll(`input[name$=]`))


// var taxable_amnt=jQuery(`input[name$="${digit_part}-item_taxable"]`).val()
// var total_taxable_amnt=jQuery('#id_purchase_taxableamnt').val()
// var delete_val=jQuery(`input[name$="${digit_part}-DELETE"]`).val()
// console.log(delete_val)

// const delete_refs=Array.from(document.querySelectorAll(`input[name$="-DELETE"]`));
// var delete_val=delete_refs.find(x=>x.name.includes(digit_part))
//         console.log(delete_val.checked)
//         if (delete_val.checked==false){
//     total_taxable_amnt=total_taxable_amnt-taxable_amnt
//     jQuery('#id_purchase_taxableamnt').val(total_taxable_amnt)
//     }
//     else{
//         jQuery('#id_purchase_taxableamnt').val(total_taxable_amnt) 
//     }

jQuery('#purchase_formsetid').on('change','input[name$="-DELETE"]',function(){
var object=jQuery(this)
console.log(object[0].checked)
const digit_part=(object[0].name).split("-")[1];
if (object[0].checked==true){
    update_footer_table_after_del(digit_part,1)
}
else{
    update_footer_table_after_del(digit_part,0)
}
update_gst_table()

})
//update_footer_table_checkeddel(digit_part)
// var taxable_amnt=jQuery(`input[name$="${digit_part}-item_taxable"]`).val()
// var tax=jQuery(`input[name$="${digit_part}-item_tax"]`).val()
// var total_taxable_amnt=jQuery('#id_purchase_taxableamnt').val()
// total_taxable_amnt=total_taxable_amnt-taxable_amnt
// jQuery('#id_purchase_taxableamnt').val(total_taxable_amnt)

jQuery('#purchase_formsetid').on('change','select[name$="-item"]',function(){
    //alert('hii')
    var urlstring=""
    // this step helps to go to purchaselist_edit mode instead of create purchase
    // property returns the URL of the current page.
    if(window.location.href.includes('purchaselist_edit')){
        urlstring='../purchase_hsn_gst_select'
    }
    //the else side acts the normal create purchase.
    else{
        urlstring='purchase_hsn_gst_select'
    }
    var citemid=jQuery(this).val()
    
    var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1];
    if (check_duplicate_item(citemid,object[0].name)==true){
        jQuery(this).prop('selectedIndex', 0);
    }
    else {
        
    // console.log(digit_part)
    // var ccategoryname=jQuery(`input[name$="${digit_part}-item"]`).val()
    // console.log(ccategoryname)
    jQuery.ajax({
        type:"GET",
        url:urlstring,
        data:{
            itemid:citemid,
        },
        success:function(response){
            
        //    console.log(response)
            
                jQuery(`input[name$="${digit_part}-item_hsncode"]`).val(response.hsn_code)
                jQuery(`input[name$="${digit_part}-item_tax"]`).val(response.gst_percent)
                update_gst_table() 
        }
    }) 
}
})
function check_item_to_be_filled(digit_part){
    
    if (jQuery(`select[name$="${digit_part}-item"]`).val()==''){
        alert("Item field must be filled")
        return true
    }
    else {
        return false
    }
}
jQuery('#purchase_formsetid').on('change',"input[name$='_quantity']",function(){
// alert("hi")
var object=jQuery(this)
    const digit_part=(object[0].name).split("-")[1]
    // console.log(digit_part)
    if (check_item_to_be_filled(digit_part)==true){
        jQuery(this).val('')
    }
    else{
    calculation(digit_part)
    purchase_summary_caluclations()
    update_gst_table() 
}
})
jQuery('#purchase_formsetid').on('change',"input[name$='_rate']",function(){
     //alert("hi")
    var object=jQuery(this)
        const digit_part=(object[0].name).split("-")[1]
        if (check_item_to_be_filled(digit_part)==true){
            jQuery(this).val('')
        }
        else{
        // console.log(digit_part) 
        calculation(digit_part)
        purchase_summary_caluclations()
        update_gst_table() 
        }
    })
    jQuery('#purchase_formsetid').on('change',"input[name$='_disc']",function(){
        // alert("hi")
        var object=jQuery(this)
            const digit_part=(object[0].name).split("-")[1]
            // console.log(digit_part)
            if (check_item_to_be_filled(digit_part)==true){
                jQuery(this).val('')
            }
            else{
            calculation(digit_part)
            purchase_summary_caluclations()
            update_gst_table() 
            }
        })
jQuery('#id_purchase_Discount').change(function(){
    adding_purchase_gtotal()
})
function calculation(digit_part){
    var quantity=jQuery(`input[name$="${digit_part}-item_quantity"]`).val()
    var rate=jQuery(`input[name$="${digit_part}-item_rate"]`).val()
    var disc=jQuery(`input[name$="${digit_part}-item_disc"]`).val()
    var taxable=quantity*rate-disc
    jQuery(`input[name$="${digit_part}-item_taxable"]`).val(taxable)
    //var st=jQuery(`input[name$="${digit_part}-item_tax"]`).val()/2
    //var amount=taxable*st/100
    //var total_amount=parseInt(taxable)+amount*2
    jQuery(`input[name$="${digit_part}-item_disc"]`).val(0)
    //jQuery(`input[name$="${digit_part}-item_CGST"]`).val(amount)
    //jQuery(`input[name$="${digit_part}-item_SGST"]`).val(amount)
    //jQuery(`input[name$="${digit_part}-item_amnt"]`).val(total_amount)

    var st=jQuery(`input[name$="${digit_part}-item_tax"]`).val()
    var amount=taxable*st/100
    var total_amount=parseInt(taxable)+amount
    jQuery(`input[name$="${digit_part}-item_amnt"]`).val(total_amount)
    if (jQuery('#id_purchase_type').val()=='Intra'){
        jQuery(`input[name$="${digit_part}-item_IGST"]`).val(amount)
        jQuery(`input[name$="${digit_part}-item_CGST"]`).val(0)
        jQuery(`input[name$="${digit_part}-item_SGST"]`).val(0)
    }
    else {
        jQuery(`input[name$="${digit_part}-item_IGST"]`).val(0)
        jQuery(`input[name$="${digit_part}-item_CGST"]`).val(amount/2)
        jQuery(`input[name$="${digit_part}-item_SGST"]`).val(amount/2)
    }
}
function purchase_summary_caluclations(digit_part){
    adding_purchase_subtotal()
    adding_purchase_txblamnt()
    adding_purchase_cgst()
    adding_purchase_sgst()
    adding_purchase_gtotal()
    purchase_igst()
    // adding_purchase_igst(digit_part)
}
function adding_purchase_subtotal(){
    const refs=Array.from(document.querySelectorAll(`input[name$="item_amnt"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop();
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseInt(accumulator)+parseInt(currentvalue)
    })
    console.log(sum)
    
const sub_total=document.getElementById('id_purchase_subtotal');
sub_total.value=sum;
}

function adding_purchase_txblamnt(){
    const refs=Array.from(document.querySelectorAll(`input[name$="item_taxable"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    const taxbl_amnt=document.getElementById('id_purchase_taxableamnt');
    taxbl_amnt.value=sum;
}
function adding_purchase_cgst(){
    const refs=Array.from(document.querySelectorAll(`input[name$="item_CGST"]`));
    
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,curentvalue)=>{
        return parseFloat(accumulator)+parseFloat(curentvalue)
    })
    const cgst_amnt=document.getElementById('id_purchase_CGSTAmnt');
    cgst_amnt.value=sum
}
function purchase_igst(){
    const refs=Array.from(document.querySelectorAll(`input[name$="item_IGST"]`));
    const newarray=refs.map(x=>x.value)
    console.log(newarray)
    newarray.pop()
    //console.log(newarray)
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    const igst_amnt=document.getElementById('id_purchase_IGSTAmnt');
    igst_amnt.value=sum
}
// function adding_purchase_igst(){
//     const refs=Array.from(document.querySelectorAll(`input[name$="item_IGST"]`));
//     refs.value=0;
//     console.log(refs)
// }
function adding_purchase_sgst(){
    
    const refs=Array.from(document.querySelectorAll(`input[name$="item_SGST"]`));
    const newarray=refs.map(x=>x.value)
    newarray.pop()
    const sum=newarray.reduce((accumulator,currentvalue)=>{
        return parseFloat(accumulator)+parseFloat(currentvalue)
    })
    const sgst_amnt=document.getElementById('id_purchase_SGSTAmnt');
    sgst_amnt.value=sum
}
function adding_purchase_gtotal(){
const refs=document.getElementById('id_purchase_subtotal');
const sub_total=refs.value
//jQuery('#id_purchase_Discount').prop('disabled','disabled')
const discnt=document.getElementById('id_purchase_Discount');
const disc_amnt=discnt.value
// console.log(discnt.value.length)
if (discnt.value.length>0)
{const gtotal=parseInt(sub_total)-parseInt(disc_amnt)
const g_total=document.getElementById('id_purchase_GTotal');
g_total.value=gtotal
}
else{
    const g_total=document.getElementById('id_purchase_GTotal');
    g_total.value=sub_total
}
}
// jQuery('input[name$="-item_quantity').change(function(){
//     var quantity=jQuery(this).val()
//     var rate=jQuery('input[name$="-item_rate"]').val()
//     var taxable=quantity*rate;
//    jQuery('input[name$="-item_taxable"]').val(taxable)
//    var st=jQuery('input[name$="-item_tax').val()/2
//     var amount=jQuery('input[name$="-item_taxable"]').val()*st/100;
//     var total=parseInt(jQuery('input[name$="-item_taxable"]').val())+(amount)*2;
//     jQuery('input[name$="-item_CGST"]').val(amount)
//     jQuery('input[name$="-item_SGST"]').val(amount)
//     jQuery('input[name$="-item_amnt"]').val(total)
// })
// jQuery('input[name$="-item_rate').change(function(){
//     var rate=jQuery(this).val()
//     var quantity=jQuery('input[name$="-item_quantity"]').val()
//     var taxable=quantity*rate;
//    jQuery('input[name$="-item_taxable"]').val(taxable)
//    var st=jQuery('input[name$="-item_tax').val()/2
//     var amount=jQuery('input[name$="-item_taxable"]').val()*st/100;
//     var total=parseInt(jQuery('input[name$="-item_taxable"]').val())+(amount)*2;
//     jQuery('input[name$="-item_CGST"]').val(amount)
//     jQuery('input[name$="-item_SGST"]').val(amount)
//     jQuery('input[name$="-item_amnt"]').val(total)
// })

// jQuery('input[name$="-item_rate"]').change(function(){
//     var st=jQuery('input[name$="-item_tax').val()/2
//     var amount=jQuery('input[name$="-item_taxable"]').val()*st/100;
//     var total=parseInt(jQuery('input[name$="-item_taxable"]').val())+(amount)*2;
//     jQuery('input[name$="-item_CGST"]').val(amount)
//     jQuery('input[name$="-item_SGST"]').val(amount)
//     jQuery('input[name$="-item_amnt"]').val(total)

// })

function check_addmore_table_values(form_index){ 
    // sales_items_bridge-0-salesitem_amnt
    var amount=jQuery(`input[name$="${(form_index)-1}-item_amnt"]`).val()
    var item=jQuery(`select[name$="${(form_index)-1}-item"]`).val()
    // sales_items_bridge-0-sales_item
    if (jQuery(`input[name$="${(form_index)-1}-item_disc"]`).val()==''){
        // sales_items_bridge-0-salesitem_disc
        jQuery(`input[name$="${(form_index)-1}-item_disc"]`).val(0)
    }
    if (item>0 & amount>0){
        return true
}
else {
    return false
}
}

//make 'readonly' empty-form fileds
function change_to_readonly_fields(){
    const hsn_refs=Array.from(document.querySelectorAll(`input[name$="item_hsncode"]`));
    for(const item of hsn_refs){
        item.readOnly=true
    }
    const tax_refs=Array.from(document.querySelectorAll(`input[name$="item_tax"]`));
    for(const item of tax_refs){
        item.readOnly=true
    }
    const cgst_refs=Array.from(document.querySelectorAll(`input[name$="item_CGST"]`));
    for(const item of cgst_refs){
        item.readOnly=true
    } 
    const sgst_refs=Array.from(document.querySelectorAll(`input[name$="item_SGST"]`));
    for(const item of sgst_refs){
        item.readOnly=true
    } 
    const igst_refs=Array.from(document.querySelectorAll(`input[name$="item_IGST"]`));
    for(const item of igst_refs){
        //item.value=0
        item.readOnly=true
    } 
    const taxable_refs=Array.from(document.querySelectorAll(`input[name$="item_taxable"]`));
    for(const item of taxable_refs){
        item.readOnly=true
    } 
    const amnt_refs=Array.from(document.querySelectorAll(`input[name$="item_amnt"]`));
    for(const item of amnt_refs){
        item.readOnly=true
    } 
}
jQuery('#addmore_btn').click(function(){
    var form_index=$('#id_purchade_items_bridge-TOTAL_FORMS').val();
    //var x=jQuery('#purchase_formsetid').find('table').length
    if (check_addmore_table_values(form_index)==true){
    jQuery('#purchase_formsetid').append(jQuery('#empty_form_id').html().replace(/__prefix__/g,form_index));
    jQuery('#id_purchade_items_bridge-TOTAL_FORMS').val(parseInt(form_index)+1);
}
change_to_readonly_fields()
}) 


jQuery('#purchase_return_addmore_btn').click(function(){
    var current_button=document.getElementById('purchase_return_addmore_btn')
original_itemlength=current_button.getAttribute('data-itemlength')

    optionvaluejson={}
    var form_index=jQuery('#id_sales_items_bridge-TOTAL_FORMS').val()
    if (form_index<original_itemlength){
    jQuery('#purchase_return_formsetid') .append(jQuery('#purchase_return_empty_form_id').html().replace(/__prefix__/g,form_index));
    jQuery('#id_purchase_items_returns_bridge-TOTAL_FORMS').val(parseInt(form_index)+1);
    jQuery(`#id_purchase_items_returns_bridge-${form_index}-item`).empty()
    jQuery('#id_purchase_items_returns_bridge-0-item option').each(function(){
    var item_value=jQuery(this).val()
    var item_text=jQuery(this).text()
    //console.log(item_text)
    //console.log(item_value)
        jQuery(`#id_purchase_items_returns_bridge-${form_index}-item`).append(`<option value=${item_value}>${item_text}</option>`)
    })
}
})

jQuery('#id_return_invoice_no').change(function(){
    //alert("hi")
    var invno=jQuery(`#id_return_invoice_no option:selected`).text()
    //alert(invno)
    jQuery.ajax({
        type:"GET",
        url:"purchasereturninfo",
        data:{
            invoice_no:invno,
        },
        success:function(response){
            state=response['purchase_details']['purchase_state__state_name']
            supplier=response['purchase_details']['supplier__party_name']
            //console.log(supplier)
            invoice_date=response['purchase_details']['invoice_date']
            purchase_type=response['purchase_details']['purchase_type']
            remarks=response['purchase_details']['remarks']
            Discount=response['purchase_details']['purchase_Discount']
            pay_mode=response['purchase_details']['purchase_Paymode__payment_method']
            //console.log(pay_mode)
            jQuery('#id_remarks').val(remarks)
            jQuery('#id_remarks').prop('readonly','readonly')
            jQuery('#id_invoice_date').val(invoice_date)
            jQuery('#id_invoice_date').prop('readonly','readonly')
            jQuery('#id_purchase_type').val(purchase_type)
            jQuery('#id_purchase_type').prop('readonly','readonly')
            jQuery('#id_purchase_Discount').val(Discount)
            jQuery('#id_purchase_Discount').prop('readonly','readonly')
            
            // jQuery('#id_purchase_Paymode option').each(function(){
            //     if (jQuery(this).text()==pay_mode){
            //         jQuery(this).prop('selected','selected')
            //     }
            // })
            // jQuery('#id_purchase_Paymode').prop('readonly','readonly')
            jQuery('#id_purchase_Paymode option').each(function(){
                if (jQuery(this).text()==pay_mode){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_purchase_Paymode option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=pay_mode){
                   
                    options[i].disabled = true;
                }   
              }

            // using loop through option as it is a combo box
            // jQuery('#id_purchase_state option').each(function(){
            //     if(jQuery(this).text()==state){
            //         jQuery(this).prop('selected','selected')
            //     }
            // })
            // jQuery('#id_purchase_state').prop('readonly','readonly')
            jQuery('#id_purchase_state option').each(function(){
                if (jQuery(this).text()==state){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_purchase_state option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=state){
                   
                    options[i].disabled = true;
                }   
              }
              jQuery('#id_supplier option').each(function(){
                if (jQuery(this).text()==supplier){
                    jQuery(this).prop('selected','selected')
                }   
            })
            var options = jQuery('#id_supplier option');
            for (var i=0; i<options.length;i++) {
                console.log(options[i].text)
                if (options[i].text !=supplier){
                   
                    options[i].disabled = true;
                }   
              }
           
            // another way of set a value to the combobox
            // jQuery("#id_supplier option").filter(function() {
            //     //may want to use $.trim in here
            //     return jQuery(this).text() == supplier;
            //   }).attr('selected',true);  
            //   jQuery('#id_supplier').prop('readonly','readonly')
              jQuery('#id_purchase_items_returns_bridge-0-item').empty()
              //console.log(response['item_details'])
              items_length=Object.entries(response['item_details']).length
              //console.log(items_length)
              document.getElementById('purchase_return_addmore_btn').setAttribute('data-itemlength',items_length)
              jQuery('#id_purchase_items_returns_bridge-0-item').append("<option value='0'>-------</option>")
              //jQuery('#id_purchade_items_bridge-0-item').append("<option value='0'>-------</option>")
              jQuery.each(response['item_details'],function(i,item){
                console.log(item)
                  jQuery('#id_purchase_items_returns_bridge-0-item').append(`<option value=${i}>${item}</option>`)
                  //jQuery('id_purchade_items_bridge-0-item').append(`<option value=${i}>${item}</option>`)
              })  
        }   
    }) 

jQuery('#purchase_return_formsetid').on('blur',"select[name$='-item']",function(){
       objects=jQuery(this)
       //console.log(objects[0])
       var currentrow = (objects[0]).closest("tr") //find the textbox row of the control in which has an existing value.
       //console.log(currentrow)
       current_item=jQuery(this).val()
       var inv_no=jQuery(`#id_return_invoice_no option:selected`).text()
        const digit_part=(objects[0].name).split("-")[1];
        //alert(digit_part)
        if (check_duplicate_item(current_item,objects[0].name)==true){
            jQuery(this).prop('selectedIndex', 0);
        }
        else {
        jQuery.ajax({
            type:"GET",
            url:"item_bridge_fields",
            data:{
                item:current_item,
                invoice_no:inv_no
            },
            success:function(response){
                //console.log(response['purchase_details']['purchase_Discount'])
                //console.log(response['item_details']) 
                alert("hi")       
                jQuery.each(response,function(i,item){
                    hsn=response['hsn_code']
                    quantity=response['quantity']
                    rate=response['rate']
                    uom=response['uom']
                    
                    disc=response['disc']
                    taxable=response['taxable']
                    tax=response['tax']
                    cgst=response['CGST']
                    sgst=response['SGST']
                    igst=response['IGST']
                    amount=response['amount']
                    //console.log(hsn)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_hsncode`).val(hsn)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_hsncode`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_quantity`).val(quantity)
                    currentrow.setAttribute("data-actualquantity", quantity)// set the attribute value to 'actualquantity' from 'quantity' using data-property.
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_rate`).val(rate)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_rate`).prop('readonly','readonly')
                    //jQuery(`#id_purchase_items_returns_bridge-${digit_part}-uom option:selected`).text(uom)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-uom option`).each(function () {        
                        if ($(this).text() == uom) {
                            $(this).prop('selected', 'selected');
                        }
                    });
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-uom`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_disc`).val(disc)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_disc`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_taxable`).val(taxable)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_taxable`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_tax`).val(tax)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_tax`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_CGST`).val(cgst)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_CGST`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_SGST`).val(sgst)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_SGST`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_IGST`).val(igst)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_IGST`).prop('readonly','readonly')
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_amnt`).val(amount)
                    jQuery(`#id_purchase_items_returns_bridge-${digit_part}-item_amnt`).prop('readonly','readonly')
                    purchase_summary_caluclations()
                    update_gst_table() 
                })
            }
        })
    }
    }) 
    

jQuery('#purchase_return_formsetid').on('change',"input[name$='-item_quantity']",function(){
    var current_quantity=jQuery(this).val()
    console.log(current_quantity)
    objects=jQuery(this)
    var currentrow = (objects[0]).closest("tr")
    var actualquantity=currentrow.getAttribute('data-actualquantity')// check  attribute of "currentrow" settings in item_bridge_fields()- retrieve existing quantity value from actualquantity using getattribute.
    console.log(actualquantity)
    const digit_part=(objects[0].name).split("-")[1];
    if (parseFloat(actualquantity)< parseFloat(current_quantity)){
        alert("Enter a quantity within the existing value !!!")
        jQuery(this).val(actualquantity)
    }
    else{
        calculation(digit_part)
        purchase_summary_caluclations()
        update_gst_table() 
    }
    })  
})
// set the 'puchase type' according to the selected 'state'

jQuery('#id_purchase_state').change(function(){
    if (jQuery('#id_purchase_state option:selected').text()=="Kerala"){
        jQuery('#id_purchase_type').val('Local')
    }
    else {
        jQuery('#id_purchase_type').val('Intra')
    }
    jQuery('#id_purchase_type').prop('readonly','readonly')
})
 })
    
    