import { new_vue } from "../main";

var app = {
    components      : {},
    data            : {
        name        : 'django_vue',
        message     : 'Hello World !',
    },
    methods         : {},
    template        : {},
    mounted         : function (v_self) {
        console.log(v_self)
        console.log(Axios)
        console.log(JQuery)
        console.log($)
    }
}

var vm = new_vue(app)
