<template>
  <div>
    <div ref="terminal" id="container">
      <div v-if="banner" id="banner">
        <p>
          <img
            v-if="banner.img"
            :align="banner.img.align ? banner.img.align : 'left'"
            :src="banner.img.link ? banner.img.link : '@/logo.png'"
            :width="banner.img.width ? banner.img.width : '100px'"
            :height="banner.img.height ? banner.img.height : '100px'"
          />
        </p>
        <h2 v-if="banner.header" style="letter-spacing: 4px">{{banner.header}}</h2>
        <p v-if="banner.subHeader">{{banner.subHeader}}</p>
        <p v-if="banner.helpHeader">{{banner.helpHeader}}</p>
        <p></p>
      </div>
      <output ref="output" id="output" @click="notify()"></output>
      <div id="input-line" class="input-line">
        <div class="prompt">
          <div v-if="banner.emoji.first && showemoji">({{banner.emoji.first}})</div>
          <div v-if="banner.emoji.second && !showemoji">({{banner.emoji.second}})</div>
          <div>{{banner.sign ? banner.sign : ''}}</div>
        </div>

<!--         <input
          v-model="value"
          ref="cmd"
          @keydown.enter="cmd_enter($event)"
          @keydown.up="history_up()"
          @keydown.down="history_down()"
          @keydown.tab="cmd_tab($event)"
          class="cmdline"
          autofocus
        /> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["sendValue"],
  props: {
    shell_input: {
      required: false
    },
    model_name: {
      required: false
    },
    banner: {
      type: Object,
      required: false,
      default: () => {
        return {
          header: "Vue Shell",
          subHeader: "Shell is power just enjoy 🔥",
          helpHeader: 'Enter "help" for more information.',
          emoji: {
            first: "🔅",
            second: "🔆",
            time: 750
          },
          sign: "VueShell $",
          img: {
            align: "left",
            link: `@/logo.png`,
            width: 100,
            height: 100
          }
        };
      }
    },
    commands: {
      type: Array
    }
  },
  data() {
    return {
      showemoji: true,
      value: "",
      history_: [],
      histpos_: 0,
      histtemp_: 0
    };
  },
  computed: {
    allcommands() {
      var tab = ["help", "clear"];
      if (this.commands) {
        this.commands.forEach(a => {
          tab.push(a.name);
        });
      }

      return tab;
    }
  },
  watch: {
    shell_input(val) {
      this.output(val);
      this.$parent.send_to_terminal = "";
    }
  },
  methods: {
    notify() {
      /* var output_value = document.getElementById('output').value
      var arr_output_value = output_value.split('find')
      var arr_output_value_split = arr_output_value[1].split('model')
      var name = arr_output_value_split[0] */
      if(this.model_name) {
        window.localStorage.setItem('shell_model_name', this.model_name)
        this.$emit("sendValue",this.model_name)
      }
    },
    history_up() {
      if (this.history_.length) {
        if (this.history_[this.histpos_]) {
          this.history_[this.histpos_] = this.value;
        } else {
          this.histtemp_ = this.value;
        }
      }
      // up 38
      this.histpos_--;
      if (this.histpos_ < 0) {
        this.histpos_ = 0;
      }
      this.value = this.history_[this.histpos_]
        ? this.history_[this.histpos_]
        : this.histtemp_;
    },
    history_down() {
      if (this.history_.length) {
        if (this.history_[this.histpos_]) {
          this.history_[this.histpos_] = this.value;
        } else {
          this.histtemp_ = this.value;
        }
      }
      this.histpos_++;
      if (this.histpos_ > this.history_.length) {
        this.histpos_ = this.history_.length;
      }
      this.value = this.history_[this.histpos_]
        ? this.history_[this.histpos_]
        : this.histtemp_;
    },
    cmd_tab(e) {
      e.preventDefault();
    },
    cmd_enter() {
      if (this.value) {
        this.history_[this.history_.length] = this.value;
        this.histpos_ = this.history_.length;
      }

      //   Duplicate current input and append to output section.
      var line = this.$refs.cmd.parentNode.cloneNode(true);
      line.removeAttribute("id");
      line.classList.add("line");
      var input = line.querySelector("input.cmdline");
      input.autofocus = false;
      input.readOnly = true;
      this.$refs.output.appendChild(line);

      if (this.value && this.value.trim()) {
        var args = this.value.split(" ").filter(function(val) {
          return val;
        });
        var cmd = args[0].toLowerCase();
        args = args.splice(1); // Remove cmd from arg list.
      }

      if (cmd == "clear") {
        this.$refs.output.innerHTML = "";
        this.value = "";
      } else if (cmd == "help") {
        this.output(
          '<div class="ls-files">' + this.allcommands.join("<br>") + "</div>"
        );
      } else {
        if (this.commands) {
          this.commands.forEach(a => {
            if (cmd == a.name) {
              this.output(a.get());
              return;
            }
          });
        }
        if (this.value.trim() != "") {
          this.$emit("shell_output", this.value);
        }
        this.value = "";
      }

      // Clear/setup line for next input.
    },
    output(html) {
      this.$refs.output.insertAdjacentHTML(
        "beforeEnd",
        "<pre>" + html + "</pre>"
      );
      this.value = "";
    }
  },
  mounted() {
    if (
      this.banner.emoji.first &&
      this.banner.emoji.second &&
      this.banner.emoji.time
    ) {
      setInterval(() => {
        this.showemoji = !this.showemoji;
      }, this.banner.emoji.time);
    }
  }
/*   setup() {
    const notify = (props, { emit }) => {
      var output_value = document.getElementById('output')
      var arr_output_value = output_value.split('find')
      var arr_output_value_split = arr_output_value[1].split('model')
      var name = arr_output_value_split[0]
      console.log('NAME IN SHEELL ', name)
      emit("sendValue",name)
    }
    return { notify }
  } */
};
</script>

<style lang="css" scoped>
#container {
  color: white;
  background-color: #1E1D33;
  font-size: 11pt;
  font-family: Inconsolata, monospace;
  padding: 0.5em 1.5em 1em 1em;
}
#container output {
  clear: both;
  width: 100%;
}
#banner {
  margin-bottom: 3em;
}
img {
  margin-right: 20px;
}
.input-line {
/*   display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch; */
  display: flex;
  box-orient: horizontal;
  box-align: stretch;
  clear: both;
}
.input-line > div:nth-child(2) {
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
}
.prompt {
  white-space: nowrap;
  color: #3a8b17;
  margin-right: 7px;
  display: -webkit-box;
  display: -moz-box;
  display: flex;
  box-pack: center;
  box-orient: vertical;
  user-select: none;
}
.cmdline {
  outline: none;
  background-color: transparent;
  margin: 0;
  width: 100%;
  font: inherit;
  border: none;
  color: inherit;
}
.ls-files {
  height: 45px;
  column-width: 100px;
}
</style>