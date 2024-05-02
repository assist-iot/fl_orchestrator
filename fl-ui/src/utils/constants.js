/*global config*/
/*eslint no-undef: "error"*/
// const apiHostName = config.FL_GUI_API_HOST_NAME || process.env.FL_GUI_API_HOST_NAME || (config.FL_GUI_API_HOST_NAME === '') 'localhost'
const apiHostName = (!config.FL_GUI_API_HOST_NAME.includes('VALUE')) ? config.FL_GUI_API_HOST_NAME : 'localhost'
const apiPort = (!config.FL_GUI_API_PORT.includes('VALUE')) ? config.FL_GUI_API_PORT : 3000
const apiWsPort = (!config.FL_GUI_API_WS_PORT.includes('VALUE')) ? config.FL_GUI_API_WS_PORT : 3010

export default {
  // base URL of our API
  baseURL_LOCAL: `http://${apiHostName}:${apiPort}`,
  baseWS_LOCAL: `ws://${apiHostName}:${apiWsPort}/websockets`,
  // methods petition API
  METHOD_GET: 'GET',
  METHOD_POST: 'POST',
  METHOD_PUT: 'PUT',
  METHOD_DELETE: 'DELETE',
  METHOD_PATCH: 'PATCH',
  // attributes for petitionS
  Application_Json: 'application/json',
  Fiware_Service: 'metadata',
  // Results petitions
  OK: 'OK',
  // Type of message for Modal Dialog
  SUCCESS_MESSAGE_TYPE: 'success',
  WARNING_MESSAGE_TYPE: 'warning',
  ERROR_MESSAGE_TYPE: 'error'
}
