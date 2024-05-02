<template>
  <div id="parametrization" ref="parametrizationRef">
    <div class="tabs__content">
      <div v-if="activeTab === 'more'" class="flex-container">
        <p class="head">It is recommended to be modified by an expert</p>
        <el-switch
          v-model="checkParam"
          class="switch_head"
          active-color="#13ce66"
          active-value="true"
          inactive-value="false"
        />
      </div>
      <el-form v-if="activeTab === 'more'" ref="paramProperties" :model="paramProperties" :disabled="disabled_form" label-position="left" label-width="190px" style="margin-left:50px;">
        <!-- Client Type Id -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Client Type Id'"
          prop="client_type_id"
          :rules="{ required: true, message: 'Client Type Id' + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="paramProperties.client_type_id"
            style="width:80%"
          />
        </el-form-item>
        <!-- 'Server Address' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Server Address'"
          prop="server_address"
          :rules="{ required: true, message: 'Server Address' + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="paramProperties.server_address"
            style="width:80%"
          />
        </el-form-item>
        <!-- 'Evaluation Function' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Evaluation Function'"
          prop="eval_func"
          :rules="{ required: true, message: 'Evaluation Function' + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="paramProperties.eval_func"
            style="width:80%"
          />
        </el-form-item>
        <!-- 'Number Of Classes' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Number Of Classes'"
          prop="num_classes"
          :rules="{ required: true, message: 'Number Of Classes' + requiredText, trigger: 'blur' }"
          class="label_dialog"
        >
          <el-input
            v-model="paramProperties.num_classes"
            style="width:80%"
          />
        </el-form-item>
        <!-- 'Shape' -->
        <el-form-item
          :label-with="label_widthColumn"
          :label="'Shape'"
          prop="shape"
          :rules="{ required: true, message: 'Shape' + requiredText, trigger: 'blur' }"
        >
          <div class="flex-container">
            <el-input-number v-model="paramProperties.shape[0]" style="width:26.6%" />
            <el-input-number v-model="paramProperties.shape[1]" style="width:26.8%" />
            <el-input-number v-model="paramProperties.shape[2]" style="width:26.6%" />
          </div>
        </el-form-item>
        <!-- 'Client Configuration' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Client Configuration'"
          prop="config"
          :rules="{ required: true, message: 'Client Configuration' + requiredText, trigger: 'blur' }"
        >
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Configuration Id'"
            prop="config_id"
            :rules="{ required: true, message: 'Configuration Id' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.config[0].config_id" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Batch Size'"
            prop="batch_size"
            :rules="{ required: true, message: 'Batch Size' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.config[0].batch_size" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Steps Per Epoch'"
            prop="steps_per_epoch"
            :rules="{ required: true, message: 'Steps Per Epochs' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.config[0].steps_per_epoch" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Epochs'"
            prop="epochs"
            :rules="{ required: true, message: 'Epochs' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.config[0].epochs" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Learning Rate'"
            prop="learning_rate"
            :rules="{ required: true, message: 'Learning Rate' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.config[0].learning_rate" style="width:76.65%" />
          </el-form-item>
        </el-form-item>
        <!-- 'Optimizer Configuration' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Optimizer Configuration'"
          prop="optimizer_config"
          :rules="{ required: true, message: 'Optimizer Configuration' + requiredText, trigger: 'blur' }"
        >
          <!-- 'Keras Optimizer Configuration' -->
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Optimizer'"
            prop="optimizer"
            :rules="{ required: true, message: 'Optimizer' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.optimizer_config.optimizer" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="!changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Learning Rate'"
            prop="learning_rate"
            :rules="{ required: true, message: 'Learning Rate' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.optimizer_config.learning_rate" :precision="3" :step="0.001" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="!changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Amsgrad'"
            prop="amsgrad"
            :rules="{ required: true, message: 'Amsgrad' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.optimizer_config.amsgrad" style="width:76.65%" />
          </el-form-item>

          <!-- 'TwoTronics Optimizer Configuration' -->
          <el-form-item
            v-if="changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'LR'"
            prop="LR"
            :rules="{ required: true, message: 'LR' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.optimizer_config.lr" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Momentum'"
            prop="momentum"
            :rules="{ required: true, message: 'Momentum' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.optimizer_config.momentum" :precision="3" :step="0.001" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Weight Decay'"
            prop="weight_decay"
            :rules="{ required: true, message: 'Weight Decay' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.optimizer_config.weight_decay" style="width:76.65%" />
          </el-form-item>
        </el-form-item>
        <!-- 'Scheduler Configuration' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Scheduler Configuration'"
          prop="scheduler_config"
          :rules="{ required: true, message: 'Scheduler Configuration' + requiredText, trigger: 'blur' }"
        >
          <!-- 'Keras Scheduler Configuration' -->
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Scheduler'"
            prop="scheduler"
            :rules="{ required: true, message: 'Scheduler' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.scheduler_config.scheduler" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="!changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Factor'"
            prop="factor"
            :rules="{ required: true, message: 'Factor' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.scheduler_config.factor" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="!changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Min Delta'"
            prop="min_delta"
            :rules="{ required: true, message: 'Min Delta' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.scheduler_config.min_delta" style="width:76.65%" />
          </el-form-item>

          <!-- 'TwoTronics Scheduler Configuration' -->
          <el-form-item
            v-if="changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Step Size'"
            prop="step_size"
            :rules="{ required: true, message: 'Step Size' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.scheduler_config.step_size" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            v-if="changeConfig"
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Gamma'"
            prop="gamma"
            :rules="{ required: true, message: 'Gamma' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.scheduler_config.gamma" style="width:76.65%" />
          </el-form-item>
        </el-form-item>
        <!-- 'Twotronic Warmup Configuration' -->
        <el-form-item
          v-if="changeConfig"
          :label-width="label_widthColumn"
          :label="'Warmup Configuration'"
          prop="warmup_config"
          :rules="{ required: true, message: 'Warmup Configuration' + requiredText, trigger: 'blur' }"
        >
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Scheduler'"
            prop="scheduler"
            :rules="{ required: true, message: 'Scheduler' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.warmup_config.scheduler" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Warmup Iters'"
            prop="warmup_iters"
            :rules="{ required: true, message: 'Warmup Iters' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.warmup_config.warmup_iters" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Warmup Epochs'"
            prop="warmup_epochs"
            :rules="{ required: true, message: 'Warmpup Epochs' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.warmup_config.warmup_epochs" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            class="obj_param"
            :label-width="label_widthColumn"
            :label="'Warmup Factor'"
            prop="warmup_factor"
            :rules="{ required: true, message: 'Warmpup Factor' + requiredText, trigger: 'blur' }"
          >
            <el-input-number v-model="paramProperties.warmup_config.warmup_factor" style="width:76.65%" />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="'Scheduler Configuration'"
            prop="scheduler_conf"
            :rules="{ required: true, message: 'Scheduler Configuration' + requiredText, trigger: 'blur' }"
          >
            <el-input v-model="paramProperties.warmup_config.scheduler_conf.scheduler" style="width:76.65%" />
          </el-form-item>

        </el-form-item>

        <!-- 'Adapt Configuration' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Adapt Configuration'"
          prop="adapt_config"
          :rules="{ required: true, message: 'Adapt Configuration' + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="paramProperties.adapt_config"
            style="width:80%"
          />
        </el-form-item>
        <!-- 'Min Evaluate Clients' -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="'Min Evaluate Clients'"
          prop="min_eval_clients"
          :rules="{ required: true, message: 'Min Evaluate Clients' + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="paramProperties.min_eval_clients"
            style="width:80%"
          />
        </el-form-item>
      </el-form>

    </div>
  </div>
