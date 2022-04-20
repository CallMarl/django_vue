/* Base file of all JS pages
*   - This file should be loaded for all script rendering vue app.
*   - This file should'nt be loaded in other file without vue app.
*/
import { from_json } from "./libs/html.js"

// Setup DJango global parametters
const HOST              = from_json('dja_host')
const URI               = from_json('dja_uri')

// Setup VueJS global parametters
const VUE_DELIMITERS    = ["[[", "]]"]
const VUE_EL            = "#app"

/*
*   Setup VueJS base App
*   This is the base app used by `new_vue()` to create the vm.
*   This base_app completion is usefull you want to load components global like
*   nav_bar or others.
*/
var base_app = {
    delimiters  : VUE_DELIMITERS,
    el          : VUE_EL,
    data        : {},
    components  : {},
    mounted     : function() {}
}

/*
*   This is hack function to generate a vue.
*   This function merge base app with the app you created in the page then
*   return the 2.0 vue.
*/
function new_vue(app) {
    return new Vue({
        delimiters  : base_app.delimiters,
        el          : base_app.el,
        components  : (base_app.data)
            ? Object.assign(
                base_app.components,
                (app.components) ? app.components : {}
            )
            : app.components,
        data        : (base_app.data)
            ? Object.assign(
                base_app.data,
                (app.data) ? app.data : {}
            )
            : app.data,
        methods     : (base_app.methods)
            ? Object.assign(
                base_app.methods,
                (app.methods) ? app.methods : {}
            )
            : app.methods,
        mounted     : function () {
            base_app.mounted()
            if (app.mounted)
                app.mounted(this)
        }
    })
}

export {
    HOST, URI, VUE_DELIMITERS, VUE_EL,
    new_vue, base_app
}
