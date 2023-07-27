define(["require","exports","metaserver/static/js/modules/core/exception","metaserver/static/js/file_viewer/sdk_file_viewer/proto_to_stone_utils/proto_to_stone_util","metaserver/static/js/dropbox/proto/per_node_metadata/api_v2_meta"],(function(e,s,o,t,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0}),s.protoJsToFileData=void 0;const r=i.per_node_metadata.LinkNodeAction,l={[r.UNKNOWN_ACTION]:{".tag":"unknown_action"},[r.DEVICE_FOLDER_PRE_SETUP]:{".tag":"device_folder_pre_setup"},[r.LIFE_VAULT_PRE_SETUP]:{".tag":"life_vault_pre_setup"},[r.LIFE_VAULT_POST_SETUP]:{".tag":"life_vault_post_setup"},[r.PASSWORDS_PRE_SETUP]:{".tag":"passwords_pre_setup"},[r.PASSWORDS_POST_SETUP]:{".tag":"passwords_post_setup"}},_=e=>{var s,o,t,i,r,_,a,d,n;if(e)return{bypass_behaviors:e.bypassBehaviors?{is_vault:null===(s=e.bypassBehaviors.isVault)||void 0===s?void 0:s.value,is_device_folder:null===(o=e.bypassBehaviors.isDeviceFolder)||void 0===o?void 0:o.value}:void 0,suppress_delete:null===(t=e.suppressDelete)||void 0===t?void 0:t.value,suppress_move:null===(i=e.suppressMove)||void 0===i?void 0:i.value,suppress_ns_partition:null===(r=e.suppressNsPartition)||void 0===r?void 0:r.value,suppress_shared_link:null===(_=e.suppressSharedLink)||void 0===_?void 0:_.value,link_node:e.linkNode?{action:l[e.linkNode.action]}:void 0,hide_extension:null===(a=e.hideExtension)||void 0===a?void 0:a.value,suppress_remote_actions:null===(d=e.suppressRemoteActions)||void 0===d?void 0:d.value,suppress_share:null===(n=e.suppressShare)||void 0===n?void 0:n.value}};s.protoJsToFileData=e=>{let s,i,r,l;e.hasMountAccessPerms&&(s=e.mountAccessPerms),e.isLocked&&(i=e.lockInfo.isLockholder,r=e.lockInfo.lockholderName,l=e.lockInfo.tsLocked);const a=e.type;null==a&&o.reportStack("Object file type not recognized. Falling back to FileTypes.FILE",{exc_extra:{type:e.type}});let d=e.fqPath;""===d&&(d="/");let n=e.icon;return"/"===d&&(n="dropbox_32"),{bytes:e.sizeBytes,direct_blockserver_link:e.directBlockserverLink,event_type:0,ext:e.ext||"",file_id:e.fileId||"",href:e.href||"",icon:n,is_cloud_doc:!!e.isCloudDoc,is_dir:!!e.isDir,is_in_team_folder_tree:!!e.isInTeamFolderTree,is_in_vault_folder:!!e.isInVaultFolder,is_locked:!!e.isLocked,is_symlink:!!e.isSymlink,is_unmounted:!!e.isUnmounted,is_versionable:!0,last_modified_name:e.lastModifiedName,open_to_url:e.openToUrl,per_node_metadata:_(e.perNodeMetadata),read_only:!!e.readOnly,thumbnail_url_tmpl:e.thumbnailUrlTmpl,ts:e.ts,revision_id:e.revisionId||"",sjid:e.sjid,sort_key:e.sortKey,target_ns:e.targetNs||0,type:null!=a?a:0,ns_id:e.nsId,ns_path:e.nsPath,fq_path:d,_mount_access_perms:s,isDeleted:-1===e.sizeBytes,is_lockholder:i,lockholder_name:r,ts_locked:l,lock_info:e.isLocked?{is_lockholder:i,lockholder_name:r,ts_locked:l}:null,has_automated_rule:!!e.hasAutomatedRule,ago:e.modifiedAgo,agoFromLastActionByUserTs:e.agoFromLastActionByUserTs,preview:t.convertPreviewProtoToAPIV2(e.preview)}}}));
//# sourceMappingURL=model_types_utils.min.js-vflL0DAF5.map