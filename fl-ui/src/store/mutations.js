import Vue from 'vue'

// Mutation to set resources in state
export const setResources = (state, resources) => {
  state.resources = resources || {}
}

// Mutation too new grid item in resources
export const setNewGridItem = (state, payload) => {
  state.resources.push(payload)
}

// Mutation to remove item from the resources
export const removeItem = (state, payload) => {
  if (payload.key > -1) {
    state.resources.splice(payload.key, 1)
  }
}

// Mutation to update item in resources
export const setUpdatedItem = (state, response) => {
  state.resources[response.itemIndex] = response.item
}

export const SOCKET_ONOPEN = (state, event) => {
  console.log('SOCKET_ONOPEN')
  Vue.prototype.$socket = event.currentTarget
  state.socket.isConnected = true
}

export const SOCKET_ONCLOSE = (state, event) => {
  console.log('SOCKET_ONCLOSE')
  state.socket.isConnected = false
}

export const SOCKET_ONERROR = (state, event) => {
  console.log('SOCKET_ONERROR')
  console.error(state, event)
}

export const SOCKET_ONMESSAGE = (state, message) => {
  console.log('SOCKET_ONMESSAGE')
  // property message contiene toda la informacion del socket
  state.socket.message = message.data
  window.localStorage.setItem('isOk', '1')
}

// mutations for reconnect methods
export const SOCKET_RECONNECT = (state, count) => {
  console.log('SOCKET_RECONNECT')
}

export const SOCKET_RECONNECT_ERROR = (state) => {
  console.log('SOCKET_RECONNECT_ERROR')
  state.socket.reconnectError = true
}
