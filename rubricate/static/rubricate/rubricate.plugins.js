!function(e){function t(r){if(n[r])return n[r].exports;var o=n[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,t),o.l=!0,o.exports}var n={};t.m=e,t.c=n,t.i=function(e){return e},t.d=function(e,n,r){t.o(e,n)||Object.defineProperty(e,n,{configurable:!1,enumerable:!0,get:r})},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="",t(t.s=23)}({14:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(16);t.HeaderPlugin=r.default;var o=n(15);t.FilesPlugin=o.default},15:function(e,t,n){"use strict";function r(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var o=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();Object.defineProperty(t,"__esModule",{value:!0});var i=function(){function e(t,n){r(this,e),this._uploads=[],this._options=n,this._defaults=t}return o(e,[{key:"getForm",value:function(){var e=document.createElement("div");e.classList.add("fs-dropzone"),this.initDropzoneToElement(e,this._options.uploadUrl(),this._options.csrfToken()),this.existingAttachments();var t=document.createElement("div");return t.appendChild(e),t}},{key:"getValues",value:function(e){return{}}},{key:"getUploads",value:function(){return this._uploads}},{key:"initDropzoneToElement",value:function(t,n,r){var o=this;t.classList.add("dropzone");var i=r?{"X-CSRFToken":r,"X-App-Plugin":e.type}:{"X-App-Plugin":e.type};this._dropzone=new Dropzone(t,{url:n,headers:i,addRemoveLinks:!0}),Dropzone.options.dropzone=!1,this._dropzone.on("success",function(e,t){t.temp=1,o._uploads.push(t)}),this._dropzone.on("removedfile",function(e){var t=!0,n=!1,r=void 0;try{for(var i,a=o._uploads[Symbol.iterator]();!(t=(i=a.next()).done);t=!0){var u=i.value;e.name===u.name&&(u.removed=!0)}}catch(e){n=!0,r=e}finally{try{!t&&a.return&&a.return()}finally{if(n)throw r}}})}},{key:"existingAttachments",value:function(){if(this._defaults&&this._defaults.hasOwnProperty("uploads")){console.log(this._defaults);var e=!0,t=!1,n=void 0;try{for(var r,o=this._defaults.uploads[Symbol.iterator]();!(e=(r=o.next()).done);e=!0){var i=r.value;this._dropzone.options.addedfile.call(this._dropzone,i),this._dropzone.options.thumbnail.call(this._dropzone,i,i.url),this._dropzone.options.complete.call(this._dropzone,i),this._uploads.push(i)}}catch(e){t=!0,n=e}finally{try{!e&&o.return&&o.return()}finally{if(t)throw n}}}}}],[{key:"getName",value:function(){return"Files Plugin"}},{key:"getIcon",value:function(){return"https://cdnjs.cloudflare.com/ajax/libs/foundicons/3.0.0/svgs/fi-photo.svg"}}]),e}();i.type="files_plugin",t.default=i},16:function(e,t,n){"use strict";function r(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var o=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();Object.defineProperty(t,"__esModule",{value:!0});var i=function(){function e(t,n){r(this,e),this._options=n,this._defaults=t,this._text=null}return o(e,[{key:"getForm",value:function(){var e=this._defaults.values;this._text=document.createElement("input"),this._text.type="text",this._text.value=e?e.input:"",this._level=document.createElement("select");for(var t=1;t<7;t++){var n=document.createElement("option");n.value=t.toString(),n.text=t.toString(),n.selected=e&&e.level==t,this._level.appendChild(n)}var r=document.createElement("div");return r.appendChild(this._level),r.appendChild(this._text),r}},{key:"getValues",value:function(){return{input:this._text.value,level:this._level.value}}}],[{key:"getName",value:function(){return"Header Plugin"}},{key:"getIcon",value:function(){return"https://cdnjs.cloudflare.com/ajax/libs/foundicons/3.0.0/svgs/fi-bold.svg"}}]),e}();i.type="header_plugin",t.default=i},23:function(e,t,n){n(5),e.exports=n(8)},5:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(14);window.addEventListener("rubricate__app_created",function(e){var t=!0,n=!1,o=void 0;try{for(var i,a=Object.keys(r)[Symbol.iterator]();!(t=(i=a.next()).done);t=!0){var u=i.value;e.detail.app.types.add(r[u])}}catch(e){n=!0,o=e}finally{try{!t&&a.return&&a.return()}finally{if(n)throw o}}})},8:function(e,t){}});