</template>
<script>
import { getPersistConfiguration } from '@/api/FL_API'
export default {
  props: {
    activeTab: {
      type: String,
      default: ''
    },
    rowName: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      paramProperties: {},
      strategy_list: ['fedavg', 'qfedavg', 'fault-tolerant-fedavg'],
      label_widthColumn: '190px',
      requiredText: '',
      checkParam: false,
      disabled_form: true,
      changeConfig: false
    }
  },
  watch: {
    lang() {
      this.commonTranslation()
    },
    checkParam(newVal) {
      var bool = this.StringToBoolean(newVal)
      if (bool === true) {
        this.disabled_form = false
      } else if (bool === false) {
        this.disabled_form = true
      }
    },
    rowName: function(newValue, oldValue) {
      getPersistConfiguration().then(response => {
        var data = response.message[0]
        if (newValue === 'keras_test') {
          delete data['eval_metrics_twotronics']
          delete data['optimizer_config_twotronics']
          delete data['scheduler_config_twotronics']
          delete data['warmup_config']
        } else if (newValue === 'twotronics') {
          data['optimizer_config'] = data['optimizer_config_twotronics']
          data['scheduler_config'] = data['scheduler_config_twotronics']
          delete data['eval_metrics_twotronics']
          delete data['optimizer_config_twotronics']
          delete data['scheduler_config_twotronics']
          this.changeConfig = true
        }
        this.paramProperties = data
      })
    }
  },
  created() {
    this.commonTranslation()
    getPersistConfiguration().then(response => {
      var data = response.message[0]
      if (this.rowName === 'keras_test') {
        delete data['eval_metrics_twotronics']
        delete data['optimizer_config_twotronics']
        delete data['scheduler_config_twotronics']
        delete data['warmup_config']
      } else if (this.rowName === 'twotronics') {
        data['optimizer_config'] = data['optimizer_config_twotronics']
        data['scheduler_config'] = data['scheduler_config_twotronics']
        delete data['eval_metrics_twotronics']
        delete data['optimizer_config_twotronics']
        delete data['scheduler_config_twotronics']
        this.changeConfig = true
      }
      this.paramProperties = data
    })
  },
  methods: {
    commonTranslation() { this.requiredText = ' ' + this.$t('common.required') },
    StringToBoolean(stringValue) {
      switch (stringValue) {
        case 'true':return true
        case 'false':return false
      }
    }
  }
}
</script>
    <style scoped>
     .tabs__content {
         background: #fff;
         /* padding: 1rem; */
         border-radius: 0 0.5rem 0.5rem 0.5rem;
    }
    .flex-container{
        display: flex;
        flex-direction: row;
    }
    .obj_param{
        padding-bottom: 20px;
    }
    .head{
        color: red;
        font-style: italic;
        align-items: start;
        padding-right: 10px;
    }
    .switch_head{
        padding-top: 25px !important;
    }
    </style>
