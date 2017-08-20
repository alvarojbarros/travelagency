function showUsers(){
	$.getJSON($SCRIPT_ROOT + '/_get_users_list', {} ,function(data) {
	    vue_user_list.users = data.result;
	    console.log(data.result)
	});
}

function showServices(){
	$.getJSON($SCRIPT_ROOT + '/_get_services_list', {} ,function(data) {
	    vue_services_list.services = data.result;
	    console.log(data.result)
	});
}

function saveService(){
    price = vue_service.Price
    name = vue_service.Name
	/*$.getJSON($SCRIPT_ROOT + '/_save_service', {'price': price, 'name': name} ,function(data) {
	    if (data.result.ok){
	        vue_services_list.services.push(data.result.record)
	    }else{
	        alert(data.result.error)
	    }
	});*/

	$.ajax({
	  type: "POST",
	  url: "/_save_service",
	  data: {'price': price, 'name': name},
	  success: function (data) {
	    if (data.result.ok){
	        vue_services_list.services.push(data.result.record)
	    }else{
	        alert(data.result.error)
	    }
	  },
	  dataType: "json"
	});
}

function setServiceForm(service){
    console.o
    //console.log(service)
}