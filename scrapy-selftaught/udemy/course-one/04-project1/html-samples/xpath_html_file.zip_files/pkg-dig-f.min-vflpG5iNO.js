define("metaserver/static/js/prod_assets_web_modules/dig-components/typeahead",["exports","focus-visible","react","./click_outside","./hooks","../classnames","./motion","./overlay","./progress_indicators","./icons","./icons/src","./typography","./buttons","./layer","react-dom","../resize-observer-polyfill","../common/Transition","../@popperjs/core","../react-transition-group/CSSTransition","../common/extends"],(function(e,t,o,n,a,s,r,i,l,c,u,d,m,p,g,h,y,v,w,f){"use strict";var T=['.dig-Typeahead-row--interactive[role="option"]','.dig-Typeahead-row--interactive[role="menuitemcheckbox"]',".dig-Typeahead-results--show-more"],E={value:void 0,setSelected:()=>!1,setFocused:()=>!1,closeMenu:()=>!1,isPortaled:!0,menuRows:a.createMenuRows(),containerId:"",setIsTypeaheadDropdownVisible:()=>{}},x=o.createContext(E),b=o.createContext({}),R=o.createContext({}),C=({children:e,isPortaled:t,closeOnSelection:s=!0,inlineProps:r,openMenuOnFocus:i=!0,containerId:l,hasMaxHeight:c=!1,onSelection:u,onBlur:d,onToggle:m,...p})=>{const g=o.useRef(null),[h,y]=o.useState(!1),[v,w]=o.useState(!1),f=o.useRef(null),E=o.useRef(null),b=a.useUniqueId({prefix:"dig-Typeahead",idOverride:l}),R=o.useCallback(e=>{v!==e&&w(e)},[v]),C=o.useCallback((e,t)=>{u&&u(e,t),s&&(E&&E.current&&E.current(void 0),g&&a.returnFocus(g))},[s,u,E]),{isOpen:M,openMenu:N,closeMenu:k,toggleMenu:P,value:I,setSelected:S,setFocused:F,getRootProps:D,getTriggerProps:O,getContentProps:B,menuRows:K,isFocusing:A}=a.useMenu({triggerRef:g,contentRef:f,onSelection:C,onToggle:m,closeOnSelection:s,shouldFocusDisabledRows:!0,interactiveRowSelectors:T,allowLetterNavigation:!1,focusMenuRowTriggerKey:"ArrowDown",allowSpaceBarToOpenMenu:!1,focusNextItemImmediately:!1});E.current=F;const z=o.useCallback(()=>{y(!1),document.removeEventListener("mouseup",z)},[]);o.useEffect(()=>(h&&document.addEventListener("mouseup",z),()=>document.removeEventListener("mouseup",z)),[h,z]);const _={getContentProps:e=>({open:Boolean(M),triggerRef:g,...B({tabIndex:void 0,...e}),role:"listbox"}),getTriggerProps:e=>({...O({...e,onKeyDown:t=>{if(r){const{customOpenKey:e,onCustomOpenKeyTrigger:o,customCloseKey:n}=r;t.key===e.key?(N({autoFocus:!1}),o&&o(t)):n&&t.key===n.key&&k({autoFocus:!1})}e&&e.onKeyDown&&e.onKeyDown(t)}}),role:"combobox","aria-haspopup":"listbox","aria-autocomplete":"list","aria-controls":b,onChange:t=>{r||N({autoFocus:!1}),e&&e.onChange&&e.onChange(t)},onMouseDown:t=>{e&&e.onMouseDown&&e.onMouseDown(t),y(!0)},onClick:e?e.onClick:void 0,onKeyUp:e?e.onKeyUp:void 0,onFocus:t=>{i&&N({autoFocus:!1}),F(void 0),e&&e.onFocus&&e.onFocus(t)}}),openMenu:N,closeMenu:k,toggleMenu:P,triggerRef:g},H=o.useCallback(e=>{I||A||k({autoFocus:!1}),d&&d(e)},[I,A,k,d]),L={isPortaled:t,contentRef:f,value:I,setSelected:S,setFocused:F,closeMenu:k,inlineProps:r,menuRows:K,containerId:b,hasMaxHeight:c,setIsTypeaheadDropdownVisible:R},U=o.useCallback(()=>{k({autoFocus:!1})},[k]),j=r?e&&e(_):o.createElement(n.ClickOutside,{className:"dig-Typeahead-backdrop",isBlock:!0,onClickOutside:U,shouldPropagateMouseEvents:!1,isClickThroughPortaled:t,isActive:Boolean(M)&&!h&&v},e&&e(_));return o.createElement(x.Provider,{value:L},o.createElement("div",{className:"dig-Typeahead",...D({...p,onBlur:H})},j))};C.displayName="Wrapper";var M=({className:e,children:t,...n})=>{const a=s("dig-Typeahead-row-accessory",e);return o.createElement("div",{className:a,...n},t)};M.displayName="RowAccessory";var N=({className:e,children:t,...n})=>{const a=s("dig-Typeahead-row-content",e);return o.createElement("div",{className:a,...n},t)};N.displayName="RowContent";var k=({className:e,children:t,...n})=>{const a=s("dig-Typeahead-row-subtitle",e);return o.createElement("div",{className:a,...n},t)};k.displayName="RowSubtitle";var P=({className:e,children:t,...n})=>{const a=s("dig-Typeahead-row-title",e);return o.createElement("div",{className:a,...n},t)};P.displayName="RowTitle";var I=({id:e,title:t,subTitle:n,sectionTitle:a})=>o.createElement("div",{className:"dig-Typeahead-accessible-text",id:e},t," ",n,a&&`, ${a}`),S=o.forwardRef(({tagName:e="li",role:t="option",disabled:n=!1,interactive:r=!0,className:i,withLeftAccessory:l,withRightAccessory:c,withSubtitle:u,withTitle:d,onFocus:m,onMouseDown:p,value:g,tabIndex:h=-1,children:y,...v},w)=>{const f=o.useRef(null),{menuRows:T,setSelected:E,setFocused:C}=o.useContext(x),{resultIndex:S}=o.useContext(R),{rowIndex:F,focusIndex:D,sectionTitle:O}=o.useContext(b),B=100*(S||0)+(F||0),K=a.useUniqueId({prefix:""}),{getItemProps:A}=a.useMenuItem({interactive:r,disabled:n,ref:f,role:t,index:B},T);o.useEffect(()=>{void 0!==D&&D===F&&setTimeout(()=>{f.current&&f.current.focus()},0)},[D,F]);const z=s("dig-Typeahead-row",{"dig-Typeahead-row--disabled":n,"dig-Typeahead-row--interactive":r},i);return o.useImperativeHandle(w,()=>({getBoundingClientRect:()=>{if(f.current)return f.current.getBoundingClientRect()}})),o.createElement(e,{onMouseDown:e=>{e.preventDefault(),E(g,e),C(void 0),p&&p(e)},onFocus:e=>{C(g),m&&m(e)},className:z,ref:f,...A({...v})},y||o.createElement(o.Fragment,null,l&&o.createElement(M,null,l),o.createElement(N,{"aria-labelledby":K},o.createElement(P,{"aria-hidden":"true"},d),u&&o.createElement(k,{"aria-hidden":"true"},u)),o.createElement(I,{id:K,title:d,subTitle:u,sectionTitle:O}),c&&o.createElement(M,null,c)))});S.displayName="Row";var F=({children:e})=>o.createElement("div",{className:"dig-Typeahead-prompt"},e);F.displayName="Prompt";var D=({open:e,triggerRef:t,emptyPrompt:s,isEmptyQuery:c=!1,loading:u,children:d,auto:m=!0,positioningStrategy:p="absolute",placement:g="bottom-start",omitOverlay:h=!1,...y})=>{const{menuRows:v,closeMenu:w,contentRef:f,isPortaled:T,containerId:E,inlineProps:b,hasMaxHeight:C,setIsTypeaheadDropdownVisible:M}=o.useContext(x),N=o.useCallback(()=>{w({autoFocus:!1})},[w]),{styles:k}=a.useMaxHeight({hasMaxHeight:C,contentRef:f}),P=null!=s;if(o.useEffect(()=>{let e=!0;u||c&&P||0!==v.items.size||(e=!1),M(e)},[u,P,c,v.items.size,M]),!e||!d)return null;let I,S={};if(u?I=o.createElement(F,null,o.createElement(l.Spinner,null)):c&&P?I=s:0===v.items.size?(I=d,S={display:"none"}):I=o.Children.map(d,(e,t)=>o.createElement(R.Provider,{value:{resultIndex:t}},e)),h)return o.createElement(o.Fragment,null,I);const D=(e=>{switch(e){default:return"up";case"bottom":case"bottom-start":case"bottom-end":return"down"}})(g),O=o.createElement(r.Motion,{transitionIn:{transitions:[{property:D,value:0},{property:"opacity",value:1}],easing:"enter",duration:125},transitionOut:{transitions:[{property:"opacity",value:0}],easing:"leave",duration:125},style:{opacity:0},in:e,mountOnEnter:!0,unmountOnExit:!0},({state:n,style:a})=>(e||"exited"!==n)&&o.createElement(i.Overlay,{anchorRef:t,auto:m,isPortaled:T,placement:g,positioningStrategy:p,offsetDistance:4,setWidthSameAsAnchor:!Boolean(b)},o.createElement("ul",{className:"dig-Typeahead-container",ref:f,id:E,style:S,...y},o.createElement("div",{className:"dig-Typeahead-container--canvas",style:{...a,...k}},I))));return b?o.createElement(n.ClickOutside,{className:"dig-Typeahead-backdrop",isBlock:!0,onClickOutside:N,shouldPropagateMouseEvents:!1,isClickThroughPortaled:T,isActive:Boolean(e)},O):O};D.displayName="Container";var O=e=>{const{placeholderText:t}=e;return o.createElement(F,null,o.createElement(c.UIIcon,{size:"large",src:u.SearchLine}),o.createElement(d.Text,{color:"faint"},t))};O.displayName="EmptyPrompt";var B=({onShowMoreClick:e,showMoreButtonText:t="Show more"})=>{const n=o.useRef(null),{menuRows:s,setFocused:r}=o.useContext(x),{resultIndex:i}=o.useContext(R),{rowIndex:l}=o.useContext(b),c=100*(i||0)+(l||0),{getItemProps:u}=a.useMenuItem({interactive:!0,disabled:!0,ref:n,role:"option",index:c},s),d=t=>{t.stopPropagation(),t.preventDefault(),e()};return o.createElement(m.Button,{className:"dig-Typeahead-results--show-more",variant:"transparent",ref:n,type:"button",onClick:d,onKeyDown:t=>{"Enter"!==t.key&&" "!==t.key||(t.stopPropagation(),t.preventDefault(),e())},onMouseDown:d,onFocus:()=>{r(void 0)},...u(),disabled:!1,"aria-disabled":!1},t)};function K({results:e,title:t,renderRow:n,initialResults:a=4,maxResults:r=8,showMoreButtonText:i,size:l="standard"}){const{setFocused:c}=o.useContext(x),[u,m]=o.useState(Math.min(e.length,a)),[p,g]=o.useState();if(o.useEffect(()=>{m(Math.min(e.length,a))},[e,a]),!e||0===e.length)return null;const h=s("dig-Typeahead-results",{"dig-Typeahead-results--standard":"standard"===l,"dig-Typeahead-results--large":"large"===l});return o.createElement("div",{className:h},t?o.createElement(d.Text,{className:"dig-Typeahead-results--title",color:"faint",isBold:!0,size:"small","aria-hidden":"true"},t):o.createElement("div",{className:"dig-Typeahead-results--title-spacer",role:"presentation"}),e.slice(0,u).map((e,a)=>o.createElement(b.Provider,{key:a,value:{rowIndex:a,focusIndex:p,sectionTitle:t}},n(e))),u<e.length&&u!==r&&o.createElement(b.Provider,{value:{rowIndex:u+100}},o.createElement(B,{showMoreButtonText:i,onShowMoreClick:()=>{u<e.length&&(c(e[u]),g(u),m(Math.min(e.length,r)))}})))}B.displayName="ShowMore",K.displayName="Results";var A={Row:S,RowAccessory:M,RowContent:N,RowSubtitle:k,RowTitle:P,Wrapper:C,Container:D,Prompt:F,EmptyPrompt:O,Results:K};e.Typeahead=A,Object.defineProperty(e,"__esModule",{value:!0})}));
//# sourceMappingURL=pkg-dig-f.min.js-vflPMDtNu.map