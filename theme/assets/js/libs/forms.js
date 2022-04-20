/*
*   Fonction de récupération des information de formulaire.
*   @ form      => élément HTML de formulaire
*
*   @ return    => un objet FormData
*/
export function form_data(form) {
    var data = new FormData();
    var i;

    for (i = 0; i < form.length - 1; i++) {
        data.append(form[i].name, form[i].value)
    }
    return data
}

/*
*   Calcul de la longueur d'un formulaire
*   @ form_data => un oject FormData
*
*   @ return    => un nombre
*/
export function form_data_length(form_data) {
    var i = 0;

    for (var value of form_data.values()) {
       i++;
    }
    return i
}

/*
*   Cette fonction est un hack pour le gestionnaire Multiform utilisé en back.
*   Si plusieurs structure de formulaire `back` sont fusionné dans un même
*   formulaire en front. cette fonction divise les différents formulaire grace
*   au champs `name=multifom` de chacun des formulaire et les ajoute dans des
*   objets FormData.
*   @ form      => élément HTML de formulaire
*
*   @ return    => un tableau d'objet FormData
*/
export function multiform_data(form) {
    var forms = [];
    var data = new FormData();
    var csrftoken;
    var i;

    for (i = 0; i < form.length - 1; i++) {
        if (form[i].name == 'csrfmiddlewaretoken')
            csrftoken = form[i].value
        else if (form[i].name) {
            if (form[i].name == 'multiform') {
                if (form_data_length(data))
                    forms.push(data)
                data = new FormData
            }
            if (form[i].type == 'checkbox')
                data.append(form[i].name, form[i].checked)
            else
                data.append(form[i].name, form[i].value)
        }
    }
    if (form_data_length(data))
        forms.push(data)

    for (form in forms){
        forms[form].append('csrfmiddlewaretoken', csrftoken)
    }
    return forms
}
