<template>
  <div>
    <div>
      <el-table
        style="width: 100%"
        :data="tableList"
      >
        <el-table-column
          prop="uploadDate"
          :label="$t('availableModel.tableInformationColumnModelDate')"
          width="110"
          align="center"
        />
        <el-table-column
          prop="fl_local_operations"
          :label="$t('availableModel.tableInformationColumnModelFlLocalOperations')"
          align="center"
        />
        <el-table-column
          prop="fl_training_rounds"
          :label="$t('availableModel.tableInformationColumnModelFlTrainingRounds')"
          align="center"
        />
        <el-table-column
          prop="mse"
          :label="$t('availableModel.eval_metrics')"
          align="center"
        />
        <el-table-column
          :label="$t('availableModel.tableInformationColumnModelDownload')"
          align="center"
        >
          <template slot-scope="{ row }">
            <el-button type="primary" @click="downloadModel(row)">{{ $t('availableModel.buttonDownload') }} <i class="el-icon-download el-icon-right" /></el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
import { downloadModel, trainedConfiguration } from '@/api/FL_API'
export default {
  components: {
  },
  props: {
    'tableList': {
      type: Array,
      default: function() {
        return []
      }
    },
    'total': {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      tableInformation: []
    }
  },
  mounted() {
    var nameSplit = this.tableList[0].filename.split('/')
    // var configurationId = { 'configurationId': parseInt(nameSplit[3]) }
    var configurationId = parseInt(nameSplit[3])
    trainedConfiguration().then(response => {
      var data = response.message
      var filterConfigIdObjects = data.filter(object => parseInt(object.configuration_id) === configurationId)
      /* var lo = filterConfigIdObjects[0].results.min_available_clients
      var rounds = response.message.number_of_rounds */
      this.tableList.forEach(element => {
        var obj = filterConfigIdObjects.filter(item => item.training_id === element.training_id)

        this.$set(element, 'fl_local_operations', obj[0].results.min_available_clients)
        this.$set(element, 'fl_training_rounds', obj[0].results.rounds)
        this.$set(element, 'mse', obj[0].results.accuracy)
      })
    })
    console.log(this.tableList)
  },
  methods: {
    async downloadModel(model) {
      var filename = model.filename.split('/')
      var model_name = filename[1]
      var model_version = filename[2]
      var dataObj = {
        'model_name': model_name,
        'model_version': model_version,
        'training_id': model.training_id
      }
      await downloadModel(dataObj).then(response => {
        this.b64toBlob(response.message).then(blob => this.saveFile(blob, 'model.pkl'))
      })
    },
    async b64toBlob(base64, type = 'application/octet-stream') {
      return await fetch(`data:${type};base64,${base64}`).then(res => res.blob())
    },
    saveFile(blob, filename) {
      if (window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(blob, filename)
      } else {
        const a = document.createElement('a')
        document.body.appendChild(a)
        const url = window.URL.createObjectURL(blob)
        a.href = url
        a.download = filename
        a.click()
        setTimeout(() => {
          window.URL.revokeObjectURL(url)
          document.body.removeChild(a)
        }, 0)
      }
    }
  }
}
</script>
<style lang="scss" scoped>
</style>
