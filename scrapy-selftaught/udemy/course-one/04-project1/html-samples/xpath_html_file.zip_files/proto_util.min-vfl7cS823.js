define(["require","exports"],(function(e,i){"use strict";Object.defineProperty(i,"__esModule",{value:!0}),i.protoJsToBrandingInfo=void 0;const o=e=>{var i,o;if(null==e)return;const r="image"===e.value?{".tag":"image",original_url:null===(i=e.image)||void 0===i?void 0:i.originalUrl}:"video"===e.value?{".tag":"video",original_url:null===(o=e.video)||void 0===o?void 0:o.originalUrl}:{".tag":"other"};return{picker_image:e.pickerImage,fallback_image_url:e.fallbackImageUrl,value:r}},r=e=>{if(null==e)return;const{graphic:i}=e;return{asset_id:e.assetId,color_hex:e.colorHex,graphic:o(i)}};i.protoJsToBrandingInfo=e=>{var i,o,n;if(null==e)return;const{backgroundAsset:a}=e;return{backgroundAsset:r(a),logoUrl:null===(i=e.logoUrl)||void 0===i?void 0:i.value,organizationName:null===(o=e.organizationName)||void 0===o?void 0:o.value,isEnhancedBrandingEnabled:null===(n=e.isEnhancedBrandingEnabled)||void 0===n?void 0:n.value}}}));
//# sourceMappingURL=proto_util.min.js-vfld-_UZy.map