function showUsers(){
	$.getJSON($SCRIPT_ROOT + '/_get_users_list', {} ,function(data) {
	    vue_user_list.users = data.result;
	});
}

function showServices(){
	$.getJSON($SCRIPT_ROOT + '/_get_services_list', {} ,function(data) {
	    vue_services_list.services = data.result;
	});
}

function saveService(){
    price = vue_service.Price;
    name = vue_service.Name;
    id = vue_service.id;
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
	  data: {'price': price, 'name': name, 'id': id},
	  success: function (data) {
	    console.log(data)
	    if (data.result.ok){
	        console.log(vue_services_list.current_service_index)
	        if (vue_services_list.current_service_index>=0){
	            index = vue_services_list.current_service_index;
	            Vue.set(vue_services_list.services, index, data.result.record)
	        }else{
    	        vue_services_list.services.push(data.result.record);
	        }
	    }else{
	        alert(data.result.error)
	    }
	  },
	  dataType: "json"
	});
}

function setServiceForm(service_id,index){
    //service = vue_services_list.filterItems(service_id)[0];
    //vue_service.Name = service.Name
    //vue_service.Price = service.Price
    //vue_service.id = service.id

    vue_services_list.current_service_index = index;
	$.ajax({
	  type: "POST",
	  url: "/_get_service",
	  data: {'id': service_id},
	  success: function (data) {
	    if (data.result.ok){
            vue_service.Name = data.result.record.Name
            vue_service.Price = data.result.record.Price
            vue_service.id = data.result.record.id
	    }else{
	        alert(data.result.error)
	    }
	  },
	  dataType: "json"
	});

}