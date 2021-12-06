
(cl:in-package :asdf)

(defsystem "indy-voice-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IndyVoice" :depends-on ("_package_IndyVoice"))
    (:file "_package_IndyVoice" :depends-on ("_package"))
  ))