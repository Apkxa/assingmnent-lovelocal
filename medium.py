<html lang="en"><head><style id="ace-chrome">.ace-chrome .ace_gutter {background: #ebebeb;color: #333;overflow : hidden;}.ace-chrome .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-chrome {background-color: #FFFFFF;color: black;}.ace-chrome .ace_cursor {color: black;}.ace-chrome .ace_invisible {color: rgb(191, 191, 191);}.ace-chrome .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-chrome .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-chrome .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-chrome .ace_invalid {background-color: rgb(153, 0, 0);color: white;}.ace-chrome .ace_fold {}.ace-chrome .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-chrome .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-chrome .ace_support.ace_type,.ace-chrome .ace_support.ace_class.ace-chrome .ace_support.ace_other {color: rgb(109, 121, 222);}.ace-chrome .ace_variable.ace_parameter {font-style:italic;color:#FD971F;}.ace-chrome .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-chrome .ace_comment {color: #236e24;}.ace-chrome .ace_comment.ace_doc {color: #236e24;}.ace-chrome .ace_comment.ace_doc.ace_tag {color: #236e24;}.ace-chrome .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-chrome .ace_variable {color: rgb(49, 132, 149);}.ace-chrome .ace_xml-pe {color: rgb(104, 104, 91);}.ace-chrome .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-chrome .ace_heading {color: rgb(12, 7, 255);}.ace-chrome .ace_list {color:rgb(185, 6, 144);}.ace-chrome .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-chrome .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-chrome .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-chrome .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-chrome .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-chrome .ace_gutter-active-line {background-color : #dcdcdc;}.ace-chrome .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-chrome .ace_storage,.ace-chrome .ace_keyword,.ace-chrome .ace_meta.ace_tag {color: rgb(147, 15, 128);}.ace-chrome .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-chrome .ace_string {color: #1A1AA6;}.ace-chrome .ace_entity.ace_other.ace_attribute-name {color: #994409;}.ace-chrome .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-chrome */</style><style id="autocompletion.css">.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #CAD6FA;    z-index: 1;}.ace_dark.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #3a674e;}.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid #abbffe;    margin-top: -1px;    background: rgba(233,233,253,0.4);    position: absolute;    z-index: 2;}.ace_dark.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid rgba(109, 150, 13, 0.8);    background: rgba(58, 103, 78, 0.62);}.ace_completion-meta {    opacity: 0.5;    margin: 0.9em;}.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #2d69c7;}.ace_dark.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #93ca12;}.ace_editor.ace_autocomplete {    width: 300px;    z-index: 200000;    border: 1px lightgray solid;    position: fixed;    box-shadow: 2px 3px 5px rgba(0,0,0,.2);    line-height: 1.4;    background: #fefefe;    color: #111;}.ace_dark.ace_editor.ace_autocomplete {    border: 1px #484747 solid;    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.51);    line-height: 1.4;    background: #25282c;    color: #c1c1c1;}
/*# sourceURL=ace/css/autocompletion.css */</style><style>.ace_snippet-marker {    -moz-box-sizing: border-box;    box-sizing: border-box;    background: rgba(194, 193, 208, 0.09);    border: 1px dotted rgba(211, 208, 235, 0.62);    position: absolute;}</style><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;perspective: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_text-input-ios {position: absolute !important;top: -100000px !important;left: -100000px !important;}
/*# sourceURL=ace/css/ace_editor.css */</style><script type="text/javascript" async="" src="medium_files/analytics.js"></script><script type="text/javascript" async="" src="medium_files/js_002"></script><script type="text/javascript" async="" src="medium_files/js"></script><script type="text/javascript" async="" src="medium_files/recaptcha__en.js" crossorigin="anonymous" integrity="sha384-JtvhFQlPQ6LL/+I5aABhkbXo/hmh5M6IvL9vK+ecFqveRPvf7P6cGzs1DEyU5A3c"></script><script async="" src="medium_files/analytics.js"></script><script type="text/javascript">
    var jsMetaDesc ={"Default":"Compile and run your code with ease on GeeksforGeeks Online IDE. GFG online compiler supports multiple languages like C, C++, Python, Java, NodeJS and more. Try it now on ide.geeksforgeeks.org","C":"Get fast, reliable C compilation online with our user-friendly compiler. Write, edit, and run your C code all in one place using the GeeksforGeeks C compiler. Perfect for students and professionals.","Cpp":"Get fast, reliable C compilation online with our user-friendly compiler. Write, edit, and run your C code all in one place using the GeeksforGeeks C compiler. Perfect for students and professionals.","Cpp14":"Get fast, reliable C compilation online with our user-friendly compiler. Write, edit, and run your C code all in one place using the GeeksforGeeks C compiler. Perfect for students and professionals.","Csharp":"Write and run C# code online with our user-friendly C# compiler, making it easy to test and debug your code in real-time, give our online compiler a try and see the power of online coding at your fingertips!","Java":"Experience the convenience of online coding with our user-friendly Java online compiler. Try it out now and see how easy it is to code online with our Java compiler!","Perl":"Easily write and run Perl code online with our user-friendly Perl compiler. Try our Perl compiler now and see the power of online coding at your fingertips!","Php":"Easily write and run PHP code online with our user-friendly PHP compiler. Plus, you can take input from the user and access standard libraries for quick and easy debugging.","Python":"Easily compile and run Python code online with our powerful Python compiler. With our online interpreter, you can test and debug your code in real-time, all from your web browser. Try it out now!","Python3":"Easily execute Python 3 code online with our user-friendly Python 3 compiler (interpreter). Our interpreter uses the latest version of the standard Python 3 interpreter to ensure accurate results. Try our Python 3 online compiler now!","Scala":"Write and run Scala code online with our user-friendly Scala compiler. Our online interpreter offers a simple Integrated Development Environment (IDE) for students and professionals.","Swift":"Swift Compiler Online is a web-based IDE for compiling and executing Swift code in real-time. Fast and convenient, perfect for quick testing.","Rust":"Rust Online Compiler - an easy-to-use IDE for writing, editing, and compiling Rust code in your browser. Features include syntax highlighting, code sharing, and library support. Ideal for students and professionals to quickly write, test, and execute Rust code.","Golang":"Golang Compiler Online - an intuitive IDE for Go programming. Edit, save, compile, and share Go code online with ease. User-friendly interface with libraries and syntax highlighting","R":"Write, run, and test R code online with R Online Compiler. User-friendly interface, syntax highlighting, library support, console, and no installation required.","Nodejs":"Streamline your coding process with our online JavaScript compiler.  Try it out now and see how it can simplify your coding experience.","Html":"Learn how to write and run HTML and CSS code using our online editor. Our real-time webview updates automatically as you write, making it easy to build and style your website. Try it out now and see the results instantly.","HTML":"Learn how to write and run HTML and CSS code using our online editor. Our real-time webview updates automatically as you write, making it easy to build and style your website. Try it out now and see the results instantly."};
</script>
<script type="text/javascript">
    function setPageTitleHeading(setLang) {
		let selectedLang = "C"
		
		if(setLang) {
			selectedLang = setLang
		} else if(localStorage.getItem('lang0') && localStorage.getItem('lang0') != 'null') {
			selectedLang = localStorage.getItem('lang0')
		} 

		newHeading = "Online Compiler and IDE"
		if(selectedLang == "Html"){
			newHeading = "HTML,CSS & JS Online Editor";
        }
		else if(selectedLang == "Cpp" || selectedLang == "Cpp14"){
			newHeading = "C++ Online Compiler";
        }
		else{
			newHeading = selectedLang + " Online Compiler"
		}
		newTitle = newHeading + ' - GeeksforGeeks';
		document.title = newTitle;
		document.querySelector('meta[name="description"]').setAttribute("content", jsMetaDesc[selectedLang]);
		$('#pageHeading').text(newHeading);
	}

    function setLocalStorage(currentTab, tabCode, tabLang, tabVis, tabSize) {
		try {
			for( var i = 0; i < tabSize; i++ ){
				localStorage.setItem( 'code'+i, tabCode[i] );
				localStorage.setItem( 'lang'+i, tabLang[i] );
				localStorage.setItem( 'vis'+i, tabVis[i] );
			}
			localStorage.setItem( 'currentTab', currentTab );
		} catch (error) {
			console.log(error.message);
		}
	}

    function getLocalStorage(search, tabSize) {
		let lang = localStorage.getItem( 'lang0' )
		if(window.location.pathname=="/" && lang == "Html") return [];
		if(!lang || (search && lang != search)) return [];

		let currentTab = parseInt(localStorage.getItem( 'currentTab' ));
		if( currentTab == '' || currentTab == null )currentTab = 0;
		let tabCounter = 0;
		let tabCode = [], tabLang = [], tabVis = [];

		for( var i = 0; i < tabSize; i++ ){
			tabCode[i] = localStorage.getItem( 'code'+i );
			tabLang[i] = localStorage.getItem( 'lang'+i );
			tabVis[i] = $.parseJSON(localStorage.getItem( 'vis'+i ));
			if( tabVis[i] == '' || tabVis[i] == null )tabVis[i] = false;
			if( tabCode[i] == null ) tabCode[i] = '';
			if( tabLang[i] == null || tabLang[i] == '' ) tabLang[i] = 'C';
			if( tabVis[i] == true )tabCounter++;
			$('#tab'+i+' > .text').text( $('[l='+tabLang[i]+']').html() );
		}
		setPageTitleHeading(lang);

		return [tabCounter, currentTab, tabCode, tabLang, tabVis];
	}

    function setSessionStorage(currentTab, tabCode, tabLang, tabVis, tabSize) {
		try {
			for( var i = 0; i < tabSize; i++ ){
				sessionStorage.setItem( 'code'+i, tabCode[i] );
				sessionStorage.setItem( 'lang'+i, tabLang[i] );
				sessionStorage.setItem( 'vis'+i, tabVis[i] );
			}
			sessionStorage.setItem( 'currentTab', currentTab );
		} catch (error) {
			console.log(error.message);
		}
	}

    function getSessionStorage(search, tabSize) {
		let lang = sessionStorage.getItem( 'lang0' )
		if(window.location.pathname=="/" && lang == "Html") return [];
		if(!lang || (search && lang != search)) return [];

		let currentTab = parseInt(sessionStorage.getItem( 'currentTab' ));
		if( currentTab == '' || currentTab == null )currentTab = 0;
		let tabCounter = 0;
		let tabCode = [], tabLang = [], tabVis = [];

		for( var i = 0; i < tabSize; i++ ){
			tabCode[i] = sessionStorage.getItem( 'code'+i );
			tabLang[i] = sessionStorage.getItem( 'lang'+i );
			tabVis[i] = $.parseJSON(sessionStorage.getItem( 'vis'+i ));
			if( tabVis[i] == '' || tabVis[i] == null )tabVis[i] = false;
			if( tabCode[i] == null ) tabCode[i] = '';
			if( tabLang[i] == null || tabLang[i] == '' ) tabLang[i] = 'C';
			if( tabVis[i] == true )tabCounter++;
			$('#tab'+i+' > .text').text( $('[l='+tabLang[i]+']').html() );
		}
		setPageTitleHeading(lang);

		return [tabCounter, currentTab, tabCode, tabLang, tabVis];
	}
</script>



	<meta charset="UTF-8">
	<meta name="keywords" content="programming, code online, snippet, snippets, code debugging, run code, execute code, C, C++, Java">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <meta property="og:image" content="https://media.geeksforgeeks.org/img-practice/gfg_200X200.png">
    <meta name="description" content="Easily compile and run Python code online with our powerful Python compiler. With our online interpreter, you can test and debug your code in real-time, all from your web browser. Try it out now!">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8">  
    	<title id="pageTitle">Python Online Compiler - GeeksforGeeks</title>

	<link rel="icon" href="https://ide.geeksforgeeks.org/images/gfglogo.ico" type="image/x-icon">
	<link href="medium_files/icon.css" rel="stylesheet"> 
        <link href="medium_files/css.css" rel="stylesheet"> 
	<link href="medium_files/font-awesome.min.css" rel="stylesheet">
	<link rel="stylesheet" href="medium_files/bootstrap.min.css">
	<link rel="stylesheet" href="medium_files/gfg-style.css">
	<link rel="stylesheet" type="text/css" href="medium_files/cookieconsent.min.css">
	<link rel="stylesheet" href="medium_files/header-footer.css">

	<script src="medium_files/jquery.min.js"></script>
	<script defer="defer" src="medium_files/bootstrap.min.js"></script>
	<script src="medium_files/clipboard.min.js"></script>
	<script type="text/javascript">
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		ga('create', 'UA-37433965-2', 'auto');ga('send', 'pageview');
	</script>
	<script defer="defer" src="medium_files/ace.js"></script>
	<script defer="defer" src="medium_files/ext-themelist.js"></script>
	<script defer="defer" src="medium_files/ext-language_tools.js"></script>
    <script src="medium_files/beautify-html.min.js"></script>
	<script defer="defer" src="medium_files/gfg-main.js"></script>
	<script async="" src="medium_files/gfg-header-footer.js"></script>
	<!--[if lt IE 9]>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js" type="text/javascript"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/respond.js/1.4.2/respond.min.js" type="text/javascript"></script>
	<![endif]-->
	<script async="async" src="medium_files/f_002.txt"></script>
	<script>
		var googletag = googletag || {};
		googletag.cmd = googletag.cmd || [];
	</script>
<script async="" src="medium_files/optimize.js"></script>	

        <script src="medium_files/cookieconsent.min.js"></script>
        <script>
        window.addEventListener("load", function(){
        window.cookieconsent.initialise({
        "palette": {
            "popup": {
              "background": "#3c404d",
              "text": "#d6d6d6"
            },
            "button": {
              "background": "#8bed4f"
            }
          },
          "theme": "classic",
            onStatusChange: function(status) {
            
            },
            law: {
              regionalLaw: false,
            },
            location: true,
            "content": {
            "message": "We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our <a href=\"https://www.geeksforgeeks.org/cookie-policy/\" class=\"cc-link\" target=\"_blank\">Cookie Policy</a> & ",
            "link": "Privacy Policy",
            "href": "https://www.geeksforgeeks.org/privacy-policy/"
            },
        cookie: {
        name : "geeksforgeeks_consent_status",
        }
        })});
    
        </script>
	          <script src="medium_files/client" async="" defer="defer"></script>
      	<style id="googleidentityservice_button_styles">.qJTHM{-moz-user-select:none;color:#202124;direction:ltr;font-family:"Roboto-Regular",arial,sans-serif;font-weight:400;margin:0;overflow:hidden}.ynRLnc{left:-9999px;position:absolute;top:-9999px}.L6cTce{display:none}.bltWBb{word-break:break-all}.hSRGPd{color:#1a73e8;cursor:pointer;font-weight:500;text-decoration:none}.Bz112c-W3lGp{height:16px;width:16px}.Bz112c-E3DyYd{height:20px;width:20px}.Bz112c-r9oPif{height:24px;width:24px}.Bz112c-uaxL4e{-moz-border-radius:10px;border-radius:10px}.LgbsSe-Bz112c{display:block}.S9gUrf-YoZ4jf,.S9gUrf-YoZ4jf *{border:none;margin:0;padding:0}.fFW7wc-ibnC6b>.aZ2wEe>div{border-color:#4285f4}.P1ekSe-ZMv3u>div:nth-child(1){background-color:#1a73e8!important}.P1ekSe-ZMv3u>div:nth-child(2),.P1ekSe-ZMv3u>div:nth-child(3){background-image:linear-gradient(to right,rgba(255,255,255,.7),rgba(255,255,255,.7)),linear-gradient(to right,#1a73e8,#1a73e8)!important}.haAclf{display:inline-block}.nsm7Bb-HzV7m-LgbsSe{border-radius:4px;box-sizing:border-box;transition:background-color .218s,border-color .218s;-moz-user-select:none;background-color:#fff;background-image:none;border:1px solid #dadce0;color:#3c4043;cursor:pointer;font-family:"Google Sans",arial,sans-serif;font-size:14px;height:40px;letter-spacing:0.25px;outline:none;overflow:hidden;padding:0 12px;position:relative;text-align:center;vertical-align:middle;white-space:nowrap;width:auto}@media screen and (-ms-high-contrast:active){.nsm7Bb-HzV7m-LgbsSe{border:2px solid windowText;color:windowText}}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe{font-size:14px;height:32px;letter-spacing:0.25px;padding:0 10px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe{font-size:11px;height:20px;letter-spacing:0.3px;padding:0 8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe{padding:0;width:40px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe{width:32px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe{width:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK{border-radius:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.pSzOP-SxQuSe{border-radius:16px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.purZT-SxQuSe{border-radius:10px}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc{border:none;color:#fff}.nsm7Bb-HzV7m-LgbsSe.MFS4be-v3pZbf-Ia7Qfc{background-color:#1a73e8}.nsm7Bb-HzV7m-LgbsSe.MFS4be-JaPV2b-Ia7Qfc{background-color:#202124;color:#e8eaed}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:18px;margin-right:8px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:14px;min-width:14px;width:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:10px;min-width:10px;width:10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin-left:8px;margin-right:-4px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:10px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:4px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-top-left-radius:3px;border-bottom-left-radius:3px;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;justify-content:center;align-items:center;background-color:#fff;height:36px;margin-left:-10px;margin-right:12px;min-width:36px;width:36px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c,.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:28px;margin-left:-8px;margin-right:10px;min-width:28px;width:28px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:16px;margin-left:-6px;margin-right:8px;min-width:16px;width:16px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-radius:3px;margin-left:2px;margin-right:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-radius:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-radius:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-radius:8px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;align-items:center;flex-direction:row;justify-content:space-between;flex-wrap:nowrap;height:100%;position:relative;width:100%}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX{justify-content:center}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{flex-grow:1;font-family:"Google Sans",arial,sans-serif;font-weight:500;overflow:hidden;text-overflow:ellipsis;vertical-align:top}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-weight:300}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX .nsm7Bb-HzV7m-LgbsSe-BPrWId{flex-grow:0}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-MJoBVe{transition:background-color .218s;bottom:0;left:0;position:absolute;right:0;top:0}.nsm7Bb-HzV7m-LgbsSe:hover,.nsm7Bb-HzV7m-LgbsSe:focus{box-shadow:none;border-color:#d2e3fc;outline:none}.nsm7Bb-HzV7m-LgbsSe:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.04)}.nsm7Bb-HzV7m-LgbsSe:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.1)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.24)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.32)}.nsm7Bb-HzV7m-LgbsSe .n1UuX-DkfjY{border-radius:50%;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;height:20px;margin-left:-4px;margin-right:8px;min-width:20px;width:20px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-family:"Roboto";font-size:12px;text-align:left}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .ssJRIf,.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .fmcmS{overflow:hidden;text-overflow:ellipsis}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;align-items:center;color:#5f6368;fill:#5f6368;font-size:11px;font-weight:400}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.MFS4be-Ia7Qfc .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{color:#e8eaed;fill:#e8eaed}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .Bz112c{height:18px;margin:-3px -3px -3px 2px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-top-left-radius:0;border-bottom-left-radius:0;border-top-right-radius:3px;border-bottom-right-radius:3px;margin-left:12px;margin-right:-10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{border-radius:18px}.L5Fo6c-sM5MNb{border:0;display:block;left:0;position:relative;top:0}.L5Fo6c-bF1uUb{-moz-border-radius:4px;border-radius:4px;bottom:0;cursor:pointer;left:0;position:absolute;right:0;top:0}.L5Fo6c-bF1uUb:focus{border:none;outline:none}sentinel{}</style><script src="medium_files/theme-chrome.js"></script><script src="medium_files/text.js"></script><script src="medium_files/mode-python.js"></script><link id="googleidentityservice" type="text/css" media="all" rel="stylesheet" href="medium_files/style.css"><meta http-equiv="origin-trial" content="AymqwRC7u88Y4JPvfIF2F37QKylC04248hLCdJAsh8xgOfe/dVJPV3XS3wLFca1ZMVOtnBfVjaCMTVudWM//5g4AAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjk1MTY3OTk5LCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="medium_files/python.js"></script><meta http-equiv="origin-trial" content="As0hBNJ8h++fNYlkq8cTye2qDLyom8NddByiVytXGGD0YVE+2CEuTCpqXMDxdhOMILKoaiaYifwEvCRlJ/9GcQ8AAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="AgRYsXo24ypxC89CJanC+JgEmraCCBebKl8ZmG7Tj5oJNx0cmH0NtNRZs3NB5ubhpbX/bIt7l2zJOSyO64NGmwMAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A/ERL66fN363FkXxgDc6F1+ucRUkAhjEca9W3la6xaLnD2Y1lABsqmdaJmPNaUKPKVBRpyMKEhXYl7rSvrQw+AkAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MTkzNTk5OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A6OdGH3fVf4eKRDbXb4thXA4InNqDJDRhZ8U533U/roYjp4Yau0T3YSuc63vmAs/8ga1cD0E3A7LEq6AXk1uXgsAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MTkzNTk5OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="medium_files/f.txt" async=""></script><script async="" src="medium_files/27823234"></script><script async="" src="medium_files/AGSKWxU6Hhdhq6vIxyP3ocW1XuG6ydvWU8iDZH1jXgygKdD4MtNhaI4hNaoW4FQB"></script><script esp-signal="true" src="medium_files/esp.js"></script><script async="" src="medium_files/AGSKWxWfsiOm0a9GGmx3aoddsw4mVqCO6Xv3UDfLhQtg5sT3uUkkrY4F4_KCguyM"></script><script async="" src="medium_files/AGSKWxU5UlZFj459siQPPStgXbJ8W64ZipyXjDWmKYWlaYvF3weaQiFJe9jIRr-v"></script><script async="" src="medium_files/AGSKWxXyUYTeHCg_kxS01q36Fzz-YWeYi3dmG-sR17vkIYqvV0sCtYc4FOma6j_q"></script><style></style></head><body class="header-body" style="margin: 0;"><div role="dialog" aria-live="polite" aria-label="cookieconsent" aria-describedby="cookieconsent:desc" class="cc-window cc-banner cc-type-info cc-theme-classic cc-bottom cc-color-override-382972913 cc-invisible" style="display: none;"><!--googleoff: all--><span id="cookieconsent:desc" class="cc-message">We
 use cookies to ensure you have the best browsing experience on our 
website. By using our site, you acknowledge that you have read and 
understood our <a href="https://www.geeksforgeeks.org/cookie-policy/" class="cc-link" target="_blank">Cookie Policy</a> &amp;  <a aria-label="learn more about cookies" role="button" tabindex="0" class="cc-link" href="https://www.geeksforgeeks.org/privacy-policy/" target="_blank">Privacy Policy</a></span><div class="cc-compliance"><a aria-label="dismiss cookie message" role="button" tabindex="0" class="cc-btn cc-dismiss">Got it!</a></div><!--googleon: all--></div><div id="g_id_onload" data-client_id="388036620207-3uolk1hv6ta7p3r9l6s3bobifh086qe1.apps.googleusercontent.com" data-login_uri="https://auth.geeksforgeeks.org/oauth/google.php"  data-state_cookie_domain="geeksforgeeks.org" data-redirect="https://ide.geeksforgeeks.org/online-python-compiler" data-cancel_on_tap_outside="false"></div>
           <script>
		var cdnUrl = "https://ide.geeksforgeeks.org/";
        var ide_backend_url = "https://codejudge.geeksforgeeks.org/";
        </script>


  

    <i id="utoken" style="display:none"></i>
    <div class="header-main__wrapper stick-me">
        <a href="https://ide.geeksforgeeks.org/" class="header-main__logo">
            <div class="_logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="76.533" height="39.026" viewBox="0 0 76.533 39.026" class="normal">
                    <path d="M2380.7,6597.866a12.252,12.252,0,0,0-.261-1.513l-30.726-.027a12.545,12.545,0,0,1,.908-3.443,12.337,12.337,0,0,1,2.739-4.044,12.151,12.151,0,0,1,4.018-2.581,12.634,12.634,0,0,1,14.3,3.051l4.852-4.748a18.176,18.176,0,0,0-6.131-4.331,20.037,20.037,0,0,0-8.112-1.564,20.25,20.25,0,0,0-7.671,1.459,19.158,19.158,0,0,0-6.261,4.07,19.584,19.584,0,0,0-4.226,6.184,18.7,18.7,0,0,0-1.487,5.947h-.2a18.674,18.674,0,0,0-1.489-5.947,19.544,19.544,0,0,0-4.226-6.184,19.133,19.133,0,0,0-6.261-4.07,21.354,21.354,0,0,0-15.783.1,18.2,18.2,0,0,0-6.131,4.331l4.853,4.748a13.264,13.264,0,0,1,14.3-3.051,12.131,12.131,0,0,1,4.017,2.581,12.323,12.323,0,0,1,2.74,4.044,12.527,12.527,0,0,1,.908,3.443l-30.726.027a12.256,12.256,0,0,0-.261,1.513,15,15,0,0,0-.1,1.773,20.713,20.713,0,0,0,1.1,6.783,15.709,15.709,0,0,0,3.443,5.686,17.309,17.309,0,0,0,6,4.123,20.587,20.587,0,0,0,7.983,1.46,20.226,20.226,0,0,0,7.669-1.46,19.086,19.086,0,0,0,6.261-4.07,19.506,19.506,0,0,0,4.226-6.184,18.163,18.163,0,0,0,1.153-3.629h.871a18.27,18.27,0,0,0,1.151,3.629,19.545,19.545,0,0,0,4.226,6.184,19.111,19.111,0,0,0,6.261,4.07,20.241,20.241,0,0,0,7.671,1.46,20.572,20.572,0,0,0,7.981-1.46,17.282,17.282,0,0,0,6-4.123,15.717,15.717,0,0,0,3.445-5.686,20.726,20.726,0,0,0,1.1-6.783A15.259,15.259,0,0,0,2380.7,6597.866Zm-46.245,5.608a12.1,12.1,0,0,1-2.766,4.043,12.467,12.467,0,0,1-4.043,2.583,14.378,14.378,0,0,1-9.939.052,11.776,11.776,0,0,1-3.522-2.218,8.459,8.459,0,0,1-1.8-2.374,13.476,13.476,0,0,1-1.173-3.208l23.658,0A11.487,11.487,0,0,1,2334.457,6603.475Zm38.236,2.086a8.466,8.466,0,0,1-1.8,2.374,11.771,11.771,0,0,1-3.522,2.218,14.378,14.378,0,0,1-9.939-.052,12.491,12.491,0,0,1-4.044-2.583,12.088,12.088,0,0,1-2.765-4.043,11.427,11.427,0,0,1-.415-1.126h11.92v0h11.739A13.509,13.509,0,0,1,2372.692,6605.561Z" transform="translate(-2304.273 -6578.666)" fill="#2f8d46"></path>
                </svg>
		<svg xmlns="http://www.w3.org/2000/svg" width="45.42" height="24.603" viewBox="0 0 39.42 18.603" aria-hidden="false"><defs><style>.a{fill:#0f2b3c;}</style></defs><path class="a" d="M6.021,0V-18.6H2.268V0Zm4.536-18.6V0h7.29a8.278,8.278,0,0,0,5.81-2.211A9.455,9.455,0,0,0,26.3-9.261c0-5.292-3.1-9.342-8.451-9.342ZM14.31-3.321V-15.282h3.537c3.1,0,4.7,2.835,4.7,6.021s-1.593,5.94-4.7,5.94ZM33.534-7.479h6.939v-3.375H33.534v-4.428h7.911V-18.6H29.781V0H41.688V-3.321H33.534Z" transform="translate(-2.268 18.603)"></path></svg>
            </div>
        </a>
        <div class="header-main__container">
            <h1 style="font-size:18px" id="pageHeading" class="header-main__right">Python Online Compiler</h1>
            <span class="hamburger-menu"> <!-- sidebar on tab and mobile view -->
                <span class="gfg-burger-1"></span>
                <span class="gfg-burger-2"></span>
                <span class="gfg-burger-3"></span>
            </span>
            <ul class="header-main__list">
		
            </ul>
            <ul class="header-main__left-list" data-type="0" data-nl="false">
                                <li class="header-main__left-list-item profile-head" style="margin-top: auto;margin-bottom: auto;" aria-expanded="false" data-expandable="false">
                    <a type="button" class="header-main__signup login-modal-btn" href="https://auth.geeksforgeeks.org/?to=https%3A%2F%2Fide.geeksforgeeks.org%2Fonline-python-compiler">Sign In</a>
                </li>
                            </ul>
        </div>
        <div class="gfg-overlay display-none" id="gfg-overlay"></div>
        <div class="header-sidebar__wrapper">
            <ul class="header-sidebar__list">
                                <li class="header-sidebar__list-item"><a href="https://auth.geeksforgeeks.org/?to=https%3A%2F%2Fide.geeksforgeeks.org%2Fonline-python-compiler" class="gfg-sec-bg color-white login-modal-btn" style="color: white!important; text-align: center; padding : 10px!important;" target="_self">Sign In</a>
                </li>
                                <li class="header-sidebar__list-item">
                    <a href="https://ide.geeksforgeeks.org/report.php">Report Bug</a>
                </li>
                <li class="dropdown header-sidebar__list-item">
                    <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Theme <span class="caret"></span></a>
                    <ul class="dropdown-menu theme-sidebar">
                        <li class="theme"><a href="javascript:void(0)">Light</a></li>
                        <li class="theme"><a href="javascript:void(0)">Dark</a></li>
                    </ul>
                </li>
            </ul>
            <div class="" style="height: 80px;"></div>
        </div>

    </div>  <!-- header-main__wrapper stick-me -->

<link rel="stylesheet" href="medium_files/font-awesome.min_002.css">
<link rel="stylesheet" href="medium_files/bootstrap-social.css">
<script src="medium_files/api.js" async="" defer="defer"></script>
<script src="medium_files/platform.js" gapi_processed="true"></script>
<link rel="stylesheet" href="medium_files/css_002.css">
<link rel="stylesheet" href="medium_files/icon.css">
<script src="medium_files/typeahead.bundle.js"></script> 
<style>
  *,
  *:after,
  *:before{
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }

  .login-modal-div form{
    margin-bottom: 14px;
  }

  .login-modal-div input[type=checkbox]{
    display: inline-block !important;
  }

  /* The Modal (background) */
  .login-modal-div{
    font-family: 'RobotoDraft', 'Roboto', 'Helvetica Neue, Helvetica, Arial', sans-serif;
    display: none;
    position: fixed; /* Stay in place */
    z-index: 1000; /* Sit on top */
    padding-top: 70px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  }

  /* Modal Content */
  .login-modal-div .modal-content{
    background-color: #eff1f3;
    margin: auto;
    padding-top: 20px;
    border: 1px solid #888;
    width: 550px;
    border-radius: 5px;
  }

  /* The Close Button */
  .login-modal-div .close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .login-modal-div .close:hover,
  .login-modal-div .close:focus {
      color: #000;
      text-decoration: none;
      cursor: pointer;
  }

  .login-modal-div img.logo{
    width: 250px;
  }

  .login-modal-div .white-bg{
    background-color: #fff;
  }

  .login-modal-div .close-div{
    height: 30px;
    padding: 0 20px;
  }

  .login-modal-div .modal-header{
    padding: 20px;
    border-radius: 5px;
  }

  .login-modal-div .center{
    text-align: center;
  }

  .login-modal-div .alert{
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid transparent;
    border-radius: 4px;
  }

  .login-modal-div #extra .alert-danger, .login-modal-div .extra .alert-danger{
    color: #f1270b;
    background-color: transparent; 
    border-color: #f65039;
    font-weight: 400;
    font-size: 14px;
    line-height: 1.3;
  }

  .login-modal-div #extra .alert-info, .login-modal-div .extra .alert-info{
    color: #1583ed;
    background-color: transparent;
    border-color: #418bf9;
    font-weight: 400;
    font-size: 14px;
    line-height: 1.3;
  }

  .login-modal-div input[type=text],
  .login-modal-div input[type=email],
  .login-modal-div input[type=password]{
    border: 1px solid #C2C7D0;
    border-top-color: rgb(194, 199, 208);
    border-right-color: rgb(194, 199, 208);
    border-bottom-color: rgb(194, 199, 208);
    border-left-color: rgb(194, 199, 208);
    border-radius: 5px;
    box-shadow: inset 0 1px 2px rgba(151,159,175,0.1),inset 0 1px 15px rgba(151,159,175,0.05);
    box-sizing: border-box;
    color: #39424e;
    display: inline-block;
    line-height: 1.5em;
    margin-left: 0;
    margin-right: 0;
    margin-top: 0;
    margin-bottom: 10px;
    padding: 7px 10px;
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
    font-weight: 500;
    width: 100%;
  }

  .modal-form-group{
    margin-top: 15px;
    margin-bottom: 15px;
    position: relative;
  }

  .modal-form-group .input-icon{
    position: absolute;
    z-index: 1;
    left: 8px;
    top: 10px;
    color: #979faf;
    font-size: 26px;
  }

  .modal-form-group .modal-form-input{
    display: block !important;
    padding: 15px 8px 8px 45px !important;
    height: auto !important;
    width: 450px;
  }

  .modal-form-group .modal-form-input:focus{
    border-color: #0f9d58 !important;
    -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 5px rgba(78, 236, 141, 0.6) !important;
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 5px rgba(78, 236, 141, 0.6) !important;
  }

  .modal-form-group .modal-form-input.error-focus, .modal-form-group .modal-form-input.error-focus:focus{
    border-color: #ef1313 !important;
    -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 5px rgba(177, 74, 71, 0.6) !important;
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 5px rgba(177, 74, 71, 0.6) !important;
  }

  .modal-form-group .modal-form-input::placeholder{
    color: #999;
    font-weight: 400;
    font-size: 16px;
  }

  @media(max-width: 768px){
    .login-modal-div{
      padding-top: 30px;
    }

    .login-modal-div .modal-content{
      width: 90%;
    }

    .modal-form-group .modal-form-input{
      width: 100%;
    }
  }

  .login-modal-div .modal-header section{
    display: none;
    padding: 20px 30px 30px 30px;
    border: 1px solid #ddd;
    border-bottom: none;
  }

  .login-modal-div .modal-header input[type=radio]{
    display: none;
  }

  .login-modal-div .modal-header label.tab-label{
    display: inline-block;
    margin: 0 0 -1px;
    padding: 15px 25px;
    font-weight: 600;
    text-align: center;
    color: #888;
    border: 1px solid transparent;
    width: 50%;
    padding-bottom: 12px;
    font-size: 20px;
    border-bottom-width: 4px;
    background-color: #e9ebee;
  }

  .login-modal-div .modal-header label.tab-label:first-of-type{
    float: left;
  }

  .login-modal-div .modal-header label.tab-label:before{
    font-weight: normal;
    margin-right: 10px;
  }

  .login-modal-div .modal-header label:hover{
    color: #888;
    cursor: pointer;
  }

  .login-modal-div .modal-header input:checked + label.tab-label{
    color: #555;
    border: 1px solid #ddd;
    border-top: 2px solid #0f9d58;
    border-bottom: 3px solid #fff;
    background-color: #fff;
  }

  .login-modal-div .modal-header #tab1:checked ~ #content1,
  .login-modal-div .modal-header #tab2:checked ~ #content2{
    display: block;
  }

  @media screen and (max-width: 650px) {
    .login-modal-div .modal-header label.tab-label:before{
      margin: 0;
      font-size: 18px;
    }
  }

  @media screen and (max-width: 400px) {
    .login-modal-div .modal-header label.tab-label{
      padding: 15px;
    }
  }

  /* css for overlay loading spinner */

  /* Absolute Center Spinner */
  .spinner-loading-overlay {
    position: fixed;
    display: none;
    z-index: 1001;
    height: 2em;
    width: 2em;
    overflow: show;
    margin: auto;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
  }

  /* Transparent Overlay */
  .spinner-loading-overlay:before {
    content: '';
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(239,236,233,0.7);
  }

  .spinner-loading-overlay:not(:required):after {
    content: '';
    display: block;
    font-size: 20px;
    width: 0.6em;
    height: 0.6em;
    margin-top: -0.5em;
    -webkit-animation: spinner 1500ms infinite linear;
    -moz-animation: spinner 1500ms infinite linear;
    -ms-animation: spinner 1500ms infinite linear;
    -o-animation: spinner 1500ms infinite linear;
    animation: spinner 1500ms infinite linear;
    border-radius: 0.5em;
    -webkit-box-shadow: rgba(15, 157, 88, 0.75) 1.5em 0 0 0, rgba(15, 157, 88, 0.75) 1.1em 1.1em 0 0, rgba(15, 157, 88, 0.75) 0 1.5em 0 0, rgba(15, 157, 88, 0.75) -1.1em 1.1em 0 0, rgba(15, 157, 88, 0.75) -1.5em 0 0 0, rgba(15, 157, 88, 0.75) -1.1em -1.1em 0 0, rgba(15, 157, 88, 0.75) 0 -1.5em 0 0, rgba(15, 157, 88, 0.75) 1.1em -1.1em 0 0;
    box-shadow: rgba(15, 157, 88, 0.75) 1.5em 0 0 0, rgba(15, 157, 88, 0.75) 1.1em 1.1em 0 0, rgba(15, 157, 88, 0.75) 0 1.5em 0 0, rgba(15, 157, 88, 0.75) -1.1em 1.1em 0 0, rgba(15, 157, 88, 0.75) -1.5em 0 0 0, rgba(15, 157, 88, 0.75) -1.1em -1.1em 0 0, rgba(15, 157, 88, 0.75) 0 -1.5em 0 0, rgba(15, 157, 88, 0.75) 1.1em -1.1em 0 0;
  }

  /* Animation */

  @-webkit-keyframes spinner {
    0% {
      -webkit-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -ms-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -ms-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
  @-moz-keyframes spinner {
    0% {
      -webkit-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -ms-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -ms-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
  @-o-keyframes spinner {
    0% {
      -webkit-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -ms-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -ms-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
  @keyframes spinner {
    0% {
      -webkit-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -ms-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -ms-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
  /* css end for spinner loading */

  .login-modal-div .left{
    text-align: left;
  }

  .login-modal-div .right{
    text-align: right;
  }

  .login-modal-div .pull-right{
    float: right;
  }

  .login-modal-div .pull-left{
    float: left;
  }

  .modal-form-label{
    vertical-align: middle;
    font-weight: 500;
    color: #404040;
    font-size: 12px;
    position: relative;
    /*top: -5px;*/
  }

  .login-modal-div a{
    color: #979faf;
  }

  .login-modal-div a:hover{
    color: #0f9d58;
    text-decoration: underline;
  }

  .login-modal-div .btn{
    background-color: whitesmoke;
    background-image: -webkit-gradient(linear, top left, bottom left, color-stop(0, #2bbe60), color-stop(1, #0f9d58));
    background-image: -webkit-linear-gradient(top, #2bbe60, #0f9d58);
    background-image: linear-gradient(to bottom, #2bbe60, #0f9d58);
    border: 1px solid #0f9d58;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08),inset 0 -1px 4px rgba(151,159,175,0.2);
    box-sizing: border-box;
    cursor: pointer;
    display: inline-block;
    padding: 10px 20px;
    margin-bottom: 0;
    font-size: 16px;
    font-weight: 500;
    line-height: 18px;
    position: relative;
    color: #39424e;
    text-align: center;
    text-decoration: none !important;
    vertical-align: middle;
  }

  .login-modal-div .btn-green{
    color: #fff;
    background-color: #0f9d58;
    width: 100%;
    text-shadow: none;
  }

  .login-modal-div .forgot-link, .login-modal-div .login-link{
    cursor: pointer;
    font-weight: 500;
    font-size: 12px;
    position: relative;
    bottom: -5px;
  }

  @media(max-width: 768px){
    .login-modal-div .forgot-link, .login-modal-div .login-link{
      padding: 10px 0px;    
    }
  }

  .login-modal-div .social-signin-div{
    border: 1px solid #ddd;
    border-top: none;
    padding-bottom: 20px;
  }

  .login-modal-div .social-signin-div .social-div{
    width: 50%;
    display: inline-block;
    padding: 5px 30px;
  }

  .login-modal-div .social-signin-div .tnc-div{
    font-size: 10px;
    padding: 0 15px;
    color: #999;
    margin-top: 10px;
    margin-bottom: 0;
  }

  .login-modal-div .social-signin-div .tnc-div a{
    color: #0f9d58;
  }

  .login-modal-div .social-signin-div .social-divider{
    width: 80%;
    text-align: center;
    border-bottom: 1px solid #979faf;
    line-height: 0.1em;
    margin: -20px 0 20px;
    margin-left: 10%;
  }

  .login-modal-div .social-signin-div .social-divider span{
    background: #fff;
    padding: 0 10px;
  }

  .login-modal-div .social-signin-div .btn-social{
    padding-left: 40px;
    color: #fff;
  }

  .login-modal-div .social-signin-div .btn-social span.fa{
    padding-top: 2px;
  }

  .login-modal-div .social-signin-div .btn-google{
    background-image: -webkit-gradient(linear, top left, bottom left, color-stop(0, #dd4e41), color-stop(1, #c9453a));
    background-image: -webkit-linear-gradient(top, #dd4e41, #c9453a);
    background-image: linear-gradient(to bottom, #dd4e41, #c9453a);
    color: #fff;
    border: 1px solid #c9453a;
    padding-left: 60px;
  }

  .login-modal-div .social-signin-div .btn-facebook{
    background-image: -webkit-gradient(linear, top left, bottom left, color-stop(0, #4b66a0), color-stop(1, #3b5998));
    background-image: -webkit-linear-gradient(top, #4b66a0, #eb5998);
    background-image: linear-gradient(to bottom, #4b66a0, #3b5998);
    color: #fff;
    border: 1px solid #3b5998;
  }

  .login-modal-div .social-signin-div .btn-linkedin{
    background-image: -webkit-gradient(linear, top left, bottom left, color-stop(0, #0073b1), color-stop(1, #075b8c));
    background-image: -webkit-linear-gradient(top, #0073b1, #075b8c);
    background-image: linear-gradient(to bottom, #0073b1, #075b8c);
    color: #fff;
    border: 1px solid #075b8c;
    padding-left: 60px;
  }

  .login-modal-div .social-signin-div .btn-github{
    background-image: -webkit-gradient(linear, top left, bottom left, color-stop(0, #4a4646), color-stop(1, #191717));
    background-image: -webkit-linear-gradient(top, #4a4646, #191717);
    background-image: linear-gradient(to bottom, #4a4646, #191717);
    color: #fff;
    border: 1px solid #191717;
    padding-left: 60px;
  }

  .login-modal-div .forgot-div{
    padding: 20px 30px 30px 30px;
    border: 1px solid #ddd;
    display: none;
  }

  .login-modal-div .forgot-div p:first-of-type{
    font-weight: 400;
    color: #404040;
  }

  .login-modal-div div.input-error{
    font-size: 12px;
    color: #b71c1c;
    letter-spacing: 0.83;
    text-align: left;
    position: relative;
    bottom: 10px;
    font-weight: 500;
  }

  #glogin, #fblogin, #inlogin, #gitlogin{
    display: block;
  }

  @media(max-width:468px){
    .login-modal-div .social-signin-div .social-div{
      padding: 0;
    }

    #glogin, #fblogin, #inlogin, #gitlogin{
      font-size: 14px !important;
      display: inline-block;
    }

    #glogin{
      padding-left: 50px !important;
    }

    #inlogin{
      padding-left: 43px !important;
    }
  }

  /* CSS fixes in existing login modal done by Ankit Kushwaha */ 

  .login-modal-div .twitter-typeahead{
    display: block !important;
  }
  .login-modal-div .tt-dropdown-menu, .login-modal-div .tt-menu {
    width: 100%;
    margin-top: 2px;
    padding: 8px 0;
    background-color: #F9F9F9;
    border: 1px solid #ccc;
    border: 1px solid rgba(0,0,0,.2);
    border-radius: 8px;
    box-shadow: 0 5px 10px rgb(0 0 0 / 20%);
    overflow-y: auto;
    max-height: 17em;
  }
  .login-modal-div .tt-suggestion {
    padding: 10px 5px;
    font-size: 15px;
    line-height: 1.42857143;
    cursor: pointer;
  }

  .login-modal-div .left{
    float:none !important;
  }

  .login-modal-div input[type="checkbox"]:not(:checked), .login-modal-div input[type="checkbox"]:checked{
    position: initial;
    opacity: unset;
    pointer-events: all;
  }

</style>

<div class="spinner-loading-overlay"></div>
<div class="login-modal-div">
  <div class="modal-content">
    <div class="close-div"><span class="close">×</span></div>
    <div class="white-bg center modal-header">
      <div class="login-register-div">
        <input id="tab1" type="radio" name="tabs" checked="checked">
        <label class="tab-label" for="tab1">Sign In</label>
      
        <input id="tab2" type="radio" name="tabs">
        <label class="tab-label" for="tab2">Sign Up</label>

        <section id="content1">
          <form method="POST" class="login-form" id="Login">
            <input type="hidden" name="reqType" value="Login">
            <div class="modal-form-group">
              <div class="extra"></div>
            </div>
            <div class="modal-form-group">
              <i class="input-icon material-icons">account_circle</i>
              <input name="user" id="luser" required="required" type="text" class="modal-form-input" placeholder="Username or email">
            </div>
            <div class="modal-form-group">
              <i class="input-icon material-icons">lock</i>
              <input name="pass" id="password" type="password" required="required" class="modal-form-input" placeholder="Password">
            </div>
            <div class="modal-form-group left">
              <input name="rem" type="hidden" value="false">
              <input name="to" type="hidden" value="https://auth.geeksforgeeks.org/loginModal.php">
              <input name="rem" type="checkbox" checked="checked">
              <label class="modal-form-label" for="remember">Remember me</label>
              <a class="pull-right forgot-link">Forgot Password</a>
            </div>
            <div class="modal-form-group left" style="display: none;">
              <center><div id="loginCaptcha"><div style="width: 304px; height: 78px;"><div><iframe title="reCAPTCHA" width="304" height="78" role="presentation" name="a-8bmtlgtd23fq" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/anchor.htm"></iframe></div><textarea id="g-recaptcha-response-1" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div></center>
            </div>
            <button class="btn btn-green signin-button" type="submit">Sign In</button>
          </form>
        </section>
        <section id="content2">
          <form method="POST" class="login-form" id="Register">
            <input type="hidden" name="reqType" value="Register">
            <div class="modal-form-group">
              <div class="extra"></div>
            </div>
            <!-- <div class="modal-form-group">
              <i class="input-icon material-icons">account_circle</i>
              <input name="user" id="reg-user" type="text" required="required" class="modal-form-input" placeholder="Username">
            </div> -->
            <div class="modal-form-group">
              <i class="input-icon material-icons">email</i>
              <input name="email" id="email" type="email" required="required" class="modal-form-input" placeholder="E-mail">
            </div>
            <div class="modal-form-group">
              <i class="input-icon material-icons">lock</i>
              <input name="pass" id="reg-password" type="password" required="required" class="modal-form-input" placeholder="Password">
            </div>
            <div class="modal-form-group">
              <i class="input-icon material-icons">business</i>
              <span class="twitter-typeahead" style="position: relative; display: inline-block;"><input autocomplete="off" type="text" class="modal-form-input typeahead institute tt-hint" style="position: absolute; top: 0px; left: 0px; border-color: transparent; box-shadow: none; opacity: 1; background: rgb(255, 255, 255);" readonly="readonly" spellcheck="false" tabindex="-1" dir="ltr"><input name="institute" id="organization" autocomplete="off" required="required" type="text" class="modal-form-input typeahead institute tt-input" placeholder="Institution/Organization" spellcheck="false" dir="auto" style="position: relative; vertical-align: top; background-color: transparent;" aria-activedescendant="" aria-owns="organization_listbox" role="combobox" aria-readonly="true" aria-autocomplete="list"><span role="status" aria-live="polite" style="position: absolute; padding: 0px; border: 0px; height: 1px; width: 1px; margin-bottom: -1px; margin-right: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap;"></span><pre aria-hidden="true" style="position: absolute; visibility: hidden; white-space: pre; font-family: &quot;RobotoDraft&quot;, &quot;Roboto&quot;, &quot;Helvetica Neue, Helvetica, Arial&quot;, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 500; word-spacing: 0px; letter-spacing: 0px; text-indent: 0px; text-rendering: optimizelegibility; text-transform: none;"></pre><div role="listbox" class="tt-menu" style="position: absolute; top: 100%; left: 0px; z-index: 100; display: none;"><div role="presentation" class="tt-dataset tt-dataset-0"></div></div></span>
            </div>
            <div class="modal-form-group">
              <center><div id="registerCaptcha"><div style="width: 304px; height: 78px;"><div><iframe title="reCAPTCHA" width="304" height="78" role="presentation" name="a-hmcgnwly6nnf" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/anchor_002.htm"></iframe></div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div></center>
            </div>
            <input name="to" type="hidden" value="https://auth.geeksforgeeks.org/loginModal.php">
            <button class="btn btn-green signup-button" type="submit">Sign Up</button>
          </form>
        </section>
        <div class="social-signin-div">
          <div class="social-divider">
            <span>or</span>
          </div>
          <div class="google-div social-div pull-left">
            <a id="glogin" href="javascript:void(0)" class="btn btn-social btn-google">
              <span class="fa fa-google"></span>Google
            </a>
          </div>
          <div class="facebook-div social-div">
            <a id="fblogin" href="javascript:void(0)" class="btn btn-social btn-facebook">
              <span class="fa fa-facebook"></span>Facebook
            </a>  
          </div>
          <p></p>
          <div class="linkedin-div social-div pull-left">
            <a id="inlogin" class="btn btn-social btn-linkedin">
                <span class="fa fa-linkedin"></span>LinkedIn
            </a>
          </div>
          <div class="github-div social-div pull-left">
            <a id="gitlogin" class="btn btn-social btn-github">
                <span class="fa fa-github"></span>GitHub
            </a>
          </div>
          <div style="padding: 10px 0px;font-size: 14px;font-weight: 500;padding-top: 20px;"><a href="https://www.geeksforgeeks.org/why-create-an-account-on-geeksforgeeks/" style="color: #0f9d58;" target="_blank">Why Create an Account?</a></div>
          <div class="tnc-div">
              By creating this account, you agree to our <a href="https://www.geeksforgeeks.org/privacy-policy/" target="_blank">Privacy Policy</a> &amp; <a href="https://www.geeksforgeeks.org/cookie-policy/" target="_blank">Cookie Policy</a>.
          </div>
        </div>
      </div>
      <div class="forgot-div">
        <form class="login-form" id="Forgot">
          <input type="hidden" name="reqType" value="Forgot">
          <div class="modal-form-group">
            <div class="extra"></div>
          </div>
          <div class="modal-form-group">
            <p class="left">Please enter your email address or userHandle.</p>
          </div>
          <div class="modal-form-group">
            <i class="input-icon material-icons">account_circle</i>
            <input name="user" id="fuser" type="text" class="modal-form-input" placeholder="Username/Email">
          </div>
          <div class="modal-form-group">
            <center><div id="forgotCaptcha"><div style="width: 304px; height: 78px;"><div><iframe title="reCAPTCHA" width="304" height="78" role="presentation" name="a-c3u0ug5b7chq" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/anchor_003.htm"></iframe></div><textarea id="g-recaptcha-response-2" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;"></iframe></div></center>
          </div>
          <div class="modal-form-group left">
            <a class="login-link">Back to Login</a>
          </div>
          <button class="btn btn-green center reset-button" type="submit">Reset Password</button>
        </form> 
      </div>
    </div>
  </div>
</div>

<script>

    // set csrf token for login
    (function(){
        $.ajax({
            url: 'https://auth.geeksforgeeks.org/setLoginToken.php',
            type: 'POST',
            xhrFields: {
                 withCredentials: true
            },
            success: function(data){
            },
            error: function(data){
                console.log(data);
            }
        });
    })();

  $('#loginCaptcha').closest('.modal-form-group').hide();

  var redirectUrl = $('#Login').find('input[name=to]').val();

  // pop up modal when button clicks.
  $('body').on('click', '.login-modal-btn', function(e){
    e.preventDefault();
    var href = window.location.href;
    if($(this).prop("tagName") == "A"){
        href = $(this).attr('href');
    }
    else if($(this).prop("tagName") == "FORM"){
        href = $(this).attr('action');
    }
    $('.login-modal-div').find('input[name=to]').val(href);
    $('.login-modal-div').fadeIn('fast');
    redirectUrl = href;
  });


  //google captch initialization for register/forgot section.
  var captchaSiteKey = '6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa';
  var forgotWidgetId;
  var registerWidgetId;
  var loginWidgetId;
  var onloadCallback = function() {
      // Renders the HTML element with id 'example1' as a reCAPTCHA widget.
      // The id of the reCAPTCHA widget is assigned to 'widgetId1'.
      registerWidgetId = grecaptcha.render('registerCaptcha', {
        'sitekey' : captchaSiteKey,
      });
      loginWidgetId = grecaptcha.render('loginCaptcha', {
        'sitekey' : captchaSiteKey,
      });
      forgotWidgetId = grecaptcha.render('forgotCaptcha', {
        'sitekey' : captchaSiteKey
      });
  };

  // check required field.
  $('body').on('blur', 'input[required=required]', function(){
    var val = $(this).val();
    $('.error-focus').removeClass('error-focus');
    $('div.input-error').remove();
    if(val == "" || val == null || val == undefined){
      $(this).closest('.modal-form-group').append('<div class="input-error">Field can not be empty.</div>');
      $(this).addClass('error-focus');
      $(this).focus();
    }
  });

  //remove error message if input have some words.
  $('body').on('keydown', 'input[required=required]', function(){
    var val = $(this).val();
    if(val != "" || val != null || val != undefined){
      $(this).removeClass('error-focus');
      $(this).closest('.modal-form-group').find('.input-error').remove();
    }
  });

  // suggest organization.
  var instituteListBlood = new Bloodhound({
  initialize: false,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    sufficient: 5,
    prefetch: {  //this endpoint will hit when we will sign up again in the profile page 
      url: 'https://utilapi.geeksforgeeks.org/api/institutes/all/'
    },
    remote: {
      url: 'https://utilapi.geeksforgeeks.org/api/institutes/%QUERY/all/',
      wildcard: '%QUERY',
      filter: function (data) {
        instituteListBlood.add(data);
        return data;
      }
    }
  });

  $(document).ready(function () {
    instituteListBlood.clearPrefetchCache();
    instituteListBlood.initialize();
    $('input.typeahead.institute').typeahead({
      minLength: 2,
      dynamic: false,
      highlight: true,
      cache: "sessionStorage",
      searchOnfocus: true,
      offset: true,
      blurOnTab: true
    }, {
      displaykey: 'value',
      limit: 15,
      source: instituteListBlood.ttAdapter(),
      accent: true,
      templates: {
      empty: [
              ''
              ].join('\n')
      }
    });
  });

  $(document).ready(function(){

    // dismiss modal when click on close icon.
    $('body').on('click', '.close', function(){
      $(this).closest('.login-modal-div').fadeOut('fast');
    });

    //dismiss modal when esc key pressed.
    $(document).keypress(function(e) { 
        if (e.keyCode == 27) { 
            $(".login-modal-div").fadeOut('fast');
        } 
    });

    //dismiss modal when click outside of it.
    $('body').on('click', '.login-modal-div', function(){
        $(".login-modal-div").fadeOut('fast');
    });

    $('body').on('click', '.login-modal-div .modal-content', function(e){
        e.stopPropagation();
    });

    //toggle between forgot div and login div.
    $('body').on('click', '.login-link, .forgot-link', function(){
      if($(this).hasClass('login-link')){
        $('.forgot-div').slideUp();
        $('.login-register-div').slideDown();
      }
      else{
        $('.login-register-div').slideUp();
        $('.forgot-div').slideDown();
      }
    });

    // redirect function.
    function redirect(where) {
      if( where == 'to' ) {
        window.location.href = to;
      } else if( where == 'reset' ) {
        q2to3();
        $("#ruser").val($("#fuser").val());
      }
      else{
        if(window.location.href == where){
            window.location.reload(true);
        }
        else{
            window.location.href = where;
        }
      }
    }

    // event on submit either login, register or forgot form.
    $(".login-form").submit( function(e) {
      e.preventDefault();
      this1 = $(this);
      $('.spinner-loading-overlay').show();
      this1.find(".extra").empty();
      this1.find('input[type=submit]').attr('disabled', true);
      var browserInfo = fetchBrowserInfo();

      $.ajax({
        type: "POST",
        url: 'https://auth.geeksforgeeks.org/auth.php',
        data: $(this).serialize()+"&browserInfo="+JSON.stringify(browserInfo),
        xhrFields: {
          withCredentials: true
        },
        dataType: "json",
        success: function( data ) {
          this1.find('input[type=submit]').attr('disabled', false);
          if( data.redirect ) {
            redirect( data.redirect );
          } else if( data.extra ) {
            $('.spinner-loading-overlay').hide();
            this1.find(".extra").append(data.extra);
            var errorTxt = this1.find(".extra").find('div').text().trim();
            grecaptcha.reset(loginWidgetId);
            if(errorTxt == "Captcha validation needed" && this1.attr('id') == "Login"){
              if(!$('#loginCaptcha').closest('.modal-form-group').find('input[name=recaptchaShow]').length){
                $('#loginCaptcha').closest('.modal-form-group').append('<input name="recaptchaShow" type="hidden" value="1">');
              }
              $('#loginCaptcha').closest('.modal-form-group').show();
            }
          }
        },
        error: function(jqXHR, exception, errorThrown) {
          this1.find('input[type=submit]').attr('disabled', false);
          $('.spinner-loading-overlay').hide();
          console.log( "An error occurred" );
        },
        complete: function() {
          this1.find('input[type=submit]').attr('disabled', false);
          if(this1.attr('id') == "Forgot"){
            grecaptcha.reset(forgotWidgetId);
          }
          else{
            grecaptcha.reset(registerWidgetId);
          }
        }
      });
      return false;
    });

    //prevent to type space bar in register password field.
    $('body').on('keydown', 'input[name=pass]', function(e){
        if($(this).closest('form').find('input[name=reqType]').length && $(this).closest('form').find('input[name=reqType]').val() == "Register"){
            return e.which !== 32;
        }
    });


  // Facebook login
    $('#fblogin').click(function(e){
        e.preventDefault();
        var w = 600, h = 350, left = screen.width / 2 - w / 2, top = screen.height / 2 - h / 2;
        var remember = $('#Login').find('input[name=rem]').is(":checked");
        var redirect = $('#Login').find('input[name=to]').val();
        var browserInfo = JSON.stringify(fetchBrowserInfo());
        window.open('https://auth.geeksforgeeks.org//fb-login.php?to='+encodeURIComponent(redirect)+'&rem='+remember+'&browserInfo='+browserInfo,'_self','toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width='+w+', height='+h+',top='+top+', left='+left);
      }); 

    // linkedin login
    $('#inlogin').click(function(e){
        e.preventDefault();
        var w = 600, h = 350, left = screen.width / 2 - w / 2, top = screen.height / 2 - h / 2;
        var remember = $('#Login').find('input[name=rem]').is(":checked");
        var redirect = $('#Login').find('input[name=to]').val();
        var browserInfo = JSON.stringify(fetchBrowserInfo());
        window.open('https://auth.geeksforgeeks.org//linkedin-login.php?to='+encodeURIComponent(redirect)+'&rem='+remember+'&browserInfo='+browserInfo,'_self','toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width='+w+', height='+h+',top='+top+', left='+left);
      });

    // github login
    $('#gitlogin').click(function(e){
        e.preventDefault();
        var w = 600, h = 350, left = screen.width / 2 - w / 2, top = screen.height / 2 - h / 2;
        var remember = $('#Login').find('input[name=rem]').is(":checked");
        var redirect = $('#Login').find('input[name=to]').val();
        var browserInfo = JSON.stringify(fetchBrowserInfo());
        window.open('https://auth.geeksforgeeks.org//github-login.php?to='+encodeURIComponent(redirect)+'&rem='+remember+'&browserInfo='+browserInfo,'_self','toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width='+w+', height='+h+',top='+top+', left='+left);
      });

    $('#glogin').click(function(e){
        e.preventDefault();
        var remember = $('#Login').find('input[name=rem]').is(":checked");
        var redirect = $('#Login').find('input[name=to]').val();
        var browserInfo = JSON.stringify(fetchBrowserInfo());
        window.location = "https://auth.geeksforgeeks.org/googleLogin.php?redirect="+encodeURIComponent(redirect)+"&remember="+remember+"&browserInfo="+browserInfo;  
      });
  });

  function fetchBrowserInfo(){
    var browserInfo = {};
    browserInfo.appName = navigator.appName;
    browserInfo.appCodeName = navigator.appCodeName;
    browserInfo.cookieEnable = navigator.cookieEnabled;
    browserInfo.prodName = navigator.product;
    browserInfo.appVersion = navigator.appVersion;
    browserInfo.appOs = navigator.platform;
    browserInfo.appLang = navigator.language;
    browserInfo.vendorName = navigator.vendor;
    browserInfo.loginDomain = "auth";

    return browserInfo;
  }
</script>
<script src="medium_files/dropzone.js"></script>	
<script type="text/javascript">
var language = 'Python';</script>
<style>
    .fullScreen {
      position: relative;
    }

    .split {
      float: left;
    }

	.mainRightDiv {
		display: inline-block;
		width: 90%;
		margin-left: -45px;
	}

	@media (max-width: 768px) {
		.mainRightDiv{
			margin-left: 15px;
		}
	}
</style>



<div class="fullScreen" style="display:none">
      <div class="leftDiv split" style="width:56%;padding:0px 20px;outline: 10px solid #f1f1f1;"></div>
      <div class="rightDiv split" style="overflow-y:auto;width:44%;padding:10px 20px 100px 35px;overflow-x:hidden"></div>
  </div>

<div class="container-fluid" style="margin-bottom:15px;">
	<div class="row screen">
		<div class="col-sm-9 col-xs-12 normalScreen">
		    <div class="mainleftDiv">
			 		    	  <div class="col-sm-offset-1 col-sm-11 col-xs-12 text-center" style="margin-bottom:8px;">
				<div class="row">
									</div>
			  </div>
			  			  <div class="col-sm-1 col-xs-12">
				<div class="row form-group btn-group vertBtns" role="group">
					<a href="https://ide.geeksforgeeks.org/online-c-compiler" target="_blank" l="C" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C</a>
					<a href="https://ide.geeksforgeeks.org/online-cpp-compiler" target="_blank" data-toggle="tooltip" title="C++11 supported" l="Cpp" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C++</a>
					<a href="https://ide.geeksforgeeks.org/online-cpp14-compiler" target="_blank" l="Cpp14" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C++14</a>
					<a href="https://ide.geeksforgeeks.org/online-csharp-compiler" target="_blank" l="Csharp" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C#</a>
					<a href="https://ide.geeksforgeeks.org/online-java-compiler" target="_blank" l="Java" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Java</a>
					<a href="https://ide.geeksforgeeks.org/online-perl-compiler" target="_blank" l="Perl" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Perl</a>
					<a href="https://ide.geeksforgeeks.org/online-php-compiler" target="_blank" l="Php" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">PHP</a>
											<a l="Python" class="lang btn btn-default form-control" style="pointer-events: none; background-color: rgb(57, 181, 74); color: rgb(0, 0, 0);">Python</a>
										<a href="https://ide.geeksforgeeks.org/online-python3-compiler" target="_blank" l="Python3" class="lang btn btn-default form-control" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Python 3</a>
					<a href="https://ide.geeksforgeeks.org/online-scala-compiler" target="_blank" l="Scala" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Scala</a>
					<a href="https://ide.geeksforgeeks.org/online-swift-compiler" target="_blank" l="Swift" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Swift</a>
					<a href="https://ide.geeksforgeeks.org/online-rust-compiler" target="_blank" l="Rust" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Rust</a>
					<a href="https://ide.geeksforgeeks.org/online-golang-compiler" target="_blank" l="Golang" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Golang</a>
					<a href="https://ide.geeksforgeeks.org/online-r-compiler" target="_blank" l="R" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">R</a>
					<a href="https://ide.geeksforgeeks.org/online-nodejs-compiler" target="_blank" l="Nodejs" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Node JS</a>
					<a href="https://ide.geeksforgeeks.org/online-html-editor" target="_blank" class="btn btn-default form-control" style="border-radius: 0;">HTML &amp; JS</a>
				</div>
				<div class="row form-group vertBtns">
					<button id="saveFile" data-toggle="tooltip" title="Download Code" class="savebtn btn btn-default form-control">
						<span class="glyphicon glyphicon-cloud-download"></span>
					</button>
	     			<form role="form" id="uploadForm" data-toggle="tooltip" title="Upload Code" class="btn btn-default form-control dropzone dz-clickable" action=" " enctype="multipart/form-data">
	       			    <span class="glyphicon glyphicon-cloud-upload"></span><input type="hidden" name="file">
	     			<div class="dz-default dz-message"><span></span></div></form>
				</div>
			</div>
			<div id="codeBlock" class="col-sm-11 col-xs-12" style="padding-left:40px">
				<div class="row">
			                <div class="btn btn-default tab col-sm-2 col-xs-4" style="border-width: 1px 1px 2px; border-style: solid; border-color: rgb(173, 173, 173); background-color: rgb(255, 255, 255);" id="tab0" name="0"> <div class="text">Python</div> <button class="btn btn-default btn-sm closeTab" name="0" style="background-color: rgb(255, 255, 255); display: block;"><i class="glyphicon glyphicon-minus-sign"></i></button>  </div><div class="btn btn-default tab col-sm-2 col-xs-4" style="border-width: 1.5px 1.5px medium; border-style: solid solid none; border-color: rgb(173, 173, 173) rgb(173, 173, 173) currentcolor; background-color: rgb(235, 235, 235);" id="tab1" name="1"> <div class="text">Python</div> <button class="btn btn-default btn-sm closeTab" name="1" style="display: block; background-color: rgb(235, 235, 235);"><i class="glyphicon glyphicon-minus-sign"></i></button>  </div><div class="btn btn-default tab col-sm-2 col-xs-4" style="display:none" id="tab2" name="2"> <div class="text">Tab2</div> <button class="btn btn-default btn-sm closeTab" name="2" style="display: block;"><i class="glyphicon glyphicon-minus-sign"></i></button>  </div><div class="btn btn-default tab col-sm-2 col-xs-4" style="display:none" id="tab3" name="3"> <div class="text">Tab3</div> <button class="btn btn-default btn-sm closeTab" name="3" style="display: block;"><i class="glyphicon glyphicon-minus-sign"></i></button>  </div><div class="btn btn-default tab col-sm-2 col-xs-4" style="display:none" id="tab4" name="4"> <div class="text">Tab4</div> <button class="btn btn-default btn-sm closeTab" name="4" style="display: block;"><i class="glyphicon glyphicon-minus-sign"></i></button>  </div>	        		        <button class="btn btn-default" id="addTab"><i class="glyphicon glyphicon-plus-sign"></i></button>

					<div class="ideIcons">
						<a id="themeLight" class="themeLight" data-toggle="tooltip" title="Switch to Light Mode" href="javascript:void(0)" style="display:none">
							<img src="medium_files/lightmodelarge-1673520978.png">
						</a>
						<a id="themeDark" class="themeDark" data-toggle="tooltip" title="Switch to Dark Mode" href="javascript:void(0)" style="display: unset;">
							<img src="medium_files/noun-night-mode-2448868-1673515243.svg">
						</a>
						<a id="shortkeys" data-toggle="tooltip" title="Shortcuts" href="javascript:void(0)">
							<img src="medium_files/ShortcutIconSmall-1673434520.png">
						</a>
						<a id="reset1" data-toggle="tooltip" title="Reset" href="javascript:void(0)">
							<img src="medium_files/Refresh-1673515318.svg">
						</a>
						<a id="btnEditor" data-toggle="tooltip" title="Copy" href="javascript:void(0)">
							<img src="medium_files/CopyIconSmall-1673434756.png">
						</a> 
						<a id="splitScreen" data-toggle="tooltip" title="Split Screen" href="javascript:void(0)">
							<span class="glyphicon glyphicon-resize-full"></span>
						</a>
						<a id="full" data-toggle="tooltip" title="Fullscreen" href="javascript:void(0)">
							<img src="medium_files/maximize-1673520675.svg">
						</a>
					</div>
	            		</div>
				<div class="row">
					<form role="form" class="dropzone clickable-dz dz-clickable" action=" " enctype="multipart/form-data">
						<div class="form-group">
							<div class="editorBlock" style="height:500px;">
								<pre id="editor" class=" ace_editor ace-chrome" style="font-size: 12pt;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="none" spellcheck="false" style="opacity: 0; font-size: 1px; top: 19px; height: 1px; width: 1px; left: 55px;">

</textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 51px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1000000px; top: 0px; left: 0px; width: 51px;"><div class="ace_gutter-cell ace_gutter-active-line " style="height: 19px; top: 0px;">1<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 19px;">2<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 38px;">3<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 57px;">4<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 76px;">5<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 95px;">6<span class="ace_fold-widget ace_start ace_open" style="height: 19px; display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 114px;">7<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 133px;">8<span style="display: none; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 152px;">9<span style="display: none; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 171px;">10<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 190px;">11<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 209px;">12<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 228px;">13<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 247px;">14<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 266px;">15<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 285px;">16<span style="display: none; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 304px;">17<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 323px;">18<span style="display: none; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 342px;">19<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 361px;">20<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 380px;">21<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 399px;">22<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 418px;">23<span class="ace_fold-widget ace_start ace_open" style="height: 19px; display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 437px;">24<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 456px;">25<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 475px;">26<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 494px;">27<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 513px;">28<span class="ace_fold-widget ace_start ace_open" style="height: 19px; display: inline-block;"></span></div></div></div><div class="ace_scroller" style="left: 50.6px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 834.4px; height: 536px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 708px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div style="height: 19px; top: 0px; left: 0px; right: 0px;" class="ace_active-line"></div></div><div class="ace_layer ace_text-layer" style="height: 1000000px; margin: 0px 4px; top: 0px; left: 0px;"><div style="height: 19px; top: 0px;" class="ace_line"><span class="ace_keyword">def</span> <span class="ace_identifier">majority_elements</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">nums</span><span class="ace_paren ace_rparen">)</span>:</div><div style="height: 19px; top: 19px;" class="ace_line">    <span class="ace_keyword">if</span> <span class="ace_keyword">not</span> <span class="ace_identifier">nums</span>:</div><div style="height: 19px; top: 38px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_paren ace_lparen">[</span><span class="ace_paren ace_rparen">]</span></div><div style="height: 19px; top: 57px;" class="ace_line"></div><div style="height: 19px; top: 76px;" class="ace_line">    <span class="ace_comment"># Initialize candidates and their counters</span></div><div style="height: 19px; top: 95px;" class="ace_line">    <span class="ace_identifier">candidate1</span>, <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_language">None</span>, <span class="ace_constant ace_numeric">0</span></div><div style="height: 19px; top: 114px;" class="ace_line">    <span class="ace_identifier">candidate2</span>, <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_language">None</span>, <span class="ace_constant ace_numeric">0</span></div><div style="height: 19px; top: 133px;" class="ace_line"></div><div style="height: 19px; top: 152px;" class="ace_line">    <span class="ace_comment"># Find candidates using Boyer-Moore Majority Vote algorithm</span></div><div style="height: 19px; top: 171px;" class="ace_line">    <span class="ace_keyword">for</span> <span class="ace_identifier">num</span> <span class="ace_keyword">in</span> <span class="ace_identifier">nums</span>:</div><div style="height: 19px; top: 190px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span> <span class="ace_identifier">num</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_identifier">candidate1</span>:</div><div style="height: 19px; top: 209px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 228px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">elif</span> <span class="ace_identifier">num</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_identifier">candidate2</span>:</div><div style="height: 19px; top: 247px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 266px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">elif</span> <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_constant ace_numeric">0</span>:</div><div style="height: 19px; top: 285px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">candidate1</span>, <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">num</span>, <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 304px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">elif</span> <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_constant ace_numeric">0</span>:</div><div style="height: 19px; top: 323px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">candidate2</span>, <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">num</span>, <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 342px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">else</span>:</div><div style="height: 19px; top: 361px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">-=</span> <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 380px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">-=</span> <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 399px;" class="ace_line"></div><div style="height: 19px; top: 418px;" class="ace_line">    <span class="ace_comment"># Count occurrences of candidates</span></div><div style="height: 19px; top: 437px;" class="ace_line">    <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">count2</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_numeric">0</span></div><div style="height: 19px; top: 456px;" class="ace_line">    <span class="ace_keyword">for</span> <span class="ace_identifier">num</span> <span class="ace_keyword">in</span> <span class="ace_identifier">nums</span>:</div><div style="height: 19px; top: 475px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span> <span class="ace_identifier">num</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_identifier">candidate1</span>:</div><div style="height: 19px; top: 494px;" class="ace_line"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">count1</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_constant ace_numeric">1</span></div><div style="height: 19px; top: 513px;" class="ace_line"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">elif</span> <span class="ace_identifier">num</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_identifier">candidate2</span>:</div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="animation-duration: 1000ms; display: block; top: 0px; left: 4px; width: 9px; height: 19px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="width: 20px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 20px; height: 836px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px; left: 50.6px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 20px; width: 843px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-size-adjust: inherit; font-kerning: inherit; font-optical-sizing: inherit; font-language-override: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></pre>
							</div>
						</div>
					<div class="dz-default dz-message"><span></span></div></form>
				</div>
			   </div>
			</div>
			<div class="mainRightDiv">
				<div class="row">
					<div class="col-sm-offset-1 col-sm-11 col-xs-12 inputRunRow">
						<div class="row inputRunDiv">
							<div id="inputDivClass" class="form-group col-sm-7 col-xs-12 inputDiv">
								<textarea id="input" placeholder="Input Goes Here.." maxlength="10000" class="gb wf form-control input" style="height:200px;"></textarea>
								<button class="btn btn-default btnInput" type="button">Copy</button>
							</div>
							<div class="sbt-group col-sm-4 buttonDiv" role="group">
								<button id="run" class="sbt btn btn-default" title="Run Program(Ctrl+Enter)"><span class="glyphicon glyphicon-chevron-right"></span> <b>Run</b></button>
											                				<button class="sbt btn btn-default login-modal-btn" title="Generates URL as well for Code Sharing">
					        	            	<span class="glyphicon glyphicon-chevron-right"></span>
		        			        			<b>Run+URL (Generates URL as well)</b>
					            		</button>		
													
			                   		</div>
						</div>
					</div>
				</div>
				<br>
				<div class="row">
						<div class="col-sm-11 col-xs-12">
							<div class="lang-group btn-group col-sm-12" role="group">
								<a href="https://ide.geeksforgeeks.org/online-c-compiler" target="_blank" l="C" class="lang btn btn-default" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C</a>
								<a href="https://ide.geeksforgeeks.org/online-cpp-compiler" target="_blank" data-toggle="tooltip" title="C++11 supported" l="Cpp" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C++</a>
								<a href="https://ide.geeksforgeeks.org/online-cpp14-compiler" target="_blank" l="Cpp14" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C++14</a>
								<a href="https://ide.geeksforgeeks.org/online-csharp-compiler" target="_blank" l="Csharp" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">C#</a>
								<a href="https://ide.geeksforgeeks.org/online-java-compiler" target="_blank" l="Java" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Java</a>
								<a href="https://ide.geeksforgeeks.org/online-perl-compiler" target="_blank" l="Perl" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Perl</a>
								<a href="https://ide.geeksforgeeks.org/online-php-compiler" target="_blank" l="Php" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">PHP</a>
																	<a l="Python" class="lang btn btn-default" style="pointer-events: none; background-color: rgb(57, 181, 74); color: rgb(0, 0, 0);">Python</a>
																<a href="https://ide.geeksforgeeks.org/online-python3-compiler" target="_blank" l="Python3" class="lang btn btn-default" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Python 3</a>
								<a href="https://ide.geeksforgeeks.org/online-scala-compiler" target="_blank" l="Scala" class="lang btn btn-default" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Scala</a>
								<a href="https://ide.geeksforgeeks.org/online-swift-compiler" target="_blank" l="Swift" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Swift</a>
								<a href="https://ide.geeksforgeeks.org/online-rust-compiler" target="_blank" l="Rust" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Rust</a>
								<a href="https://ide.geeksforgeeks.org/online-golang-compiler" target="_blank" l="Golang" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Golang</a>
								<a href="https://ide.geeksforgeeks.org/online-r-compiler" target="_blank" l="R" class="lang btn btn-default form-control" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">R</a>
								<a href="https://ide.geeksforgeeks.org/online-nodejs-compiler" target="_blank" l="Nodejs" class="lang btn btn-default" style="border-radius: 0px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">Node JS</a>
								<a href="https://ide.geeksforgeeks.org/online-html-editor" target="_blank" class="btn btn-default" style="border-radius: 0;">HTML &amp; JS</a>
							</div>
						</div>
				</div>
				<div class="row">
					<div class="col-sm-11 col-xs-12">
						<div class="form-group lang-group row">
							<div class="col-xs-6">
								<button id="saveFileSmallScreen" data-toggle="tooltip" title="Download Code" class="savebtn btn btn-default form-control">
									<span class="glyphicon glyphicon-cloud-download"></span>
								</button>
							</div>
							<div class="col-xs-6">
								<form role="form" id="uploadFormSmallScreen" data-toggle="tooltip" title="Upload Code" class="dropzone btn btn-default form-control dz-clickable" action=" " enctype="multipart/form-data">
					       			    <span class="glyphicon glyphicon-cloud-upload"></span><input type="hidden" name="file">
			     					<div class="dz-default dz-message"><span></span></div></form>	
							</div>
						</div>
					</div>
				</div>
				<div class="col-sm-offset-1 col-sm-11 col-xs-12">
					<div style="display:none" class="row err">
						<div class="alert alert-danger">
							Oops! Something went wrong. You are probably allocating too much memory or producing too much output.
						</div>
					</div>
											<div class="row url" style="display:none">
		        			        <h3>Generated URL:<button class="btn btn-default btnLink pull-right">Copy</button></h3>
					                    <pre class="gb wf" id="preLink"></pre>
		                     		</div>
																<div style="display:none;" class="row cmp">
							<h3>Compile Errors : </h3>
								<pre class="gb wf" style="max-height:100px;overflow-y:scroll"></pre>
						</div>
					
				
						        	                        <div style="display:none;" class="row war">
	                                        <h3>Warnings: </h3>
	                	                        <pre class="gb wf" style="max-height:100px;overflow-y:scroll"></pre>
	                        	        </div>
		                        				

					<div style="display:none" class="row stats">
						<div class="col-sm-6" style="display:inline">
							<h4 style="display:inline;">Time(sec) : </h4>
							<h4 class="time" style="display:inline;"> 0.25 </h4>
						</div>
						<div class="col-sm-6" style="display:inline">
                                                        <h4 style="display:inline;">Memory(MB) : </h4>
                                                        <h4 class="memory" style="display:inline;"> 0.25 </h4>
                                                </div>
					</div>



													<div style="" class="row rnt">
								<h3>Runtime Errors: </h3>
								<pre class="gb wf" style="max-height:100px;overflow-y:scroll">Hangup (SIGHUP)
Traceback (most recent call last):
  File "Solution.py", line 13, in &lt;module&gt;
    s = input("Enter a string: ")
EOFError: EOF when reading a line
</pre>
							</div>
																		<div style="" class="row out">
							<h3>Output: <button class="btn btn-default btnOutput pull-right">Copy</button> </h3>
							<pre class="gb wf" id="preOutput">Enter a string: </pre>
						</div>
									</div>
				</div>
			<div class="col-sm-offset-1 col-sm-11 col-xs-12 hidden-xs text-center">
				<div class="row">
									</div>
			</div>
		</div>
		<div class="col-sm-3 col-xs-12">
			<div style="margin-bottom: 10px; margin-top: 9px;">
				<a href="https://ide.geeksforgeeks.org/report.php" class="btn btn-success form-control" type="button" style="background-color:#4CB96B;font-size: 18px;border-radius: 0;">Report Bug</a>
			</div>
			<div id="div-ide-img" class="imgDiv"><a href="https://practice.geeksforgeeks.org/courses/Python-Foundation?utm_source=ide&amp;utm_medium=course_python_programming&amp;utm_campaign=inbound_promotions" target="_blank" style="position: relative;"><img class="img-responsive" src="medium_files/Python-1672989593.gif"></a></div>
						<br>
					</div>
	</div>
</div>
<!--Comment Modal -->
<div class="modal fade" id="shortkeysModal" role="success">
    <div class="modal-dialog ">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">×</button>
          <h4 class="modal-title">Keyboard shortcuts for editor</h4>
        </div>
        <div class="modal-body">
			<table class="shortcutTable" border="1px solid #dfe2e5">
				<thead>
					<tr><th align="left">Action</th>
					<th align="left">Windows/Linux</th>
					<th align="left">Mac</th>
				</tr></thead>
				<tbody>
					<tr>
						<td>Run Program</td>
						<td>Ctrl-Enter</td>
						<td>Command-Enter</td>
					</tr>
					<tr>
						<td>Find</td>
						<td>Ctrl-F</td>
						<td>Command-F</td>
					</tr>
					<tr>
						<td>Replace</td>
						<td>Ctrl-H</td>
						<td>Command-Option-F</td>
					</tr>
					<tr>
						<td>Remove line</td>
						<td>Ctrl-D</td>
						<td>Command-D</td>
					</tr>
					<tr>
						<td>Move lines down</td>
						<td>Alt-Down</td>
						<td>Option-Down</td>
					</tr>
					<tr>
						<td>Move lines up</td>
						<td>Alt-UP</td>
						<td>Option-Up</td>
					</tr>
				</tbody>
			</table><br>
			<div>
				For more shortcuts you can visit the following page:
				<a href="https://github.com/ajaxorg/ace/wiki/Default-Keyboard-Shortcuts" target="_blank">Ace editor shortcuts</a>
			</div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
</div>
<style>
	table.shortcutTable	td,th {
		padding: 10px !important;
	}
	.courseCard {
		background-color: #fff;
		-webkit-box-shadow: 0px 0px 25px 0 rgba(0,0,0,.18);
		-moz-box-shadow: 0px 0px 25px 0 rgba(0,0,0,.18);
		box-shadow: 0px 0px 25px 0 rgba(0,0,0,.18);
		font-family: 'Nunito', sans-serif;
		border-radius: 3px;
		margin-bottom: 15px;
		margin-top: 20px;
		border-radius: .80rem;
		padding-bottom: 21px;
	}
	
	.ace_content {
		height: 100% !important;
	}
</style>

    <footer class="gfg-footer" id="gfg-footer">
        <div class="footer-wrapper">
            <div class="footer-wrapper_branding">
                <a href="https://www.geeksforgeeks.org/">
                    <div class="footer-wrapper_branding-logo pre-dark"></div>
                </a>
                <div class="footer-wrapper_branding-address">
                    <i class="material-icons">room</i>
                    <span>
                        A-143, 9th Floor, Sovereign Corporate Tower,<br>
                        Sector-136, Noida, Uttar Pradesh - 201305
                    </span>
                </div>
                <div class="footer-wrapper_branding-email">
                    <i class="material-icons">email</i>
                    <a href="mailto:feedback@geeksforgeeks.org">feedback@geeksforgeeks.org</a>
                </div>
                <div class="footer-wrapper_branding-social">
                    <a href="https://www.facebook.com/geeksforgeeks.org/" target="_blank">
                        <div class="facebook"></div>
                    </a>
                    <a href="https://www.instagram.com/geeks_for_geeks/" target="_blank">
                        <div class="instagram"></div>
                    </a>
                    <a href="https://in.linkedin.com/company/geeksforgeeks" target="_blank">
                        <div class="linkedin"></div>
                    </a>
                    <a href="https://twitter.com/geeksforgeeks" target="_blank">
                        <div class="twitter"></div>
                    </a>
                    <a href="https://www.youtube.com/geeksforgeeksvideos" target="_blank">
                        <div class="youtube"></div>
                    </a>
                </div>
            </div>
            <div class="footer-wrapper_links">
                <ul class="footer-wrapper_links-list">
                    <li>Company</li>
                    <li><a href="https://www.geeksforgeeks.org/about/">About Us</a></li>
		    <li><a href="https://www.geeksforgeeks.org/legal/">Legal</a></li>
                    <li><a href="https://www.geeksforgeeks.org/careers/">Careers</a></li>
                    <li><a href="https://www.geeksforgeeks.org/privacy-policy/">Privacy Policy</a></li>
                    <li><a href="https://www.geeksforgeeks.org/about/contact-us/">Contact Us</a></li>
                </ul>
                <ul class="footer-wrapper_links-list">
                    <li>Learn</li>
                    <li><a href="https://www.geeksforgeeks.org/fundamentals-of-algorithms/">Algorithms</a></li>
                    <li><a href="https://www.geeksforgeeks.org/data-structures/">Data Structures</a></li>
                    <li><a href="https://www.geeksforgeeks.org/category/program-output/">Languages</a></li>
                    <li><a href="https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/">CS
                            Subjects</a></li>
                    <li><a href="https://www.youtube.com/geeksforgeeksvideos/">Video Tutorials</a></li>
                </ul>
                <ul class="footer-wrapper_links-list">
                    <li>Practice</li>
                    <li><a href="https://practice.geeksforgeeks.org/courses/">Courses</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/company-tags/">Company-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/topic-tags/">Topic-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/faq.php">How to begin?</a></li>
                </ul>
                <ul class="footer-wrapper_links-list">
                    <li>Contribute</li>
                    
                    <li><a href="https://www.geeksforgeeks.org/contribute/">Write an Article</a></li>
                    <li><a href="https://www.geeksforgeeks.org/write-interview-experience/">Write Interview
                            Experience</a></li>
                    <li><a href="https://www.geeksforgeeks.org/internship/">Internships</a></li>
                    <li><a href="https://www.geeksforgeeks.org/how-to-contribute-videos-to-geeksforgeeks/">Videos</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="footer-strip">
            <div class="copyright">
		<a href="https://www.geeksforgeeks.org/" rel="noopener noreferrer" target="_blank">@GeeksforGeeks, Sanchhaya Education Private Limited</a>
                <span>
			<a href="https://www.geeksforgeeks.org/copyright-information/">, All rights reserved</a>
		</span>
            </div>
            <div class="social-links">

            </div>
        </div>
    </footer>
    <!-- End of footer -->

    <link rel="stylesheet" href="medium_files/jquery-ui.min.css">
    <script async="" type="text/javascript" src="medium_files/jquery-ui.min.js"></script>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async="" src="medium_files/js_003"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());

	gtag('config', 'UA-144087254-1');
    </script>





<div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div style="display: none;">Sign in with Google Dialogue</div><div style="display: none;">Sign in with Google Dialogue</div><div>Run Program(Ctrl+Enter)</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div>Switch to Dark Mode</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div style="display: none;">Shortcuts</div><div style="display: none;">Shortcuts</div><div>Shortcuts</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div style="display: none;">Reset</div><div style="display: none;">Reset</div><div style="display: none;">Reset</div><div>Reset</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div style="display: none;">Copy</div><div style="display: none;">Copy</div><div>Copy</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div style="display: none;">Split Screen</div><div>Split Screen</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"><div>Fullscreen</div></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><input type="file" class="dz-hidden-input" accept=" .cpp , .c , .java , .py , .php , .cs , .scala , .perl " style="visibility: hidden; position: absolute; top: 0px; left: 0px; height: 0px; width: 0px;"><input type="file" class="dz-hidden-input" accept=" .cpp , .c , .java , .py , .php , .cs , .scala , .perl " style="visibility: hidden; position: absolute; top: 0px; left: 0px; height: 0px; width: 0px;"><input type="file" class="dz-hidden-input" accept=" .cpp , .c , .java , .py , .php , .cs , .scala , .perl " style="visibility: hidden; position: absolute; top: 0px; left: 0px; height: 0px; width: 0px;"><div style="background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 3px; position: absolute; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0; visibility: hidden; z-index: 2000000000; left: 0px; top: -10000px;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.05;"></div><div style="border: 11px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -11px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="border: 10px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -10px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="z-index: 2000000000; position: relative;"><iframe title="recaptcha challenge expires in two minutes" style="width: 100%; height: 100%;" name="c-8bmtlgtd23fq" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/bframe_003.htm"></iframe></div></div><div style="background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 3px; position: absolute; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0; visibility: hidden; z-index: 2000000000; left: 0px; top: -10000px;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.05;"></div><div style="border: 11px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -11px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="border: 10px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -10px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="z-index: 2000000000; position: relative;"><iframe title="recaptcha challenge expires in two minutes" style="width: 100%; height: 100%;" name="c-hmcgnwly6nnf" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/bframe_003.htm"></iframe></div></div><div style="background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 3px; position: absolute; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0; visibility: hidden; z-index: 2000000000; left: 0px; top: -10000px;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.05;"></div><div style="border: 11px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -11px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="border: 10px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -10px; z-index: 2000000000;" class="g-recaptcha-bubble-arrow"></div><div style="z-index: 2000000000; position: relative;"><iframe title="recaptcha challenge expires in two minutes" style="width: 100%; height: 100%;" name="c-c3u0ug5b7chq" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="medium_files/bframe_003.htm"></iframe></div></div><iframe style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;" name="googlefcPresent"></iframe><iframe name="__tcfapiLocator" src="medium_files/a.htm" style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;"></iframe><iframe name="__uspapiLocator" src="medium_files/a.htm" style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;"></iframe><iframe name="__gppLocator" src="medium_files/a.htm" style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;"></iframe><iframe name="googlefcInactive" src="medium_files/a.htm" style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;"></iframe><iframe name="googlefcLoaded" src="medium_files/a.htm" style="display: none; width: 0px; height: 0px; border: medium; z-index: -1000; left: -1000px; top: -1000px;"></iframe><script type="text/javascript" src="medium_files/Untitled"></script><script type="text/javascript" src="medium_files/geoip2.js"></script><div role="tooltip" id="ui-id-2" class="ui-tooltip ui-corner-all ui-widget-shadow ui-widget ui-widget-content" style="top: 336px; left: 955px; display: block;"><div class="ui-tooltip-content">Sign in with Google Dialogue</div></div></body></html>