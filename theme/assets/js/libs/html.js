/*
*   Fonction de récupération d'un script JSON dans l'HTML en fonction
*   de son id
*/
export function from_json(html_id) {
    return JSON.parse(document.getElementById(html_id).textContent)
}

export default { from_json }
