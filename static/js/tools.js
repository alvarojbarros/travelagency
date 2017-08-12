function showUsers(){
	$.getJSON($SCRIPT_ROOT + '/_get_users_list', {} ,function(data) {
	    vue_user_list.users = data.result;
	    console.log(data.result)
	});
}
