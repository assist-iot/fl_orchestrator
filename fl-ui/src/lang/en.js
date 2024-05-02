export default {
  route: {
    home: 'Home',
    overview: 'New FL Training',
    models: 'Available FL Models'

  },
  navbar: {
    dashboard: 'Dashboard',
    github: 'Github',
    logOut: 'Log Out',
    profile: 'Profile',
    theme: 'Theme',
    size: 'Global Size'
  },
  login: {
    title: 'ASSIST-IoT',
    logIn: 'Login',
    username: 'Username',
    password: 'Password',
    any: 'any',
    thirdparty: 'Or connect with',
    thirdpartyTips: 'Can not be simulated on local, so please combine you own business simulation! ! !'
  },
  permission: {
    addRole: 'New Role',
    editPermission: 'Edit',
    roles: 'Your roles',
    switchRoles: 'Switch roles',
    tips: 'In some cases, using v-permission will have no effect. For example: Element-UI  el-tab or el-table-column and other scenes that dynamically render dom. You can only do this with v-if.',
    delete: 'Delete',
    confirm: 'Confirm',
    cancel: 'Cancel'
  },
  errorLog: {
    tips: 'Please click the bug icon in the upper right corner',
    description: 'Now the management system are basically the form of the spa, it enhances the user experience, but it also increases the possibility of page problems, a small negligence may lead to the entire page deadlock. Fortunately Vue provides a way to catch handling exceptions, where you can handle errors or report exceptions.',
    documentation: 'Document introduction'
  },
  tagsView: {
    refresh: 'Refresh',
    close: 'Close',
    closeOthers: 'Close Others',
    closeAll: 'Close All'
  },
  settings: {
    title: 'Page style setting',
    theme: 'Theme Color',
    tagsView: 'Open Tags-View',
    fixedHeader: 'Fixed Header',
    sidebarLogo: 'Sidebar Logo'
  },
  'common': {
    start: 'Start',
    'required': 'required',
    'close': 'Close',
    'delete': 'Delete',
    'accept': 'Accept',
    'cancel': 'Cancel',
    'success': 'Success',
    'error': 'Error',
    'warning': 'Warning',
    closeDialog: 'Are you sure to close this dialog?',
    ok: 'Ok'
  },
  'models': {
    'search': 'Search'
  },
  overview: {
    tableColumnModelName: 'Algorithm Name',
    tableColumnModelVersion: 'Algorithm version',
    models: 'Algorithms',
    tableColumnActions: 'Actions',
    viewModel: 'View Configuration',
    TrainModel: 'Train Algorithm',
    trainModelDialogTitle: 'Train Algorithm: ',
    trainModelDialogQuestion: 'Are you sure you want to train this Algorithm?',
    editModel: 'Edit Configuration',
    editModelDialogTitle: 'Edit Algorithm',
    number_of_rounds: 'Number of rounds:',
    min_fit_clients: 'Min fit clients:',
    min_available_clients: 'Min available clients:',
    eval_metrics: 'Evaluation metrics:',
    eval_metrics_value: 'Value evaluation metrics:',
    type_of_strategy: 'Type of Strategy',
    encryption: 'Encryption Type',
    configurationStored: 'Configuration stored',
    fieldsRequired: 'All fields are required',
    ecryptionFieldsRequired: 'Dp-Adaptive fields are required',
    FLTrainingstarted: 'FL Training has started',
    classification_base2_description: 'Machine Learning models for binary classification problems predict a binary outcome (one of two possible classes).',
    classification_base_description: 'Machine Learning models for classification problems predict a categorical outcome (one of several possible classes).',
    regression_base_description: 'Machine Learning models for regression problems predict a numeric value.',
    F1: 'F1',
    F1_metric_name: 'Stopping Flag',
    F1_metric_value: 'Stopping Target',
    round: 'Round',
    successfully: ' has successfully finished',
    finished: 'The FL training has been finished',
    findModel: 'you can find',
    modelText: 'model',
    hereDownload: 'here',
    trainStart: 'Training has started',
    errorTrain: 'Error in the training process',
    stopEnoughLo: 'The FL training has been stopped because not enough available local operations.',
    stopMetricTarget: 'Evaluation metric requirement achieved.',
    epoch: 'Epoch'
  },
  encryption_table: {
    num_sampled_clients: 'Number sampled clients',
    init_clip_norm: 'Init clip norm',
    noise_multiplier: 'Noise multiplier',
    server_side_noising: 'Server side noising',
    clip_count_stddev: 'Standard clip count',
    clip_norm_target_quantile: 'Clip norm target quantile',
    clip_norm_lr: 'Clip norm lr'

  },
  availableModel: {
    tableColumnModelName: 'Model Name',
    tableColumnModelDescription: 'Description Model',
    tableInformationColumnModelDownload: 'Download Model',
    tableInformationColumnModelDate: 'Date',
    tableInformationColumnModelDatasetSize: 'Dataset Size',
    tableInformationColumnModelFlLocalOperations: 'FL Local Operations',
    tableInformationColumnModelFlTrainingRounds: 'FL Training Rounds',
    tableInformationColumnModelMse: 'F1',
    models: 'Models',
    buttonDownload: 'Download',
    notAvailable: 'Not Available',
    eval_metrics: 'Evaluation metrics'
  },
  home: {
    title: 'What do you want to do?',
    newTraining: 'Start new training',
    viewAvailableModels: 'View available models'
  },
  shell: {
    header: 'Training Information',
    subHeader: 'Here you can see the information of model training'
  }
}
