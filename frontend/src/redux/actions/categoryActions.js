import * as actionTypes from "./actionTypes"
import {API_URL} from "../../api/baseUrl"

export function changeCategory(category) {
    return {type: actionTypes.CHANGE_CATEGORY, payload: category}
}

export function getCategoriesSuccess(categories) {
    return {type: actionTypes.GET_CATEGORIES_SUCCESS, payload: categories}
}

export function getCategories() {
    return function (dispatch) {
        let url = `${API_URL}/categories`
        return fetch(url)
            .then(response => response.json())
            .then(result => dispatch(getCategoriesSuccess(result)))
    }
}