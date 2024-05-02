<template>
  <div id="encrypt">
    <div class="tabs__content_encrypt">
      <el-form v-if="activeTab === 'encrypt'" ref="encryptionProperties" :model="encryptionProperties" class="form_Pop">
        <!-- ENCRYPTION -->
        <el-form-item
          :label-with="label_widthColumn"
          :label="'Encryption'"
          prop="status"
        >
          <el-switch
            v-model="checkEncryption"
            active-color="#13ce66"
            active-value="true"
            inactive-value="false"
          />
        </el-form-item>
        <el-form-item
          v-if="checkEncryption==='true'"
          :label-with="label_widthColumn"
          :label="'Encryption Type'"
          prop="encryption"
          :rules="{ required: true, message: this.$t('overview.encryption') + requiredText, trigger: 'blur' }"
        >
          <el-select
            v-model="encryptionProperties.encryption"
            :label-width="label_widthColumn"
            placeholder="Type of encryption"
            class="strategy_input"
            v-on="handlers"
          >
            <el-option
              v-for="item in encryption"
              :key="item"
              :label="item"
              :value="item"
            />

          </el-select>
        </el-form-item>
        <div v-if="show_encrypt">
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.num_sampled_clients')"
            prop="num_sampled_clients"
            :rules="{ required: true, message: this.$t('encryption_table.num_sampled_clients') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.num_sampled_clients"
              type="number"
              style="width:80%"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.init_clip_norm')"
            prop="init_clip_norm"
            :rules="{ required: true, message: this.$t('encryption_table.init_clip_norm') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.init_clip_norm"
              type="number"
              style="width:80%"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.noise_multiplier')"
            prop="noise_multiplier"
            :rules="{ required: true, message: this.$t('encryption_table.noise_multiplier') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.noise_multiplier"
              type="number"
              style="width:80%"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.server_side_noising')"
            prop="server_side_noising"
          >
            <el-switch
              v-model="encryptionProperties.server_side_noising"
              active-color="#13ce66"
              active-value="true"
              inactive-value="false"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.clip_count_stddev')"
            prop="clip_count_stddev"
            :rules="{ required: true, message: this.$t('encryption_table.clip_count_stddev') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.clip_count_stddev"
              type="number"
              style="width:80%"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.clip_norm_target_quantile')"
            prop="clip_norm_target_quantile"
            :rules="{ required: true, message: this.$t('encryption_table.clip_norm_target_quantile') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.clip_norm_target_quantile"
              type="number"
              style="width:80%"
            />
          </el-form-item>
          <el-form-item
            :label-width="label_widthColumn"
            :label="this.$t('encryption_table.clip_norm_lr')"
            prop="clip_norm_lr"
            :rules="{ required: true, message: this.$t('encryption_table.clip_norm_lr') + requiredText, trigger: 'blur' }"
          >
            <el-input

              v-model="encryptionProperties.clip_norm_lr"
              type="number"
              style="width:80%"
            />
          </el-form-item>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import { getModelsList } from '@/api/FL_API'
export default {
  props: {
    activeTab: {
      type: String,
      default: ''
    },
    modelEncrypt: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      label_widthColumn: '190px',
      requiredText: '',
      encryptionProperties: {},
      checkEncryption: false,
      encryption: [],
      handlers: {
        change: this.onChange
      },
      show_encrypt: false,
      status: null
    }
  },
  watch: {
    checkEncryption(newVal) {
      this.status = newVal
      var bool = this.StringToBoolean(newVal)

      if (bool === false) {
        this.show_encrypt = false
      } else if (bool === true && this.encryptionProperties.encryption === 'dp-adaptive') {
        this.show_encrypt = true
      }
      if (this.modelEncrypt.hasOwnProperty('dp-adaptive')) {
        this.encryptionProperties = this.modelEncrypt['dp-adaptive']
      }
    }
  },
  created() {
    getModelsList().then(res => {
      this.encryption = res.message[0].encryption
    })
  },
  methods: {
    onChange(items) {
      this.encryptionProperties.encryption = items
      this.show_encrypt = items === 'dp-adaptive'
    },
    StringToBoolean(stringValue) {
      switch (stringValue) {
        case 'true':return true
        case 'false':return false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.dropdown_select{
display: flex !important;
flex-direction: column !important;
}
.encr_butt{
  /* background-color: #F5F7FA !important; */
  background-color: white !important;
  border: none !important;
  padding: 0 !important;
}
.encr_opt:hover{
  cursor: pointer;
  color: #1890ff;
}
</style>
