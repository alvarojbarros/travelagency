Vue.config.devtools = true;

var vue_services_list = new Vue({
  el: '#services_list',
  data: {
    current_service_index: -1,
    services: [],
  },

  methods:{
      filterItems: function(id) {
        return this.services.filter(function(item) {
          return item.id == id;
        })
      },
    }

})