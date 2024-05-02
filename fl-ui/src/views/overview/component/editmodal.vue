<template>
  <div id="edit">
    <div class="tabs">
      <div class="tabs__nav">
        <div
          class="tabs__nav_tab"
          :class="{'tabs__nav_tab--active': activeTab === 'config'}"
          @click="selectOption('config')"
        >FL Configuration</div>
        <div
          class="tabs__nav_tab"
          :class="{'tabs__nav_tab--active': activeTab === 'more'}"
          @click="selectOption('more')"
        >Model Parametrization</div>
        <div
          class="tabs__nav_tab"
          :class="{'tabs__nav_tab--active': activeTab === 'encrypt'}"
          @click="selectOption('encrypt')"
        >Encryption</div>

      </div>
      <div class="tabs__content">
        <Configuration ref="configurationRef" :active-tab="activeTab" :row-name="rowName" class="comps" @modelProp="sendEncrypt" />
        <More ref="parametrizationRef" :active-tab="activeTab" :row-name="rowName" />
        <Encryption ref="encryptionRef" :active-tab="activeTab" :model-encrypt="modelEncrypt" />
        <div slot="footer" class="dialog-footer">
          <el-button type="danger" @click="closeConfiguration">
            {{ $t("common.cancel") }}
          </el-button>
          <el-button type="success" @click="sendConfiguration">
            {{ $t("common.accept") }}
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Configuration from './configuration/configuration.vue'
import Encryption from './configuration/encryption.vue'
import More from './configuration/more.vue'
import { modelConfiguration } from '@/api/FL_API'
export default {
  components: {
    Configuration,
    Encryption,
    More
  },
  props: {
    rowSelected: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      modelProperties: {},
      modelEncrypt: {},
      label_widthColumn: '190px',
      requiredText: '',
      activeTab: 'config',
      rowName: ''
    }
  },
  watch: {
    lang() {
      this.commonTranslation()
    },
    rowSelected: function(newValue, oldValue) {
      this.rowName = newValue.model_name
    }
  },
  created() {
    this.rowName = this.rowSelected.model_name
    this.commonTranslation()
  },
  methods: {
    sendEncrypt(data) {
      if (data !== false) {
        this.$emit('modelConfig', data)
        var encr = data['privacy-mechanisms']
        if (Object.keys(encr).length === 0) {
          this.modelEncrypt = {}
        } else {
          if (encr.hasOwnProperty('homomorphic')) {
            this.modelEncrypt = { [Object.keys(encr)]: encr['homomorphic'] }
          } else if (encr.hasOwnProperty('dp-adaptive')) {
            this.modelEncrypt = { [Object.keys(encr)]: encr['dp-adaptive'] }
          }
        }
      }
    },
    commonTranslation() { this.requiredText = ' ' + this.$t('common.required') },
    selectOption(option) {
      this.$nextTick(() => {
        if (option === 'config') {
          const configurationConf = this.$refs.configurationRef
          const modelProperties = JSON.parse(JSON.stringify(configurationConf.modelProperties))
          this.modelProperties = modelProperties
          /* this.modelProperties = this.$refs.Configuration.$refs.modelProperties */
        }
        this.activeTab = option
      })
    },
    sendConfiguration() {
      var sendConfi = {}
      const configurationConf = this.$refs.configurationRef
      var modelProperties = JSON.parse(JSON.stringify(configurationConf.modelProperties))
      const encryptionConf = this.$refs.encryptionRef
      var encrypt_switch = encryptionConf.checkEncryption
      const encryptionProperties = JSON.parse(JSON.stringify(encryptionConf.encryptionProperties))
      var encr_prop_copy = { ...encryptionProperties }
      const parametrizationConf = this.$refs.parametrizationRef
      const paramProperties = JSON.parse(JSON.stringify(parametrizationConf.paramProperties))
      if(!modelProperties.hasOwnProperty("stopping_flag")){modelProperties["stopping_flag"] = false}
      if (modelProperties.eval_metrics && modelProperties.eval_metrics.includes(',')) {
        modelProperties['eval_metrics'] = modelProperties.eval_metrics.split(',')
      }
      if ('encryption' in encr_prop_copy && encr_prop_copy.encryption === 'dp-adaptive') {
        delete encr_prop_copy.encryption
      }
      if (typeof encrypt_switch === 'string') {
        encrypt_switch = this.$refs.encryptionRef.StringToBoolean(encrypt_switch)
      }
      if (this.verifyObjects(modelProperties, encr_prop_copy, encrypt_switch, encryptionProperties.encryption)) {
        if (encrypt_switch) {
          if (encryptionProperties.encryption === 'homomorphic') {
            var hom_obj = { [encryptionProperties.encryption.toLowerCase()]: {}}
            sendConfi = modelProperties
            sendConfi['privacy-mechanisms'] = hom_obj
            sendConfi['model_name'] = this.rowSelected.model_name
            sendConfi['model_id'] = this.rowSelected.model_id
            sendConfi['status'] = this.rowSelected.status
            sendConfi['model_version'] = this.rowSelected.model_version
            sendConfi['checked'] = this.rowSelected.checked
            sendConfi['meta'] = this.rowSelected.meta
            sendConfi['eval_metrics_value'] = 1
            for (var it in paramProperties) {
              sendConfi[it] = paramProperties[it]
            }
            if (sendConfi['stopping_flag'] === false) {
              sendConfi['stopping_target'] = {}
            } else if (sendConfi['stopping_flag'] === true) {
              sendConfi['stopping_target'] = { [sendConfi['eval_metrics']]: parseFloat(sendConfi['stopping_target']) }
            }
            modelConfiguration(sendConfi).then(response => {
              this.$emit('close', response)
            })
          } else if (encryptionProperties.encryption === 'dp-adaptive') {
            var dp_obj = { [encryptionProperties.encryption.toLowerCase()]: encr_prop_copy }
            sendConfi = modelProperties
            sendConfi['privacy-mechanisms'] = dp_obj
            sendConfi['model_name'] = this.rowSelected.model_name
            sendConfi['model_id'] = this.rowSelected.model_id
            sendConfi['status'] = this.rowSelected.status
            sendConfi['model_version'] = this.rowSelected.model_version
            sendConfi['checked'] = this.rowSelected.checked
            sendConfi['meta'] = this.rowSelected.meta
            sendConfi['eval_metrics_value'] = 1
            for (var ite in paramProperties) {
              sendConfi[ite] = paramProperties[ite]
            }
            if (sendConfi['stopping_flag'] === false) {
              sendConfi['stopping_target'] = {}
            }
            modelConfiguration(sendConfi).then(response => {
              this.$emit('close', response)
            })
          }
        } else {
          sendConfi = modelProperties
          sendConfi['privacy-mechanisms'] = {}
          sendConfi['model_name'] = this.rowSelected.model_name
          sendConfi['model_id'] = this.rowSelected.model_id
          sendConfi['status'] = this.rowSelected.status
          sendConfi['model_version'] = this.rowSelected.model_version
          sendConfi['checked'] = this.rowSelected.checked
          sendConfi['meta'] = this.rowSelected.meta
          sendConfi['eval_metrics_value'] = 1
          for (var item in paramProperties) {
            sendConfi[item] = paramProperties[item]
          }
          if (sendConfi['stopping_flag'] === false) {
            sendConfi['stopping_target'] = {}
          }
          modelConfiguration(sendConfi).then(response => {
            this.$emit('close', response)
          })
        }
      }
    },
    verifyObjects(configuration, encryption, enc_sw, type) {
      // No configuration set
      if (Object.keys(configuration).length === 0) {
        return false
      }
      // Configuration set but not all fields
      if (Object.keys(configuration).length !== 0 && Object.keys(configuration).length < 6) {
        return false
      }
      // No configuration set and no encryption active
      if (Object.keys(configuration).length === 0 && enc_sw === false) {
        return false
      }
      // Encryption Active, Dp-Adaptive selected but not all fields completes
      if (type === 'dp-adaptive' && Object.keys(encryption).length < 7 && enc_sw === true) {
        return false
      }

      return true
    },
    closeConfiguration() {
      this.$emit('close', true)
    }
  }
}
</script>
<style scoped>
.tabs {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  background: rgb(255, 255, 255);
  padding: 1rem;
}
 .tabs__nav {
  display: flex;
}
 .tabs__nav_tab {
  padding: 1rem;
  margin: 0 0.2rem 0 0;
  background: #fff;
  border-radius:0.5rem 0.5rem 0 0;
  box-shadow: inset 0 -1rem 0.75rem -1rem rgba(0, 0, 0, 0.25);
  cursor: pointer;
  opacity: 0.75;
  transition: 100ms linear all;
}
 .tabs__nav_tab--active {
  opacity: 1;
  box-shadow: inset 0 -1rem 0.9rem 0.9rem rgba(29,30,51,0.12);
}
 .tabs__content {
  background: #fff;
  /* padding: 1rem; */
  border-radius: 0 0.5rem 0.5rem 0.5rem;
}
.comps{
	margin-top: 1rem;
}
.tabs{
  padding: 0 !important;
  padding-bottom: 1rem !important;
	height: auto !important;
}

.dialog-footer{
  display: flex;
  justify-content: space-between;
  padding-left: 1rem;
  padding-right: 1rem;
}
</style>
