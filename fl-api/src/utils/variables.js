export default {
	baseURL_FLRepository: process.env.FL_REPOSITORY_URL || 'http://localhost:30580',
	baseURL_FLOrchestrator: process.env.FL_ORCHESTRATOR_URL || 'http://localhost:5000',
	// methods petition API
	METHOD_GET: 'GET',
	METHOD_POST: 'POST',
	METHOD_PUT: 'PUT',
	METHOD_DELETE: 'DELETE',
	// attributes for petitions
	Application_Json: 'application/json',
	Application_Octet_Stream: 'application/octet-stream',

	// HTTP STATUS CODE
	INTERNAL_SERVER_ERROR: 500,
	CORRECT_REQUEST: 200,
	NOT_FOUND: 404
};