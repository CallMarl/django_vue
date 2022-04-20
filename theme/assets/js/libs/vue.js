/*
*   Fonction de récupération d'un composant racine en fonction de sa référence.
*   Si le composant n'existe pas, une exception est levé.
*   @ $component    => un composant
*   @ ref           => la référence du composant cherché
*/
export function v_root_ref($component, ref) {
    function _find(child) {
        if (child.$vnode.data.ref === ref) {
            return child
        }
        return undefined
    }

    var child   = $component.$root.$children.find(_find)
    if (child == undefined) {
        throw Error(
            "Component : " + $component.$options._componentTag +
            " need root with ref : " + ref
        )
    }
    return child
}

/*
*   Fonction de récupération d'un composant racine en fonction de sa référence.
*   Si le composant n'existe pas, une exception est levé.
*   @ $component    => un composant
*   @ tag           => le tag du composant racine
*/
export function v_root_tag($component, tag) {
    function _find(child) {
        if (child.$options._componentTag === tag) {
            return child
        }
        return undefined
    }

    var child = $component.$root.$children.find(_find)
    if (child == undefined) {
        throw Error(
            "Component : " + $component.$options._componentTag +
            " need root type : " + tag
        )
    }
    return child
}

/*
*   Fonction de récupération d'un composant enfant en fonction de sa
*   référence. Si le composant n'existe pas une exception est levé.
*   @ $component    => le composant parent
*   @ ref           => la référence du composant enfant
*/
export function v_child_ref($component, ref) {
    function _find(child) {
        if (child.$vnode.data.ref === ref) {
            return child
        }
        return undefined
    }

    var child   = $component.$children.find(_find)
    if (child == undefined) {
        throw Error(
            "Component : " + $component.$options._componentTag +
            " need child with ref : " + ref
        )
    }
    return child
}

/*
*   Fonction de récupération d'un composant enfant en fonction de son
*   tag. Si le composant n'existe pas une exception est levé.
*   @ $component    => le composant parent
*   @ tag           => le tag du composant enfant
*/
export function v_child_tag($component, tag) {
    function _find(child) {
        if (child.$options._componentTag === tag) {
            return child
        }
        return undefined
    }
    var child = $component.$children.find(_find)
    if (child == undefined) {
        throw Error(
            "Component : " + $component.$options._componentTag +
            " need child type : " + tag
        )
    }
    return child
}

export default {
    v_root_ref, v_root_tag, v_child_ref, v_child_tag
}
