define("metaserver/static/js/prod_assets_web_modules/dig-components/buttons",["exports","../classnames","focus-visible","react","./icons","./icons/src","./progress_indicators","../react-transition-group/CSSTransition","../common/extends","../common/Transition","react-dom"],(function(e,t,n,i,a,r,s,o,d,l,c){"use strict";var u=({href:e,disabled:t=!1,type:n})=>{const i={type:n};let a="button";return e?(a="a",i.href=e,i.role="button",i["aria-disabled"]=t):i.disabled=t,[a,i]};function g(e,t){switch(e){case"primary":return!t;case"opacity":case"outline":return t;default:return!1}}var p=i.forwardRef(({children:e,className:n,variant:o,inverse:d=!1,size:l="standard",withDropdownIcon:c=!1,withIconLeft:p,hasNoUnderline:m=!1,href:h,fullWidth:f=!1,isLoading:B=!1,disabled:v=B,_hasRightMargin:w,_hasCollapsedMargins:N,_hasSquaredSize:y=!1,type:b,...I},S)=>{if(f){if("transparent"===o)throw new Error("`fullWidth` can only be applied to non-transparent variants.");if("large"!==l&&"xlarge"!==l)throw new Error('`fullWidth` can only be applied to "large" and "xlarge" sizes.')}const[T,E]=u({href:h,disabled:v||B,type:b}),L=t("dig-Button",`dig-Button--${o}`,`dig-Button--${l}`,{"dig-Button--fullWidth":f,"dig-Button--isLoading":B,"dig-Button--withDropdownIcon":c,"dig-Button--withIconLeft":p,"dig-Button--hasNoUnderline":"transparent"===o&&m,"dig-Button--hasRightMargin":w,"dig-Button--hasCollapsedMargins":N,"dig-Button--hasSquaredSize":y,"dig-Button--inverse":d},n);return i.createElement(T,{className:L,ref:S,...E,...I},i.createElement("span",{className:"dig-Button-content"},p&&i.createElement("span",{className:"dig-Button-icon-left-wrapper"},p),e,c&&i.createElement(a.UIIcon,{className:"dig-Button-icon",src:r.ChevronDownLine,size:"small","data-testid":"digButtonDropdownIcon"})),B&&i.createElement("span",{className:"dig-Button-spinner","data-testid":"digButtonSpinner"},i.createElement(s.Spinner,{monochromatic:!0,inverse:g(o,d),size:"xsmall"})))});p.displayName="Button";var m=i.forwardRef(({children:e,className:n,disabled:s=!1,variant:o,inverse:d=!1,isRounded:l=!1,size:c="standard",withDropdownIcon:g=!1,href:p,type:m,...h},f)=>{const[B,v]=u({href:p,disabled:s,type:m});!g||!l||console.error("dig-components:","`withDropdownIcon` only applies to non-rounded icon buttons.");const w=t("dig-IconButton",`dig-IconButton--${o}`,`dig-IconButton--${c}`,{"dig-IconButton--inverse":d,"dig-IconButton--rounded":l,"dig-IconButton--withDropdownIcon":g&&!l},n);return i.createElement(B,{className:w,ref:f,...v,...h},i.createElement("span",{className:"dig-IconButton-content"},e,g&&!l&&i.createElement(a.UIIcon,{src:r.ChevronDownLine,size:"small","data-testid":"digIconButtonDropdownIcon"})))});m.displayName="IconButton";var h=i.forwardRef(({className:e,children:n,renderMenu:a,variant:r,inverse:s=!1,size:o="standard",fullWidth:d=!1,isLoading:l=!1,disabled:c=l,...u},g)=>{const m=t("dig-SplitButton",`dig-SplitButton--${r}`,`dig-SplitButton--${o}`,{"dig-SplitButton--fullWidth":d},e),h={buttonProps:{variant:r,size:o,inverse:s,disabled:c||l,className:"dig-SplitButton-menu-button",withDropdownIcon:!0,_hasSquaredSize:!0}};return i.createElement("span",{role:"group",className:m},i.createElement(p,{ref:g,className:"dig-SplitButton-button",variant:r,size:o,inverse:s,isLoading:l,disabled:c,...u,_hasRightMargin:"primary"===r||"opacity"===r,_hasCollapsedMargins:"outline"===r},n),a(h))});h.displayName="SplitButton";var f=i.forwardRef(({cursor:e="default",circular:n=!1,children:a,className:r,...s},o)=>{const d=t("dig-StylelessButton",r,{"dig-StylelessButton--pointer":"pointer"===e,"dig-StylelessButton--circular":n});return i.createElement("button",{className:d,ref:o,...s},i.createElement("span",{className:"dig-StylelessButton-content"},a))});f.displayName="StylelessButton",e.Button=p,e.IconButton=m,e.SplitButton=h,e.StylelessButton=f,Object.defineProperty(e,"__esModule",{value:!0})})),define("metaserver/static/js/prod_assets_web_modules/dig-components/typography",["exports","react","../classnames"],(function(e,t,n){"use strict";var i=t.forwardRef(({children:e,className:i,href:a,onClick:r,inverse:s=!1,hasNoUnderline:o=!1,isBold:d=!1,variant:l="primary",...c},u)=>{const g=n("dig-Link",i,{"dig-Link--primary":"primary"===l,"dig-Link--hasNoUnderline":o,"dig-Link--isBold":d,"dig-Link--inverse":s}),p={onClick:r};switch(typeof a){case"string":p.href=a;break;case"function":p.href="#",p.onClick=e=>{e.preventDefault(),a(e),r&&r(e)}}return t.createElement("a",{className:g,ref:u,...p,...c},e)});i.displayName="Link";var a=t.forwardRef(({variant:e="paragraph",tagName:i="span",children:a,className:r,color:s="standard",size:o="standard",isBold:d=!1,inverse:l=!1,monospace:c=!1,_withoutLineHeight:u,_withoutWrap:g,...p},m)=>{const h=n("dig-Text",`dig-Text--variant-${e}`,`dig-Text--size-${o}`,`dig-Text--color-${s}`,{"dig-Text--inverse":l,"dig-Text--isBold":d,"dig-Text--withoutLineheight":u,"dig-Text--withoutWrap":g,"dig-Text--monospace":c},r);return t.createElement(i,{ref:m,className:h,...p},a)});a.displayName="Text";var r=({tagName:e="h2",children:i,className:a,color:r="standard",size:s="standard",isBold:o=!1,inverse:d=!1,...l})=>{const c=n("dig-Title",`dig-Title--size-${s}`,`dig-Title--color-${r}`,{"dig-Title--isBold":o,"dig-Title--inverse":d},a);return t.createElement(e,{className:c,...l},i)};r.displayName="Title",e.Label=({className:e,children:i,...a})=>{const r=n("dig-Label",e);return t.createElement("label",{className:r,...a},i)},e.Link=i,e.Text=a,e.Title=r,Object.defineProperty(e,"__esModule",{value:!0})}));
//# sourceMappingURL=pkg-dig-d.min.js-vflMgjkb-.map