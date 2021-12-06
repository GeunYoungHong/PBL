;; Auto-generated. Do not edit!


(when (boundp 'indy-voice::IndyVoice)
  (if (not (find-package "INDY-VOICE"))
    (make-package "INDY-VOICE"))
  (shadow 'IndyVoice (find-package "INDY-VOICE")))
(unless (find-package "INDY-VOICE::INDYVOICE")
  (make-package "INDY-VOICE::INDYVOICE"))

(in-package "ROS")
;;//! \htmlinclude IndyVoice.msg.html


(defclass indy-voice::IndyVoice
  :super ros::object
  :slots (_data _moving ))

(defmethod indy-voice::IndyVoice
  (:init
   (&key
    ((:data __data) (make-array 8 :initial-element 0 :element-type :integer))
    ((:moving __moving) 0)
    )
   (send-super :init)
   (setq _data __data)
   (setq _moving (round __moving))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:moving
   (&optional __moving)
   (if __moving (setq _moving __moving)) _moving)
  (:serialization-length
   ()
   (+
    ;; int16[8] _data
    (* 2    8)
    ;; int16 _moving
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16[8] _data
     (dotimes (i 8)
       (write-word (elt _data i) s)
       )
     ;; int16 _moving
       (write-word _moving s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16[8] _data
   (dotimes (i (length _data))
     (setf (elt _data i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; int16 _moving
     (setq _moving (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get indy-voice::IndyVoice :md5sum-) "926d498bb3e9f898f2a3ff6ed5aff58c")
(setf (get indy-voice::IndyVoice :datatype-) "indy-voice/IndyVoice")
(setf (get indy-voice::IndyVoice :definition-)
      "int16[8] data
int16 moving

")



(provide :indy-voice/IndyVoice "926d498bb3e9f898f2a3ff6ed5aff58c")


