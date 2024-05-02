<template>
  <el-dialog :visible.sync=" visibleDialogEncryption" :title="'Enter the encryption settings'">
    <el-form ref="encryptionProperties" :model="encryptionProperties" class="form_Pop">
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
        <!--         <el-input
          v-model="encryptionProperties.server_side_noising"
          style="width:80%"
        /> -->
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
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="danger" @click="closeEncryptionModel()">
        {{ $t("common.cancel") }}
      </el-button>
      <el-button type="success" @click="storeEncryptionData()">
        {{ $t("common.accept") }}
      </el-button>
    </div>
  </el-dialog>
</template>

<script>

export default {
  emits: ['returnValue', 'encryptionProperties'],
  props: {
    visibleDialogEncryption: Boolean
  },
  data() {
    return {
      encryptionForm: {},
      label_widthColumn: '190px',
      requiredText: '',
      encryptionProperties: {}
    }
  },
  methods: {
    closeEncryptionModel() {
      this.$emit('encryptionProperties', undefined)
      this.$emit('returnValue', false)
    },
    storeEncryptionData() {
      this.$refs['encryptionProperties'].validate(valid => {
        if (valid) {
          this.encryptionProperties.server_side_noising = this.StringToBoolean(this.encryptionProperties.server_side_noising)
          this.$emit('encryptionProperties', this.encryptionProperties)
          this.$emit('returnValue', false)
        }
      })
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
.form_Pop{
  z-index: 1200 !important;
}
</style>
