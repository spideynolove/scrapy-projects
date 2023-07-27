define("metaserver/static/js/app_actions/app_actions_menu",["require","exports","tslib","metaserver/static/js/async/loadable","metaserver/static/js/modules/clean/web_timing_logger"],(function(e,s,r,t,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.UnconnectedExtensionsMenu=s.ExtensionsMenu=void 0,s.ExtensionsMenu=t.Loadable({loader:()=>r.__awaiter(void 0,void 0,void 0,(function*(){yield i.waitForTTI();const{ExtensionsMenu:s}=yield new Promise((s,r)=>{e(["metaserver/static/js/modules/clean/react/extensions/extensions_menu_component_wrapper"],s,r)}).then(r.__importStar);return s}))}),s.UnconnectedExtensionsMenu=t.Loadable({loader:()=>new Promise((s,r)=>{e(["metaserver/static/js/app_actions/unconnected_menu_wrapper"],s,r)}).then(r.__importStar).then(({UnconnectedMenu:e})=>e)})})),define("typescript/libraries/file-viewer/src/libraries/frame_messenger/index",["require","exports","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_base","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_client","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_host","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_logger"],(function(e,s,r,t,i,n){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.logFrameMessage=s.FrameMessengerHost=s.FrameMessengerClient=s.SendMessageConverter=s.ReceiveMessageConverter=s.Parameters=s.MessageHandler=s.Message=void 0,Object.defineProperty(s,"Message",{enumerable:!0,get:function(){return r.Message}}),Object.defineProperty(s,"MessageHandler",{enumerable:!0,get:function(){return r.MessageHandler}}),Object.defineProperty(s,"Parameters",{enumerable:!0,get:function(){return r.Parameters}}),Object.defineProperty(s,"ReceiveMessageConverter",{enumerable:!0,get:function(){return r.ReceiveMessageConverter}}),Object.defineProperty(s,"SendMessageConverter",{enumerable:!0,get:function(){return r.SendMessageConverter}}),Object.defineProperty(s,"FrameMessengerClient",{enumerable:!0,get:function(){return t.FrameMessengerClient}}),Object.defineProperty(s,"FrameMessengerHost",{enumerable:!0,get:function(){return i.FrameMessengerHost}}),Object.defineProperty(s,"logFrameMessage",{enumerable:!0,get:function(){return n.logFrameMessage}})})),define("typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_base",["require","exports"],(function(e,s){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.FrameMessengerBase=void 0;class r{constructor(e,s=(e=>JSON.parse(e.data)),r=(e=>JSON.stringify(e))){this._window=window,this.handleUntrustedMessage=e=>{if(!this.isOriginAllowed(e.origin))return;let s;try{s=this.receiveMessageConverter(e)}catch(e){return}null!=s.action&&this.handleTrustedMessage(e,s)},this.allowedOrigins=e,this.receiveMessageConverter=s,this.sendMessageConverter=r}getWindow(){return this._window}setWindow(e){this._window=e}startListening(){this.getWindow().addEventListener("message",this.handleUntrustedMessage)}stopListening(){this.getWindow().removeEventListener("message",this.handleUntrustedMessage)}regexIn(e,s){for(const r of s){if(r instanceof RegExp&&e.match(r))return!0;if("string"==typeof r&&r===e)return!0}return!1}static stripStandardPort(e){return"http://"===e.substr(0,7)?e.replace(/:80$/,""):"https://"===e.substr(0,8)?e.replace(/:443$/,""):e}isOriginAllowed(e){return this.regexIn(r.stripStandardPort(e),this.allowedOrigins)}packagePostMessage(e,s){const r={action:e,parameters:s};return this.sendMessageConverter(r)}}s.FrameMessengerBase=r})),define("typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_client",["require","exports","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_base"],(function(e,s,r){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.FrameMessengerClient=void 0;class t extends r.FrameMessengerBase{constructor(){super(...arguments),this.trustedOriginForPosting=null,this.validActions=[],this.trustedMessageHandler=null,this.parentMessageQueue=[],this.onParentReady=null}configureParentMessaging(e,s,r=null){this.resetOriginsForPosting(),this.validActions=s,this.trustedMessageHandler=e,this.onParentReady=r}startListening(){super.startListening(),this.requestParentOrigin()}postMessageToParent(e,s={}){const r=this.packagePostMessage(e,s);null===this.trustedOriginForPosting?this.parentMessageQueue.push(r):this.getWindow().parent.postMessage(r,this.trustedOriginForPosting)}handleTrustedMessage(e,s){"parent-ready"===s.action&&this.updateParentOrigin(e.origin),-1!==this.validActions.indexOf(s.action)&&null!==this.trustedMessageHandler&&this.trustedMessageHandler(s)}resetOriginsForPosting(){this.trustedOriginForPosting=null}updateParentOrigin(e){const s=this.trustedOriginForPosting;return!!this.isOriginAllowed(e)&&(this.trustedOriginForPosting=e,this.parentMessageQueue.length>0&&(this.parentMessageQueue.forEach(e=>{const s=JSON.parse(e);this.postMessageToParent(s.action,s.parameters)}),this.parentMessageQueue=[]),null!=this.trustedOriginForPosting&&null==s&&null!=this.onParentReady&&this.onParentReady(),!0)}requestParentOrigin(){this.getWindow().parent.postMessage('{"action": "child-requesting-parent-origin"}',"*");this.getWindow().setTimeout(()=>{null==this.trustedOriginForPosting&&this.requestParentOrigin()},t._REQUEST_PARENT_ORIGIN_POLL_DELAY)}}s.FrameMessengerClient=t,t._REQUEST_PARENT_ORIGIN_POLL_DELAY=100})),define("typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_host",["require","exports","typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_base"],(function(e,s,r){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.FrameMessengerHost=void 0;class t extends r.FrameMessengerBase{constructor(){super(...arguments),this.trustedChildOriginForPosting=null,this.validActionsFromChild=[],this.trustedMessageFromChildHandler=null,this.getChildIframes=()=>[]}configureChildMessaging(e,s,r){if("string"==typeof e){const s=e;this.getChildIframes=()=>[].slice.call(document.querySelectorAll(s),0)}else this.getChildIframes=e;this.trustedChildOriginForPosting=null,this.validActionsFromChild=r,this.trustedMessageFromChildHandler=s}startListening(){super.startListening(),this.postMessageToChildren("parent-ready")}getTrustedChildOriginForPosting(){if(null!=this.trustedChildOriginForPosting)return this.trustedChildOriginForPosting;const e=this.getChildIframes();for(const s of e){const e=""+s.getAttribute("src"),r=this.getOriginFromUrl(e);if(this.isOriginAllowed(r))return this.updateChildOrigin(r),this.trustedChildOriginForPosting}return this.trustedChildOriginForPosting}childIsValidated(){return null!=this.trustedChildOriginForPosting}isNumber(e){return!isNaN(parseInt(e,10))}getOriginFromUrl(e){const s=document.createElement("a");s.href=e;const r=s.origin;if(r)return"null"===r?"*":r;const t=this.isNumber(s.port)?`:${s.port}`:"";return`${s.protocol}//${s.hostname}${t}`}postMessageToChildren(e,s={}){const r=this.getChildIframes();this.postMessageToChildElements(r,e,s)}resetOriginsForPosting(){this.trustedChildOriginForPosting=null}updateChildOrigin(e){"null"===e&&(e="*"),this.trustedChildOriginForPosting=e}handleTrustedMessage(e,s){this.updateChildOrigin(e.origin),"child-requesting-parent-origin"===s.action&&this.postMessageToChildren("parent-ready"),-1!==this.validActionsFromChild.indexOf(s.action)&&null!=this.trustedMessageFromChildHandler&&this.trustedMessageFromChildHandler(s)}postMessageToChildElements(e,s,r={}){const t=this.getTrustedChildOriginForPosting();if(null==t)return;const i=this.packagePostMessage(s,r);e.forEach(e=>{e.contentWindow&&e.contentWindow.postMessage(i,t)})}}s.FrameMessengerHost=t})),define("typescript/libraries/file-viewer/src/libraries/frame_messenger/frame_messenger_logger",["require","exports","lodash"],(function(e,s,r){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.logFrameMessage=void 0;const t=[];r.debounce(()=>{console.groupCollapsed("Frame Messenger Events"),console.table(t),console.groupEnd()},1e3);s.logFrameMessage=(e,{eventName:s,message:r,event:t,data:i})=>{}}));
//# sourceMappingURL=pkg-frame_messenger.min.js-vflEcOrY3.map