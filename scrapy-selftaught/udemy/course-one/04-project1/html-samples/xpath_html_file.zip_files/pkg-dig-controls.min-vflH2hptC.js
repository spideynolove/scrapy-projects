define("metaserver/static/js/prod_assets_web_modules/dig-components/controls",["exports","../classnames","react","focus-visible"],(function(e,t,n,a){"use strict";var s=n.forwardRef(({checked:e,className:a,isIndeterminate:s=!1,inverse:l=!1,style:i={},...c},d)=>{const[u,p]=n.useState(!1),m=n.useRef(e);n.useEffect(()=>{u||e===m.current||p(!0)},[e,m,u]);const f=t("dig-Checkbox-input",{"dig-Checkbox--inverse":l,"dig-Checkbox--initiallyChecked":!u&&e}),g=t("dig-Checkbox",a),h=n.useRef(),v=((e,t)=>n=>{t.current=n,e&&("function"==typeof e?e(n):e.current=n)})(d,h);return n.useEffect(()=>{h.current&&(h.current.indeterminate=s)},[s,d]),n.createElement("span",{className:g,style:i},n.createElement("input",{checked:e,className:f,ref:v,type:"checkbox",...c}),n.createElement("span",{className:"dig-Checkbox-styles"}),n.createElement(r,null),n.createElement(o,null))});s.displayName="Checkbox";var o=()=>n.createElement("svg",{className:"dig-Checkbox-checked-icon","aria-hidden":"true",width:"20px",height:"20px",viewBox:"0 0 20 20",fill:"none",xmlns:"http://www.w3.org/2000/svg",focusable:"false"},n.createElement("path",{d:"M1 4L4.5 7.5L11 1",stroke:"currentColor",strokeWidth:"2",transform:"translate(4, 6)"}));o.displayName="CheckedCheckboxIcon";var r=()=>n.createElement("svg",{"aria-hidden":"true",width:"20px",height:"20px",viewBox:"0 0 20 20",version:"1.1",className:"dig-Checkbox-indeterminate-icon",focusable:"false"},n.createElement("rect",{x:"5px",y:"9px",width:"10px",height:"2px"}));r.displayName="IndeterminateCheckboxIcon";var l=n.forwardRef(({className:e,children:a,inverse:s,...o},r)=>{const l=t("dig-Radio",e,{"dig-Radio--inverse":s});return n.createElement("input",{type:"radio",className:l,ref:r,...o})});l.displayName="RadioButton";var i={options:new Map},c=(e,t)=>{let n;switch(t.type){case"UPDATE_OPTION":const a=new Map(e.options);a.set(t.payload.key,t.payload.value),n={options:a};break;case"REMOVE_OPTION":const s=new Map(e.options);s.delete(t.payload.key),n={options:s}}return{...e,...n}},d={setSelectedOption:()=>!1,optionItems:{items:new Map,updateOption:()=>!1,addOption:()=>!1,removeOption:()=>!1}},u=n.createContext(d),p=n.forwardRef(({children:e,disabled:a,variant:s="icon",value:o,role:r="tab",onClick:l,...i},c)=>{const{setSelectedOption:d,optionItems:p,selectedElement:m}=n.useContext(u),f=n.useRef(null);((e,t)=>{n.useEffect(()=>(t.addOption(e),()=>{t.removeOption(e.value)}),[]),n.useEffect(()=>{t.updateOption(e)},[e.value,e.element])})({value:o,element:f.current},p);const g=t("dig-SegmentedControl-option",`dig-SegmentedControl-option--${s}`,{"dig-SegmentedControl-option--disabled":a});n.useImperativeHandle(c,()=>({offsetWidth:f.current?f.current.offsetWidth:0,offsetLeft:f.current?f.current.offsetLeft:0,getBoundingClientRect:()=>{if(f.current)return f.current.getBoundingClientRect()}}));const h=n.useMemo(()=>void 0===m?"false":m===f.current?"true":"false",[m,f]);return n.createElement("button",{role:r,className:g,disabled:a,ref:f,onClick:e=>{l&&l(e),d({value:o,element:f.current})},"aria-selected":h,...i},e)});p.displayName="Option";var m=({offsetWidth:e,offsetLeft:t})=>{const a=n.useRef(null);return n.useEffect(()=>{a.current.setAttribute("style",`width: ${e}px; \n       transform: translate(${t}px, 0);`)},[e,t]),n.createElement("span",{ref:a,className:"dig-SegmentedControl-selector"})},f=({className:e,children:a,selectedValue:s,onSelection:o,onValueChange:r,inverse:l=!1,...d})=>{const[p,f]=n.useState(!1),g=(()=>{const[e,t]=n.useReducer(c,i),a=({value:e,element:n})=>{e&&t({type:"UPDATE_OPTION",payload:{key:e,value:n}})},s=a;return{items:e.options,updateOption:a,addOption:s,removeOption:e=>{e&&t({type:"REMOVE_OPTION",payload:{key:e}})}}})(),[h,v]=n.useState(null),E=t("dig-SegmentedControl",e,{"dig-SegmentedControl--inverse":l});n.useEffect(()=>{p||f(!0)},[]),n.useEffect(()=>{v(((e,t)=>{let n=null;return void 0!==t&&e.has(t)&&(n=e.get(t)),n})(g.items,s))},[g.items,s]),n.useEffect(()=>{p&&r&&r(s)},[s]);const b={setSelectedOption:e=>{v(e.element?e.element:null),r&&r(e.value),o&&o(e.value)},optionItems:g,selectedElement:h};return n.createElement(u.Provider,{value:b},n.createElement("div",{role:"tablist",className:E,...d},h&&n.createElement(m,{offsetWidth:h.offsetWidth,offsetLeft:h.offsetLeft}),a))};f.displayName="SegmentedControl",f.Option=p;var g=n.forwardRef(({isToggled:e,disabled:a,className:s,wrapperProps:o,inverse:r,...l},i)=>{const c=t(s,"dig-Toggle",{"dig-Toggle--isToggled":e,"dig-Toggle--disabled":a,"dig-Toggle--inverse":r});return n.createElement("label",{className:c,...o},n.createElement("input",{role:"switch",type:"checkbox",className:"dig-Toggle-input",checked:e,disabled:a,ref:i,...l}),n.createElement("span",{className:"dig-Toggle-track"}))});g.displayName="Toggle",e.Checkbox=s,e.RadioButton=l,e.SegmentedControl=f,e.Toggle=g,Object.defineProperty(e,"__esModule",{value:!0})}));
//# sourceMappingURL=pkg-dig-controls.min.js-vflA4g9eV.map