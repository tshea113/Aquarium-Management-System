(function(e){function t(t){for(var a,r,i=t[0],l=t[1],c=t[2],u=0,p=[];u<i.length;u++)r=i[u],Object.prototype.hasOwnProperty.call(s,r)&&s[r]&&p.push(s[r][0]),s[r]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(e[a]=l[a]);d&&d(t);while(p.length)p.shift()();return o.push.apply(o,c||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],a=!0,i=1;i<n.length;i++){var l=n[i];0!==s[l]&&(a=!1)}a&&(o.splice(t--,1),e=r(r.s=n[0]))}return e}var a={},s={app:0},o=[];function r(t){if(a[t])return a[t].exports;var n=a[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.m=e,r.c=a,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)r.d(n,a,function(t){return e[t]}.bind(null,a));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var c=0;c<i.length;c++)t(i[c]);var d=l;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"234a":function(e,t,n){},"56d7":function(e,t,n){"use strict";n.r(t);var a=n("2b0e"),s=n("bc3a"),o=n.n(s),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("app-navigation"),n("v-content",{attrs:{transition:"slide-x-transition"}},[n("router-view")],1)],1)},i=[],l=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("span",[n("v-navigation-drawer",{staticClass:"deep-orange darken-4",attrs:{app:"",dark:"","disable-resize-watcher":""},model:{value:e.drawer,callback:function(t){e.drawer=t},expression:"drawer"}},[n("v-list",{attrs:{nav:""}},[e._l(e.items,function(t,a){return[e.isLoggedIn(t.accountOnly)?n("v-list-item",{key:a,attrs:{link:""},on:{click:function(n){return n.stopPropagation(),e.navbarClick(t.title)}}},[n("v-list-item-icon",[n("v-icon",{domProps:{textContent:e._s(t.icon)}})],1),n("v-list-item-content",[n("v-list-item-title",{domProps:{textContent:e._s(t.title)}})],1)],1):e._e()]})],2)],1),n("v-app-bar",{staticClass:"elevation-5",attrs:{app:"",dense:"",color:"gray darken-4",dark:""}},[n("v-app-bar-nav-icon",{staticClass:"hidden-md-and-up",on:{click:function(t){e.drawer=!e.drawer}}}),n("v-spacer",{staticClass:"hidden-sm-and-down"}),e.isLoggedIn(!1)?n("v-btn",{staticClass:"hidden-sm-and-down mx-2",attrs:{dark:""},on:{click:function(t){return t.stopPropagation(),e.navbarClick("Login")}}},[e._v("\n          LOGIN\n        ")]):e._e(),e.isLoggedIn(!1)?n("v-btn",{staticClass:"hidden-sm-and-down mx-2",attrs:{dark:""},on:{click:function(t){return t.stopPropagation(),e.navbarClick("Sign Up")}}},[e._v("\n          SIGN UP\n        ")]):e._e(),e.isLoggedIn(!0)?n("v-btn",{staticClass:"hidden-sm-and-down mx-2",attrs:{dark:""},on:{click:function(t){return t.stopPropagation(),e.navbarClick("Account Info")}}},[e._v("\n          ACCOUNT\n        ")]):e._e(),e.isLoggedIn(!0)?n("v-btn",{staticClass:"hidden-sm-and-down mx-2",attrs:{dark:""},on:{click:function(t){return t.stopPropagation(),e.navbarClick("Logout")}}},[e._v("\n          LOGOUT\n        ")]):e._e(),n("login"),n("signup")],1)],1)},c=[],d=n("2f62"),u=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-dialog",{attrs:{persistent:"","max-width":"600px"},model:{value:this.loginScreen,callback:function(t){e.$set(this,"loginScreen",t)},expression:"this.loginScreen"}},[n("v-card",[n("v-toolbar",{staticClass:"elevation-5",attrs:{color:"deep-orange darken-4",prominent:"",dark:""}},[n("v-toolbar-title",{staticClass:"display-1 mx-4"},[e._v("Login")])],1),n("v-alert",{staticClass:"ma-1",attrs:{type:"error",dense:""},model:{value:e.alert,callback:function(t){e.alert=t},expression:"alert"}},[e._v("\n      "+e._s(e.err_msg)+"\n    ")]),n("v-card-text",[n("v-container",[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("v-text-field",{attrs:{outlined:"",label:"Email","prepend-inner-icon":"mdi-email",required:""},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-text-field",{attrs:{outlined:"",label:"Password","prepend-inner-icon":"mdi-key",type:"password",required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1)],1)],1)],1),n("v-card-actions",[n("div",{staticClass:"flex-grow-1"}),n("v-btn",{attrs:{color:"deep-orange darken-1",text:""},on:{click:this.closeLogin}},[e._v("Close")]),n("v-btn",{attrs:{color:"deep-orange darken-1",text:""},on:{click:e.login}},[e._v("Submit")])],1)],1)],1)},p=[],m={name:"Login",data(){return{email:"",password:"",err_msg:"",alert:!1}},computed:{...Object(d["c"])(["loginScreen"])},components:{},methods:{...Object(d["b"])(["setAccessToken","closeLogin"]),login(){this.alert=!1,this.$http.post("http://127.0.0.1:5000/login",{email:this.email,password:this.password}).then(e=>{this.setAccessToken(e.data.token),this.$router.push({path:"/dashboard"}),this.email="",this.password="",this.closeLogin()}).catch(e=>{e.response&&(this.err_msg=e.response.data.message,this.alert=!0)})}}},g=m,v=n("2877"),h=n("6544"),f=n.n(h),b=n("0798"),k=n("8336"),_=n("b0af"),w=n("99d9"),x=n("62ad"),S=n("a523"),C=n("169a"),y=n("0fd9"),V=n("8654"),L=n("71d9"),T=n("2a7f"),O=Object(v["a"])(g,u,p,!1,null,null,null),A=O.exports;f()(O,{VAlert:b["a"],VBtn:k["a"],VCard:_["a"],VCardActions:w["a"],VCardText:w["b"],VCol:x["a"],VContainer:S["a"],VDialog:C["a"],VRow:y["a"],VTextField:V["a"],VToolbar:L["a"],VToolbarTitle:T["a"]});var I=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-dialog",{attrs:{persistent:"","max-width":"600px"},model:{value:e.signupScreen,callback:function(t){e.signupScreen=t},expression:"signupScreen"}},[n("v-card",[n("v-toolbar",{staticClass:"elevation-5",attrs:{color:"deep-orange darken-4",prominent:"",dark:""}},[n("v-toolbar-title",{staticClass:"display-1 mx-4"},[e._v("Sign up")])],1),n("v-alert",{staticClass:"ma-1",attrs:{type:"error",dense:""},model:{value:e.alert,callback:function(t){e.alert=t},expression:"alert"}},[e._v("\n        "+e._s(e.err_msg)+"\n      ")]),n("v-alert",{staticClass:"ma-1",attrs:{type:"success",dense:""},model:{value:e.success,callback:function(t){e.success=t},expression:"success"}},[e._v("\n        "+e._s(e.succ_msg)+"\n      ")]),n("v-card-text",[n("v-container",[n("v-row",[n("v-col",{attrs:{cols:"12",sm:"6",md:"4"}},[n("v-text-field",{attrs:{outlined:"",label:"First Name",required:""},model:{value:e.first_name,callback:function(t){e.first_name=t},expression:"first_name"}})],1),n("v-col",{attrs:{cols:"12",sm:"6",md:"4"}},[n("v-text-field",{attrs:{outlined:"",label:"Last Name",required:""},model:{value:e.last_name,callback:function(t){e.last_name=t},expression:"last_name"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-text-field",{attrs:{outlined:"",label:"Email","prepend-inner-icon":"mdi-email",required:""},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-text-field",{attrs:{outlined:"",label:"Password","prepend-inner-icon":"mdi-key",type:"password",required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1)],1)],1)],1),n("v-card-actions",[n("div",{staticClass:"flex-grow-1"}),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:this.closeSignup}},[e._v("Close")]),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:e.signup}},[e._v("Submit")])],1)],1)],1)},j=[],P={name:"Signup",data(){return{first_name:"",last_name:"",email:"",password:"",err_msg:"",succ_msg:"",alert:!1,success:!1}},computed:{...Object(d["c"])(["signupScreen"])},components:{},methods:{...Object(d["b"])(["setAccessToken","closeSignup"]),signup(){this.alert=!1,this.success=!1,this.$http.post("http://127.0.0.1:5000/signup",{first_name:this.first_name,last_name:this.last_name,email:this.email,password:this.password}).then(e=>{this.succ_msg="Account successfully created!",this.success=!0}).catch(e=>{this.err_msg=e.response.data,this.alert=!0})}}},$=P,E=Object(v["a"])($,I,j,!1,null,null,null),N=E.exports;f()(E,{VAlert:b["a"],VBtn:k["a"],VCard:_["a"],VCardActions:w["a"],VCardText:w["b"],VCol:x["a"],VContainer:S["a"],VDialog:C["a"],VRow:y["a"],VTextField:V["a"],VToolbar:L["a"],VToolbarTitle:T["a"]});var q={name:"AppNavigation",data(){return{drawer:!1,loginWindow:!1,signupWindow:!1,items:[{title:"Login",icon:"mdi-login",accountOnly:!1},{title:"Sign Up",icon:"mdi-account-plus",accountOnly:!1},{title:"Logout",icon:"mdi-logout",accountOnly:!0}]}},computed:{...Object(d["c"])(["loginScreen","signupScreen","loggedIn"])},components:{Login:A,Signup:N},methods:{...Object(d["b"])(["openLogin","openSignup","logout"]),navbarClick(e){"Login"===e?this.openLogin():"Sign Up"===e?this.openSignup():"Logout"===e&&(this.logout(),this.$router.push({path:"/"}))},isLoggedIn(e){return this.loggedIn&&e||!this.loggedIn&&!e}}},M=q,U=n("40dc"),B=n("5bc1"),D=n("132d"),G=n("8860"),F=n("da13"),R=n("5d23"),W=n("34c3"),z=n("f774"),J=n("2fa4"),Q=Object(v["a"])(M,l,c,!1,null,"1c786fd4",null),Y=Q.exports;f()(Q,{VAppBar:U["a"],VAppBarNavIcon:B["a"],VBtn:k["a"],VIcon:D["a"],VList:G["a"],VListItem:F["a"],VListItemContent:R["a"],VListItemIcon:W["a"],VListItemTitle:R["b"],VNavigationDrawer:z["a"],VSpacer:J["a"]});var H={name:"App",components:{AppNavigation:Y}},K=H,X=n("7496"),Z=n("a75b"),ee=Object(v["a"])(K,r,i,!1,null,null,null),te=ee.exports;f()(ee,{VApp:X["a"],VContent:Z["a"]});var ne=n("8c4f"),ae=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("span",[n("welcome")],1)},se=[],oe=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-container",{staticStyle:{"max-height":"100vh"},attrs:{id:"welcome",fluid:"","fill-height":""}},[n("v-layout",{attrs:{"justify-center":"","align-center":"",column:"","pa-5":""}},[n("div",{staticClass:"display-2\n        font-weight-black\n        white--text\n        text-xs-center\n        mb-3",attrs:{id:"content"}},[e._v("\n      AQUARIUM MANAGEMENT SYSTEM\n    ")]),n("div",{staticClass:"headline\n        font-weight-bold\n        white--text\n        text-xs-center",attrs:{id:"content"}},[e._v("\n      The all-in-one solution for remote aquarium management.\n    ")])])],1)},re=[],ie={name:"welcome"},le=ie,ce=(n("6626"),n("a722")),de=Object(v["a"])(le,oe,re,!1,null,"5f5a0ee0",null),ue=de.exports;f()(de,{VContainer:S["a"],VLayout:ce["a"]});var pe={name:"home",components:{Welcome:ue}},me=pe,ge=Object(v["a"])(me,ae,se,!1,null,null,null),ve=ge.exports,he=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("span",[n("h1",[e._v(e._s(e.message))])])},fe=[],be={name:"dashboard",data(){return{message:""}},components:{},methods:{...Object(d["b"])(["fetchAccessToken"]),getInfo(){this.fetchAccessToken(),this.$http.get("http://127.0.0.1:5000/getDashboard",{headers:{Authorization:`Bearer ${this.$store.state.accessToken}`}}).then(e=>{this.message=e.data.message}).catch(e=>{this.message=e.response.data})}},beforeMount(){this.getInfo()}},ke=be,_e=Object(v["a"])(ke,he,fe,!1,null,null,null),we=_e.exports;a["a"].use(d["a"]);var xe=new d["a"].Store({state:{accessToken:null,loginScreen:!1,signupScreen:!1,loggedIn:!1},mutations:{updateAccessToken:(e,t)=>{e.accessToken=t},toggleLogin:(e,t)=>{e.loginScreen=t},toggleSignup:(e,t)=>{e.signupScreen=t}},actions:{setAccessToken({commit:e},t){localStorage.setItem("token",t),this.state.loggedIn=!0,e("updateAccessToken",t)},fetchAccessToken({commit:e}){localStorage.getItem("token")?this.state.loggedIn=!0:this.state.loggedIn=!1,e("updateAccessToken",localStorage.getItem("token"))},logout({commit:e}){localStorage.clear(),this.state.loggedIn=!1,e("updateAccessToken",null)},openLogin({commit:e}){e("toggleLogin",!0)},closeLogin({commit:e}){e("toggleLogin",!1)},openSignup({commit:e}){e("toggleSignup",!0)},closeSignup({commit:e}){e("toggleSignup",!1)}}});a["a"].use(ne["a"]);const Se=new ne["a"]({mode:"history",base:"",routes:[{path:"/",name:"home",component:ve},{path:"/dashboard",name:"dashboard",meta:{requiresAuth:!0},component:we},{path:"*",redirect:"/"}]});Se.beforeEach((e,t,n)=>{xe.dispatch("fetchAccessToken").then(t=>{e.matched.some(e=>e.meta.requiresAuth)?xe.state.loggedIn?"/"===e.path?n("/dashboard"):n():n("/"):"/"===e.path&&xe.state.loggedIn?n("/dashboard"):n()})});var Ce=Se,ye=n("f309");a["a"].use(ye["a"]);var Ve=new ye["a"]({icons:{iconfont:"mdi"}});a["a"].prototype.$http=o.a,a["a"].config.productionTip=!1,new a["a"]({router:Ce,vuetify:Ve,store:xe,render:e=>e(te)}).$mount("#app")},6626:function(e,t,n){"use strict";var a=n("234a"),s=n.n(a);s.a}});
//# sourceMappingURL=app.55ae2200.js.map