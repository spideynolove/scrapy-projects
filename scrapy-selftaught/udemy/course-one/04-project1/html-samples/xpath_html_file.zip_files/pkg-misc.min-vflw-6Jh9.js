define("metaserver/static/js/modules/clean/beacon_nodeps",["require","exports","tslib","metaserver/static/js/modules/core/exception","lodash","metaserver/static/js/bolt/bolt_nodeps"],(function(t,e,s,o,i,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.Receiver=e.Transmitter=e.UserAppPresence=e.UserContextPresence=e.PresenceParams=e.PresenceType=e.AgentStatus=e.Agent=e.Source=e.Platforms=void 0,o=s.__importStar(o),i=s.__importStar(i);e.Platforms={WEB:0,IOS:1,ANDROID:2,DESKTOP:3};class n{constructor(t,s,o){this.platform=t,this.surface=s,this.identifier=null!=o?o:"";let i=!1;for(const t in e.Platforms){const s=e.Platforms[t];if(this.platform===s){i=!0;break}}if(!i)throw new Error("platform must be from Beacon.Platforms");if(this.surface.length>32||0===this.surface.length)throw new Error("surface must be populated and <= 32 chars.");if(this.identifier.length>128)throw new Error("identifier must be <= 128 chars.")}static from_json(t){return new n(t.platform,t.surface,t.identifier)}}e.Source=n;class a{constructor(t,e,s,o){if(this.user_id=t,this.app=e,this.context=s,this.source=o,this.user_id.length>256)throw new Error("user_id must be <= 256 chars.");if(this.app.length>32||0===this.app.length)throw new Error("app must be populated and <= 32 chars.");if(this.context.length>64||0===this.context.length)throw new Error("context must be populated and <= 64 chars.")}static from_json(t){const e=n.from_json(t.source);return new a(t.user_id,t.app,t.context,e)}}e.Agent=a;class h{constructor(t,e,s){if(this.agent=t,this.status=e,this.auth_key=s,this.status.length>32)throw new Error("status must be <= 32 chars")}static from_json(t){return new h(a.from_json(t.agent),t.status)}}e.AgentStatus=h,e.PresenceType={UserContext:"UserContext",UserApp:"UserApp",Context:"Context"};class _{constructor(t,s,o,i,r){if(this.type=t,this.user_id=s,this.app=o,this.context=i,this.token=r,this.type!==e.PresenceType.UserContext&&this.type!==e.PresenceType.UserApp&&this.type!==e.PresenceType.Context)throw new Error(`Unsupported type: ${this.type}.`);if((null!=this.user_id?this.user_id.length:0)>256)throw new Error("user_id must be <= 256 chars.");if(this.app.length>32)throw new Error("app must be <= 32 chars.");if((null!=this.context?this.context.length:0)>64)throw new Error("context must be <= 64 chars.")}}e.PresenceParams=_;class u{constructor(t,e){this.presence_params=t,this.agents=e}}e.UserContextPresence=u;class d{constructor(t,e){this.presence_params=t,this.status=e}}e.UserAppPresence=d,d.Status={Offline:1,Online:2};class c{constructor(t,e,s){this.presence_params=t,this.snapshot=e,this.delta=s}}e.Transmitter=class{constructor(t,e,s=(()=>{})){this._heartbeat=()=>{if(!this._started||0===this._presence_data.length)return;this._offline_agents=this._presence_data.filter(t=>""!==t.status).map(t=>t.agent),this._has_changes=!1;const t=new AbortController;this._heartbeat_xhr=fetch("https://beacon.dropbox.com/1/update",{method:"POST",body:JSON.stringify({token:this._token,updates:this._presence_data}),headers:{"Content-Type":"application/json; charset=utf-8"},credentials:"include",signal:t.signal}).then(t=>t.json()).then(this._handle_heartbeat_success).catch(this._handle_heartbeat_error),setTimeout(()=>t.abort(),5e3)},this._handle_heartbeat_success=t=>{if(this._heartbeat_xhr=void 0,!this._started)return;const e=[];for(const s of t.agent_errors||[]){const t=s.error,r=a.from_json(s.agent);"authorization_error"===t?e.push(r):"invalid_agent"===t&&o.reportStack(`Input error: ${s}`),this._presence_data=this._presence_data.filter(t=>!i.isEqual(t.agent,r))}if(e.length){const t=this._authz_cb;window.setTimeout(()=>t(e),0)}for(const t of this._offline_agents)for(let e=0;e<this._presence_data.length;e++){const s=this._presence_data[e];if(i.isEqual(s.agent,t)&&""===s.status){this._presence_data.splice(e,1);break}}const s=this._has_changes?0:6e4;this._backoff_window=5e3,this._timeout_id=window.setTimeout(this._heartbeat,s)},this._handle_heartbeat_error=t=>{if(this._heartbeat_xhr=void 0,!this._started)return;if(t.status>=400&&t.status<500){if(401===t.status)return window.setTimeout(this._authn_cb,0),void this.stop();400===t.status&&o.reportStack(`Bad request: ${t.responseText}`)}const e=Math.random()*this._backoff_window;this._backoff_window=Math.min(2*this._backoff_window,12e4),this._timeout_id=window.setTimeout(this._heartbeat,e)},this._token=t,this._authn_cb=e,this._authz_cb=s,this._started=!1,this._presence_data=[],this._offline_agents=[],this._has_changes=!1}start(){if(!this._started)return this._backoff_window=5e3,this._started=!0,this._has_changes=!1,this._heartbeat()}stop(){this._started=!1,this._heartbeat_xhr=void 0,window.clearTimeout(this._timeout_id),this._timeout_id=void 0}add_or_update_agents(t){for(const e of t)this._has_changes=this._add_or_update_agent(e)||this._has_changes;!this._heartbeat_xhr&&this._started&&(window.clearTimeout(this._timeout_id),this._timeout_id=window.setTimeout(this._heartbeat,0))}_add_or_update_agent(t){for(let e=0;e<this._presence_data.length;e++){const s=this._presence_data[e];if(i.isEqual(s.agent,t.agent))return(s.status!==t.status||s.auth_key!==t.auth_key)&&(this._presence_data[e]=t,!0)}return this._presence_data.push(t),!0}};e.Receiver=class{constructor(t,s,o){this._compact_context_updates=(t,e)=>{let s,o,r=!1,n=[];for(const t of e)if(null!=t.snapshot)r=!0,n=t.snapshot;else if(null!=t.delta)for(const e of t.delta){let t=!1;for(let s=0;s<n.length;s++){const o=n[s];if(i.isEqual(o.agent,e.agent)){t=!0,n[s]=e;break}}t||n.push(e)}return r?(o=n,s=void 0):(o=void 0,s=n),new c(t,o,s)},this._on_update=t=>{const s=[];for(const o of t){const{channel_state:t}=o,i=new r.ChannelId(t.app_id,t.unique_id),_=this._bolt_channel_to_presence_params(i);switch(_.type){case e.PresenceType.UserContext:{const{payload:t}=o.payloads.slice(-1)[0],e=null!=t.agents?t.agents.map(h.from_json):[];s.push(new u(_,e));break}case e.PresenceType.UserApp:{const{payload:t}=o.payloads.slice(-1)[0];s.push(new d(_,t.status));break}case e.PresenceType.Context:{const t=function(t){const e=n.from_json(t.source),s=new a(t.user_id,_.app,_.context,e);return new h(s,t.status)},e=function(e){var s,o,i,r;return{snapshot:null===(o=null===(s=e.snapshot)||void 0===s?void 0:s.agents)||void 0===o?void 0:o.map(t),delta:null===(r=null===(i=e.delta)||void 0===i?void 0:i.agents)||void 0===r?void 0:r.map(t)}},i=o.payloads.map(t=>e(t.payload));s.push(this._compact_context_updates(_,i));break}}}return this._update_callback(s)},this._on_refresh=t=>this._refresh_callback(t.map(this._bolt_channel_to_presence_params)),this._presence_params=t,this._update_callback=s,this._refresh_callback=o;const _=this._presence_params.map(this._presence_params_to_bolt_channel);this._thunder_client=new r.ThunderClient(_,this._on_update,this._on_refresh)}start(){return this._thunder_client.start()}stop(){return this._thunder_client.unsubscribe()}_presence_params_to_bolt_channel(t){switch(t.type){case e.PresenceType.UserContext:return new r.SignedChannelState(`beacon_uc-${t.app}`,`${t.user_id}|${t.context}`,"0",t.token);case e.PresenceType.UserApp:return new r.SignedChannelState(`beacon_ua-${t.app}`,t.user_id||"","0",t.token);case e.PresenceType.Context:return new r.SignedChannelState(`beacon_c-${t.app}`,t.context,"0",t.token);default:throw new Error(`Unknown type: ${t.type}`)}}_bolt_channel_to_presence_params(t){const s=t.app_id.split("-"),o=t.unique_id.split("|");if(2!==s.length)throw new Error(`Unexpected format of Bolt app_id: ${t.app_id}.`);const i=s[1];let r="",n="",a=e.PresenceType.UserContext;switch(s[0]){case"beacon_uc":if(2!==o.length)throw new Error(`Unexpected format of beacon_uc: ${t.unique_id}.`);a=e.PresenceType.UserContext,r=o[0],n=o[1];break;case"beacon_ua":if(1!==o.length)throw new Error(`Unexpected format of beacon_ua: ${t.unique_id}.`);a=e.PresenceType.UserApp,r=o[0];break;case"beacon_c":if(1!==o.length)throw new Error(`Unexpected format of beacon_c: ${t.unique_id}.`);a=e.PresenceType.Context,n=o[0];break;default:throw new Error(`Unknown Bolt app_id: ${t.app_id}.`)}return new _(a,r,i,n,void 0)}}})),define("metaserver/static/js/file_uploader/drag_utils",["require","exports"],(function(t,e){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.buildUrlLinkfileContents=e.getDraggedLink=void 0,e.getDraggedLink=function(t){if(!t||!t.types)return null;if(((t,e)=>{for(const s of t)if(e===s)return!0;return!1})(t.types,"Files"))return null;let e,s=null;try{e=t.getData("text/x-moz-url")}catch(t){}if(null!=e){const t=e.split("\n");t.length>=1&&(s=t[0])}if(!s)try{s=t.getData("text/uri-list")}catch(t){}if(!s)try{s=t.getData("Url")}catch(t){}return s||(s=null),s},e.buildUrlLinkfileContents=function(t){return`[InternetShortcut]\r\nURL=${t}\r\n`}})),define("metaserver/static/js/deprecated_pyxl/controllers/bubble_dropdown",["require","exports","tslib","lodash","jquery","ts-key-enum","metaserver/static/js/modules/core/dom"],(function(t,e,s,o,i,r,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),o=s.__importStar(o),i=s.__importDefault(i),n=s.__importStar(n);class a{constructor(t,e,s,r,n,h,_){null==h&&(h=0),this.closeDropdown=this.closeDropdown.bind(this),this.openDropdown=this.openDropdown.bind(this),this.repositionDropdown=this.repositionDropdown.bind(this),this._activateNonButton=this._activateNonButton.bind(this),this._onTargetKeydown=this._onTargetKeydown.bind(this),this._onDropdownKeydown=this._onDropdownKeydown.bind(this),this._on_mouseover=this._on_mouseover.bind(this),this._on_mouseout=this._on_mouseout.bind(this),this._on_global_hover=this._on_global_hover.bind(this),this._toggle_bubble=this._toggle_bubble.bind(this),this._show_bubble=this._show_bubble.bind(this),this._hide_bubble=this._hide_bubble.bind(this),this.$root=t,this.arrow_direction=e,this.show_on_hover=s,this.show_close_button=r,this.shown_by_default=n,this.top_adjustment=h,this.tabindex=_,this.$target=this.$root.find(".bubble-dropdown-target"),this.$dropdown=this.$root.find(".bubble-dropdown"),this.$arrow_anchor=this.$root.find(".bubble-dropdown-arrow-anchor"),this.$arrow=this.$dropdown.find(".bubble-arrow");if(this.target_position={top:"bottom",left:"right",bottom:"top",right:"left"}[this.arrow_direction],this.$target.on("keydown",this._onTargetKeydown),this.$dropdown.on("keydown",this._onDropdownKeydown),this.$target.attr("aria-expanded",!1),this.show_close_button)this.$root.find(".bubble-dropdown-x").on("click",this.closeDropdown);else if(this.show_on_hover){if(this.$target.on("mouseover",this._on_mouseover),this.$dropdown.on("mouseover",this._on_mouseover),this.$target.on("mouseout",this._on_mouseout),this.$dropdown.on("mouseout",this._on_mouseout),this.$target.attr("tabindex",0).on("focus",this._show_bubble),0===this.$dropdown.find(this._focus_selectors).length){const t=o.uniqueId("bubble-dropdown-tooltip-");this.$dropdown.attr({id:t,role:"tooltip"}),this.$target.attr("aria-describedby",t)}i.default(document).on(a.HOVER_SHOWN,this._on_global_hover)}else{this.$target.click(this._toggle_bubble);let t=0;this.tabindex&&(t=this.tabindex),"BUTTON"!==this.$target.get(0).tagName&&this.$target.attr({role:"button",tabindex:t}).on("keyup",this._activateNonButton),i.default("body").on("click",t=>{if(i.default(t.target).is("select"))return!0;return i.default(t.target).closest(this.$target).length||i.default(t.target).closest(this.$dropdown).length||this._hide_bubble(),!0})}this.shown_by_default&&this.openDropdown()}static initClass(){this.HOVER_SHOWN="bubble:hover:shown",this.prototype._dropdown_shown=!1,this.prototype._focus_selectors="a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, *[tabindex], *[contenteditable]"}closeDropdown(){if(this._dropdown_shown)return this._hide_bubble()}openDropdown(){if(!this._dropdown_shown)return this._show_bubble()}repositionDropdown(){if(this._dropdown_shown)return this._show_bubble()}_activateNonButton(t){if([r.Key.Enter," "].includes(t.key))return this._toggle_bubble(),!1}_onTargetKeydown(t){return(t.key===r.Key.Escape&&!this.show_on_hover||t.key===r.Key.Tab&&t.shiftKey||t.key===r.Key.Tab&&1===this.$root.find(this._focus_selectors).length)&&this._hide_bubble(),!0}_onDropdownKeydown(t){if(this.show_on_hover||t.key!==r.Key.Escape){if(t.key===r.Key.Tab&&!t.shiftKey){const e=this.$root.find(this._focus_selectors);t.target===e[e.length-1]&&this._hide_bubble(!this.show_on_hover)}}else this._hide_bubble(!0);return!0}_on_mouseover(){return i.default(document).trigger(a.HOVER_SHOWN,this.$target),this._show_bubble(),clearTimeout(this.$dropdown.data("timeout_id"))}_on_mouseout(){const t=setTimeout(this._hide_bubble,200);return this.$dropdown.data("timeout_id",t)}_on_global_hover(t,e){if(this._dropdown_shown&&e!==this.$target)return this._hide_bubble(),clearTimeout(this.$dropdown.data("timeout_id"))}_toggle_bubble(){return this._dropdown_shown?this._hide_bubble():this._show_bubble(),!0}_show_bubble(){let t,e;if(this.$target.hasClass("disabled"))return;this.$dropdown.show();const s=this.$arrow_anchor.length?this.$arrow_anchor:this.$target,{top:o}=this.$arrow.position(),{left:i}=this.$arrow.position();switch(this.arrow_direction){case"left":t=s.outerWidth()+this.$arrow.outerWidth(),e=s.outerHeight()/2-o;break;case"right":t=-1*(this.$dropdown.outerWidth()+this.$arrow.outerWidth()),e=s.outerHeight()/2-o;break;case"top":t=s.outerWidth()/2-i,e=s.outerHeight()+this.$arrow.outerHeight()-this.top_adjustment;break;case"bottom":t=s.outerWidth()/2-i,e=-1*(this.$dropdown.outerHeight()+this.$arrow.outerHeight()+this.top_adjustment)}return n.clone_position(this.$dropdown[0],s[0],{setHeight:!1,setWidth:!1,offsetLeft:t,offsetTop:e}),this._dropdown_shown=!0,this.$target.addClass("bubble-dropdown-target--active").attr("aria-expanded",!0)}_hide_bubble(t){if(this.$dropdown.hide(),this._dropdown_shown=!1,this.$target.removeClass("bubble-dropdown-target--active").attr("aria-expanded",!1),t)return this.$target.focus()}}a.initClass(),e.default=a})),define("metaserver/static/js/deprecated_pyxl/controllers/input",["require","exports","tslib","jquery","metaserver/static/js/accessibility/tabbable","metaserver/static/js/modules/clean/web_timing_logger","metaserver/static/js/modules/core/assert","metaserver/static/js/modules/core/i18n"],(function(t,e,s,o,i,r,n,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.PasswordWatchInput=e.PasswordInput=e.TextInput=void 0,o=s.__importDefault(o),i=s.__importDefault(i),r=s.__importStar(r);const h=function(t){const e=o.default.data(t,"input-element");return n.assert(e.length,"TextInput element has no related input element please ensure it was setup correctly"),e};o.default.valHooks.textinput={get:t=>h(t).val(),set:(t,e)=>h(t).val(e).trigger("input")};class _ extends i.default{constructor(t,e=!0){super(),this._on_change=this._on_change.bind(this),this.$text_input=t,this.persistent_label=this.$text_input.is(".label-above"),this.$input=this.$text_input.find(".text-input-input"),this.$text_input.data("input-element",this.$input),this.$label=this.$text_input.find("label"),this.$text_input.find(".error-message").length&&this.$input.addClass("input-error"),this.$text_input.each((t,e)=>e.type="textinput"),this.$text_input.focus(()=>setTimeout(()=>this.$input.focus(),0)),o.default((function(){if("BODY"===(null!=document.activeElement?document.activeElement.tagName:void 0))return o.default(".autofocus:visible").first().focus()})),this._listen(),e&&this._on_change()}_listen(){return this.$input.on("keydown keyup paste input blur",()=>this._on_change()),this.$input.on("blur",t=>this.$text_input.trigger(t)),this.$input.on("focus",()=>this.$input.removeClass("input-error"))}_on_change(){this.persistent_label||this.$label.toggle(!this.$input.val());const t=this.$text_input.find(".error-message");t.length&&window.setTimeout((function(){return t[0].remove()}),3e3)}}e.TextInput=_;class u extends _{constructor(t,e=!0){super(t,e),this.$caps=this.$text_input.find(".password-caps-indicator"),this.$caps_lock=!1,this.$text_input.on("keypress",t=>{let e;const s=/Mac/.test(navigator.platform),o=null!=t.charCode?t.charCode:t.keyCode,i=String.fromCharCode(o);return i.toLowerCase()===i.toUpperCase()?e=void 0:i===i.toLowerCase()?e=t.shiftKey:i!==i.toUpperCase()||t.shiftKey&&s||(e=!t.shiftKey),null!=e&&(this.$caps_lock=e),this.$caps_lock?this.$caps.addClass("password-caps-indicator-activated"):this.$caps.removeClass("password-caps-indicator-activated")})}}e.PasswordInput=u;e.PasswordWatchInput=class extends u{constructor(e,o){super(e,!1),this._on_change=this._on_change.bind(this),this.$bubble_title=this.$text_input.find(".password-bubble-title"),this.$bubble_desc=this.$text_input.find(".password-bubble-desc"),this.$meter=this.$text_input.find(".password-input-meter"),this.$default_bubble_text=this.$bubble_desc.text(),this.$last_pwd="",this._on_change(),o?r.waitForTTI().then(()=>{new Promise((e,s)=>{t(["zxcvbn"],e,s)}).then(s.__importStar).then(({default:t})=>{this.zxcvbn=t})}):new Promise((e,s)=>{t(["zxcvbn"],e,s)}).then(s.__importStar).then(({default:t})=>{this.zxcvbn=t})}_on_change(){let t,e;const s=this.$input.val();if(this.$last_pwd!==s){if(this.$last_pwd=s,"correcthorsebatterystaple"===s||"Tr0ub4dour&3"===s||"Tr0ub4dor&3"===s){let o;t=0,e=a.intl.formatMessage({id:"6aphVB",defaultMessage:"lol"}),this.$bubble_title.text(e),"correcthorsebatterystaple"===s?(o=a.intl.formatMessage({id:"WRnWCY",defaultMessage:"Whoa there, don't take advice from a webcomic too literally ;)"}),this.$bubble_desc.text(o)):(o=a.intl.formatMessage({id:"E44pjD",defaultMessage:"Guess again"}),this.$bubble_desc.text(o))}else{const o=["",a.intl.formatMessage({id:"i/ragh",defaultMessage:"Weak"}),a.intl.formatMessage({id:"GwYES8",defaultMessage:"So-so"}),a.intl.formatMessage({id:"Yd7c8F",defaultMessage:"Good"}),a.intl.formatMessage({id:"kbsmZh",defaultMessage:"Great!"})];t=this._score(s),e=o[t],this.$bubble_title.text(e),this.$bubble_desc.text(this.$default_bubble_text)}return this.$meter.find(".password-input-dot").removeClass("password-input-dot-selected"),this.$meter.find(".password-input-dot").slice(4-t,4).addClass("password-input-dot-selected"),super._on_change()}}_get_user_inputs(){const t=["dropbox"];for(const e of Array.from(this.$text_input.closest("form").find("input[type=text], input[type=email]")))t.push(o.default(e).val());return t}_score(t){return this.zxcvbn&&t?Math.max(1,this.zxcvbn(t,this._get_user_inputs()).score):0}}}));
//# sourceMappingURL=pkg-misc.min.js-vfli3aXzh.map