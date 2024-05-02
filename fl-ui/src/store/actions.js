// Import helper lib module
import * as lib from './lib'
// Importing sample JSON data for the state
import data from '../../static/data3.json'

// Action to fetch resources and set in state through the mutation
export const fetchResources = ({ commit }) => {
  commit('setResources', data)
}

// Action to add title grid item in the state through the mutation
export const addTitleGridItem = ({ commit, state }, payload) => {
  const g = lib.guid()
  const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 2, 'i': g, 'type': 'title', 'title': 'Title', 'headings': { 'h1': true, 'h2': false, 'h3': false }}
  commit('setNewGridItem', k)
}

// Action to add content grid item in the state through the mutation
export const addContentGridItem = ({ commit, state }, payload) => {
  const g = lib.guid()
  const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 3, 'i': g, 'type': 'content', 'content': 'Text goes here' }
  commit('setNewGridItem', k)
}

// Action to add image grid item in the state through the mutation
export const addImageGridItem = ({ commit, state }, payload) => {
  const g = lib.guid()
  // const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'image', 'location': 'http://via.placeholder.com/600x350' }
  const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'image', 'location': '' }
  commit('setNewGridItem', k)
}

export const addIframeWidgetItem = ({ commit, state }, payload) => {
  const g = lib.guid()
  // const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'image', 'location': 'http://via.placeholder.com/600x350' }
  const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'iframe', 'location': '' }
  commit('setNewGridItem', k)
}

// Action to add a visualization grid item in the state through the mutation
export const addVisualizationGridItem = ({ commit, state }, payload) => {
  const g = lib.guid()
  // const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'image', 'location': 'http://via.placeholder.com/600x350' }
  const k = { 'x': 0, 'y': 0, 'w': 4, 'h': 4, 'i': g, 'type': 'image', 'location': '' }
  commit('setNewGridItem', k)
}

// Action to remove item from the state through the mutation
export const removeItem = ({ commit, state }, payload) => {
  commit('removeItem', payload)
}

// Action to save updated headings through the mutation
export const saveHeadings = ({ commit, state }, payload) => {
  const currentItem = state.resources[payload.itemIndex]
  currentItem.headings.h1 = payload.values[0]
  currentItem.headings.h2 = payload.values[1]
  currentItem.headings.h3 = payload.values[2]
  commit('setUpdatedItem', { itemIndex: payload.itemIndex, item: currentItem })
}

// Action to save item through the mutation
export const saveItem = ({ commit, state }, payload) => {
  commit('setUpdatedItem', payload)
}
