define("metaserver/static/js/modules/clean/referrer_cleansing_redirect",["require","exports","tslib","sjcl","metaserver/static/js/modules/core/browser","metaserver/static/js/modules/core/cookies","metaserver/static/js/modules/core/uri"],(function(e,r,t,s,c,i,o){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.safe_open_tab_and_redirect=r.redirect=r.get_redirect_uri=void 0,s=t.__importStar(s),c=t.__importStar(c);const n=function(e){const r=s.codec.utf8String.toBits(i.Cookies.read("__Host-js_csrf")),t=new s.misc.hmac(r).encrypt(e);return s.codec.base64.fromBits(t)};function a(e){const r=o.URI.parse(e).getScheme();if(r&&!["http","https"].includes(r))return"#";const t=new o.URI({scheme:"https",authority:"www.dropbox.com",path:"/referrer_cleansing_redirect"});return t.setQuery({url:e,hmac:n(e)}),t}function _(e,r=window,t=!1){t&&(r.opener=null),c.redirect(a(e),r)}r.get_redirect_uri=a,r.redirect=_,r.safe_open_tab_and_redirect=function(e){_(e,c.unsafe_open_tab(""),!0)}}));
//# sourceMappingURL=pkg-referrer-cleansing-redirect.min.js-vflzYpUol.map