<template>
  <div id="config" ref="childRef">
    <div class="tabs__content">
      <el-form v-if="activeTab === 'config'" ref="modelPropertiesRef" :model="modelProperties" label-position="left" label-width="210px" style="margin-left:50px;">
        <!-- MIN FIT CLIENTS -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="this.$t('overview.min_fit_clients')"
          prop="min_fit_clients"
          :rules="{ required: true, message: this.$t('overview.min_fit_clients') + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="modelProperties.min_fit_clients"
            style="width:80%"
          />
        </el-form-item>
        <!-- MIN AVAILABLE CLIENTS -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="this.$t('overview.min_available_clients')"
          prop="min_available_clients"
          :rules="{ required: true, message: this.$t('overview.min_available_clients') + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="modelProperties.min_available_clients"
            style="width:80%"
          />
        </el-form-item>
        <!-- EVAL METRICS -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="this.$t('overview.eval_metrics')"
          prop="eval_metrics"
          :rules="{ required: true, message: this.$t('overview.eval_metrics') + requiredText, trigger: 'blur' }"
        >
          <el-select
            v-model="modelProperties.eval_metrics"
            :label-width="label_widthColumn"
            placeholder="Type of evaluation"
          >
            <el-option
              v-for="item in this.eval"
              :key="item"
              :label="item"
              :value="item"
            />

          </el-select>
        </el-form-item>
        <!-- Stopping Flag -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="this.$t('overview.F1_metric_name') "
          prop="stopping_flag"
          :rules="{ required: true, message: this.$t('overview.F1_metric_name') + requiredText, trigger: 'blur' }"
        >
          <el-switch
            v-model="modelProperties.stopping_flag"
            active-color="#13ce66"
            :active-value="true"
            :inactive-value="false"
            @change="evalMetricsChanged"
          />
        </el-form-item>
        <!-- Stopping Target -->
        <el-form-item
          v-if="modelProperties.stopping_flag === true"
          :label-width="label_widthColumn"
          :label="this.$t('overview.F1_metric_value')"
          prop="stopping_target"
          :rules="{ required: true, message: this.$t('overview.F1_metric_value') + requiredText, trigger: 'blur' }"
          class="label_dialog"
        >
          <el-input-number
            v-model="modelProperties.stopping_target[modelProperties.eval_metrics]"
            :precision="3"
            :step="0.001"
            style="width:80%"
          />
        </el-form-item>

        <!-- TYPE OF STRATEGY -->
        <el-form-item
          :label-with="label_widthColumn"
          :label="this.$t('overview.type_of_strategy')"
          prop="strategy"
          :rules="{ required: true, message: this.$t('overview.type_of_strategy') + requiredText, trigger: 'blur' }"
          class="strategy_label"
        >
          <el-select
            v-model="modelProperties.strategy"
            :label-width="label_widthColumn"
            placeholder="Type of strategy"
            class="strategy_input"
          >
            <el-option v-for="items in strategy_list" :key="items.strategy_id" :label="items.strategy_name" :value="items.strategy_name" />
          </el-select>
        </el-form-item>
        <!-- NUMBER OF ROUNDS -->
        <el-form-item
          :label-width="label_widthColumn"
          :label="this.$t('overview.number_of_rounds')"
          prop="number_of_rounds"
          :rules="{ required: true, message: this.$t('overview.number_of_rounds') + requiredText, trigger: 'blur' }"
        >
          <el-input
            v-model="modelProperties.number_of_rounds"
            style="width:80%"
          />
        </el-form-item>

      </el-form>

    </div>
  </div>
</template>
<script>
import { configurationByModel, getStrategies } from '@/api/FL_API'
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
      modelProperties: {},
      strategy_list: [],
      label_widthColumn: '210px',
      requiredText: '',
      checkF1: false,
      eval: ['accuracy', 'F1']
    }
  },
  watch: {
    lang() {
      this.commonTranslation()
    },
    rowName: function(newValue, oldValue) {
      configurationByModel(newValue).then(res => {
        var len = res.message.data.length
        getStrategies().then(response => {
          this.strategy_list = response.message
        })
        if (len === 1) {
          var eval_met = res.message.data[0].eval_metrics
          this.modelProperties = res.message.data[0]
          if (typeof eval_met === 'object') {
            this.modelProperties['eval_metrics'] = eval_met[0] + ',' + eval_met[1]
          }
          this.$emit('modelProp', this.modelProperties)
        } else if (len === 0) {
          this.modelProperties = {}
          this.modelProperties.stopping_target = {}
          this.$emit('modelProp', false)
        } else {
          var evl_met = res.message.data[len - 1].eval_metrics
          this.modelProperties = res.message.data[len - 1]

          if (typeof evl_met === 'object') {
            this.modelProperties['eval_metrics'] = evl_met[0] + ',' + evl_met[1]
          }
          this.$emit('modelProp', this.modelProperties)
        }
      })
    }
  },
  created() {
    this.commonTranslation()
    configurationByModel(this.rowName).then(res => {
      var len = res.message.data.length
      getStrategies().then(response => {
        this.strategy_list = response.message
      })
      if (len === 1) {
        var eval_met = res.message.data[0].eval_metrics
        this.modelProperties = res.message.data[0]
        if (typeof eval_met === 'object') {
          this.modelProperties['eval_metrics'] = eval_met[0] + ',' + eval_met[1]
        }
        this.$emit('modelProp', this.modelProperties)
      } else if (len === 0) {
        this.modelProperties = {}
        this.modelProperties.stopping_target = {}
        this.$emit('modelProp', false)
      } else {
        var evl_met = res.message.data[len - 1].eval_metrics
        this.modelProperties = res.message.data[len - 1]
        if (typeof evl_met === 'object') {
          this.modelProperties['eval_metrics'] = evl_met[0] + ',' + evl_met[1]
        }
        this.$emit('modelProp', this.modelProperties)
      }
    })
  },
  methods: {
    commonTranslation() { this.requiredText = ' ' + this.$t('common.required') },
    evalMetricsChanged(newValue) {
      this.modelProperties.stopping_flag = newValue
      this.modelProperties.stopping_target = { [this.modelProperties.eval_metrics]: 0 }
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

</style>
