define(["require","exports","tslib","react","typescript/libraries/file-viewer/src/preview_archive/folder_entry_view","typescript/libraries/file-viewer/src/preview_archive/utils","typescript/libraries/file-viewer/src/preview_archive/file_entry_view","typescript/libraries/file-viewer/src/preview_error/preview_error","spectrum/media_table_skeleton/index","typescript/libraries/file-viewer/src/core/logging/actions","typescript/libraries/file-viewer/src/css/preview-archive.module.css","typescript/libraries/file-viewer/src/core/data/utils","typescript/libraries/file-viewer/src/core/data/selectors","typescript/libraries/file-viewer/src/toolbar/toolbar","typescript/libraries/file-viewer/src/plugins/types","typescript/libraries/file-viewer/src/core/errors"],(function(e,r,i,t,a,l,n,o,c,s,d,v,u,f,w,p){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.PreviewArchive=void 0,t=i.__importStar(t),d=i.__importStar(d);r.PreviewArchive=e=>{const{rivieraData:r,filePreviewUiData:i,dispatch:h,fileMetadata:y,fileViewerId:P,fileInfo:g,intl:E,onRenderFailed:m,onRenderSucceeded:b,sharedLinkInfo:F,height:_,config:A,previewKey:D,archiveFiles:I,fullFilePreviewUi:R,fullRivieraData:U,loggingSession:V,account:M,fileViewerUiData:T,toolbarPlugins:k,snackbarManagerPluginInstance:S}=e,{currentPath:N}=i,K=t.useRef("initial"),j=t.useRef(null),O=t.useMemo(()=>{if("loaded"===(null==r?void 0:r.rootEntry.state)&&i.currentPath)return v.getArchiveEntryAtPath(r.rootEntry.data,i.currentPath,P,D,h)},[r,i.currentPath,h,P,D]),x=null==r?void 0:r.rootEntry.state,C=null==g?void 0:g.file_id;t.useEffect(()=>{if(x&&x!==K.current){switch(x){case"errored":m();break;case"loaded":b(),h(s.logTTV(P)),h(s.logTTI(P));const e="loaded"===(null==r?void 0:r.rootEntry.state)&&r.rootEntry.data.isPasswordProtected;if(O&&g&&C&&!e){const{entry:e,parent:r}=O;if(!e.isDir&&r&&r.children&&i.currentPath){const e=i.currentPath.slice(0,i.currentPath.length-1),t=l.getFiles(r.children);"loaded"===M.state?l.getArchiveFiles(e,t,g,h,C,M.data):j.current=r=>{l.getArchiveFiles(e,t,g,h,C,r)}}}}K.current=x}},[P,x,h,m,b,F,O,g,D,r,C,i,M]),"loaded"===M.state&&j.current&&(j.current(M.data),j.current=null);const q=null==y?void 0:y.file_name,G=t.createElement(f.ConfigurableToolbar,{rootArchiveFileInformation:{fileName:q,previewKey:D},fileRivieraData:r,fileViewerUi:T,filePreviewUi:i,previewType:w.PreviewType.Archive,plugins:k,snackbarManagerPluginInstance:S});if("loaded"!==(null==r?void 0:r.rootEntry.state)||!O||!C||!g)return"errored"===(null==r?void 0:r.rootEntry.state)?t.createElement(o.PreviewRenderError,Object.assign({},e,{rivieraData:void 0,error:new p.FVError(p.FVErrorCode.Unknown)})):t.createElement(t.Fragment,null,t.createElement("div",{className:d.loadingScreen},t.createElement(c.MediaTableSkeleton,{numRows:10})));if(void 0===N)throw new Error("filePreviewUiData.currentPath is not defined");if(void 0===y)throw new Error("fileMetadata is not defined");const{entry:L}=O;return L.isDir?t.createElement(t.Fragment,null,t.createElement(a.FolderEntryView,{rootEntry:r.rootEntry.data,entry:L,currentPath:N,filePreviewUiData:i,fileViewerId:P,rootPreviewKey:D,dispatch:h,intl:E,height:_,config:A,rootFileInfo:g,archiveFiles:I,fullFilePreviewUi:R,fullRivieraData:U,loggingSession:V,account:M,callGetArchiveFiles:j}),G):r.rootEntry.data.isPasswordProtected||u.getArchiveFilesFetchedPreviewMetadata(I,C)?t.createElement(t.Fragment,null,t.createElement(n.FileEntryView,Object.assign({},e,{currentPath:N,rootArchiveFileInformation:{fileName:y.file_name,previewKey:D},isArchiveFilePasswordProtected:r.rootEntry.data.isPasswordProtected,rootFileId:C,entry:L}))):null},r.PreviewArchive.displayName="PreviewArchive",r.PreviewArchive.displayName="PreviewArchive"}));
//# sourceMappingURL=preview_archive.amd.min.js-vfl61ZL4L.map