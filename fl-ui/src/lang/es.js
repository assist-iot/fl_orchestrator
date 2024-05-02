export default {
  'route': {
    'home': 'Inicio',
    'overview': 'Nuevo Entrenamiento FL',
    'models': 'Modelos FL disponibles'

  },
  'navbar': {
    'dashboard': 'Tablero',
    'github': 'Github',
    'logOut': 'Cerrar sesión',
    'profile': 'Perfil',
    'theme': 'Tema',
    'size': 'Tamaño global'
  },
  'login': {
    'title': 'ASSIST-IoT',
    'logIn': 'Iniciar sesión',
    'username': 'Nombre de usuario',
    'password': 'Contraseña',
    'any': 'alguna',
    'thirdparty': 'O conéctate con',
    'thirdpartyTips': 'No se puede simular en local, así que combina tu propia simulación de negocios. ! !'
  },
  'permission': {
    'addRole': 'Nuevo rol',
    'editPermission': 'Editar',
    'roles': 'Tus roles',
    'switchRoles': 'Cambiar roles',
    'tips': 'En algunos casos, el uso de v-permission no tendrá ningún efecto. Por ejemplo: Element-UI el-tab o el-table-column y otras escenas que representan dinámicamente dom. Solo puede hacer esto con v-if.',
    'delete': 'Eliminar',
    'confirm': 'Confirmar',
    'cancel': 'Cancelar'
  },
  'errorLog': {
    'tips': 'Haga clic en el ícono de error en la esquina superior derecha',
    'description': 'Ahora, el sistema de gestión es básicamente la forma del spa, mejora la experiencia del usuario, pero también aumenta la posibilidad de problemas de página, una pequeña negligencia puede conducir al bloqueo total de la página. Afortunadamente, Vue proporciona una forma de detectar excepciones de manejo, donde puede manejar errores o informar excepciones.',
    'documentation': 'Introducción de documentos'
  },
  'tagsView': {
    'refresh': 'Actualizar',
    'close': 'Cerca',
    'closeOthers': 'Cerrar otros',
    'closeAll': 'Cierra todo'
  },
  'settings': {
    'title': 'Configuración de estilo de página',
    'theme': 'Color del tema',
    'tagsView': 'Abrir etiquetas-Vista',
    'fixedHeader': 'Encabezado fijo',
    'sidebarLogo': 'Logo de barra lateral'
  },
  'common': {
    start: 'Iniciar',
    'required': 'requerido',
    'close': 'Cerrar',
    'delete': 'Borrar',
    'accept': 'Aceptar',
    'cancel': 'Cancelar',
    'success': 'Éxito',
    'error': 'Error',
    warning: 'Warning',
    closeDialog: '¿Esta seguro de cerrar el cuadro de dialogo?',
    ok: 'Ok'
  },
  'models': {
    'search': 'Buscar'
  },
  overview: {
    tableColumnModelName: 'Nombre del algoritmo',
    tableColumnModelVersion: 'Versión algoritmo',
    models: 'Algoritmos',
    tableColumnActions: 'Acciones',
    viewModel: 'Ver configuración',
    TrainModel: 'Entrenar algoritmo',
    trainModelDialogTitle: 'Entrenar algoritmo: ',
    trainModelDialogQuestion: '¿Esta seguro que quiere entrenar este algoritmo?',
    editModel: 'Editar configuración',
    editModelDialogTitle: 'Editar algoritmo',
    number_of_rounds: 'Numero de rondas:',
    min_fit_clients: 'Ajuste mínimo de clientes:',
    min_available_clients: 'Minimo clientes disponible:',
    eval_metrics: 'Métricas de evaluación:',
    eval_metrics_value: 'Valor métricas de evaluación:',
    type_of_strategy: 'Tipo de estrategia',
    encryption: 'Tipo de cifrado',
    configurationStored: 'Configuración guardada',
    fieldsRequired: 'Todos los campos son obligatorios',
    ecryptionFieldsRequired: 'Los campos del Dp-Adaptive son obligatorios',
    FLTrainingstarted: 'FL Entrenamiento ha empezado',
    classification_base2_description: 'Los modelos de aprendizaje automático para problemas de clasificación binaria predicen un resultado binario (una de dos clases posibles).',
    classification_base_description: 'Los modelos de aprendizaje automático para problemas de clasificación predicen un resultado categórico (una de varias clases posibles).',
    regression_base_description: 'Los modelos de aprendizaje automático para problemas de regresión predicen un valor numérico.',
    F1: 'F1',
    F1_metric_name: 'Criterio de Evaluación',
    F1_metric_value: 'Objetivo',
    round: 'La ronda',
    successfully: ' ha sido finalizada',
    finished: 'El entrenamiento ha finalizado',
    findModel: 'puedes encontrar',
    modelText: 'modelo',
    hereDownload: 'aquí',
    trainStart: 'El entrenamiento ha empezado',
    errorTrain: 'Error en el proceso de entrenamiento',
    stopEnoughLo: 'El entrenamiento se ha detenido porque no hay suficientes clientes disponibles.',
    stopMetricTarget: 'Requisito de métrica de evaluación alcanzado',
    epoch: 'Época'
  },
  encryption_table: {
    num_sampled_clients: 'Número de clientes muestreados',
    init_clip_norm: 'Norma de clip de inicio',
    noise_multiplier: 'Multiplicador de ruido',
    server_side_noising: 'Ruido del lado del servidor',
    clip_count_stddev: 'Recuento de clips estándar',
    clip_norm_target_quantile: 'Cuantil objetivo de la norma de recorte',
    clip_norm_lr: 'Norma de clip lr'

  },
  availableModel: {
    tableColumnModelName: 'Nombre del modelo',
    tableColumnModelDescription: 'Descripción del modelo',
    tableInformationColumnModelDownload: 'Descargar modelo',
    tableInformationColumnModelDate: 'Fecha de creación',
    tableInformationColumnModelDatasetSize: 'Tamaño del conjunto de datos',
    tableInformationColumnModelFlLocalOperations: 'Operaciones locales FL',
    tableInformationColumnModelFlTrainingRounds: 'Rondas de entrenamiento FL',
    tableInformationColumnModelMse: 'F1',
    models: 'Modelos',
    buttonDownload: 'Descargar',
    notAvailable: 'No Disponible',
    eval_metrics: 'Métricas de Evaluación'
  },
  home: {
    title: '¿Que es lo que desea hacer?',
    newTraining: 'Empezar un nuevo entrenamiento',
    viewAvailableModels: 'Ver modelos disponibles'
  },
  shell: {
    header: 'Información de entrenamiento',
    subHeader: 'Aquí puedes ver la información de la formación de modelos'
  }
}
