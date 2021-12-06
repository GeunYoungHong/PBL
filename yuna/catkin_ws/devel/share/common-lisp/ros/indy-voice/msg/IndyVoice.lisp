; Auto-generated. Do not edit!


(cl:in-package indy-voice-msg)


;//! \htmlinclude IndyVoice.msg.html

(cl:defclass <IndyVoice> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 8 :element-type 'cl:fixnum :initial-element 0))
   (moving
    :reader moving
    :initarg :moving
    :type cl:fixnum
    :initform 0))
)

(cl:defclass IndyVoice (<IndyVoice>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IndyVoice>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IndyVoice)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name indy-voice-msg:<IndyVoice> is deprecated: use indy-voice-msg:IndyVoice instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <IndyVoice>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader indy-voice-msg:data-val is deprecated.  Use indy-voice-msg:data instead.")
  (data m))

(cl:ensure-generic-function 'moving-val :lambda-list '(m))
(cl:defmethod moving-val ((m <IndyVoice>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader indy-voice-msg:moving-val is deprecated.  Use indy-voice-msg:moving instead.")
  (moving m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IndyVoice>) ostream)
  "Serializes a message object of type '<IndyVoice>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'data))
  (cl:let* ((signed (cl:slot-value msg 'moving)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IndyVoice>) istream)
  "Deserializes a message object of type '<IndyVoice>"
  (cl:setf (cl:slot-value msg 'data) (cl:make-array 8))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i 8)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'moving) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IndyVoice>)))
  "Returns string type for a message object of type '<IndyVoice>"
  "indy-voice/IndyVoice")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IndyVoice)))
  "Returns string type for a message object of type 'IndyVoice"
  "indy-voice/IndyVoice")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IndyVoice>)))
  "Returns md5sum for a message object of type '<IndyVoice>"
  "926d498bb3e9f898f2a3ff6ed5aff58c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IndyVoice)))
  "Returns md5sum for a message object of type 'IndyVoice"
  "926d498bb3e9f898f2a3ff6ed5aff58c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IndyVoice>)))
  "Returns full string definition for message of type '<IndyVoice>"
  (cl:format cl:nil "int16[8] data~%int16 moving~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IndyVoice)))
  "Returns full string definition for message of type 'IndyVoice"
  (cl:format cl:nil "int16[8] data~%int16 moving~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IndyVoice>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IndyVoice>))
  "Converts a ROS message object to a list"
  (cl:list 'IndyVoice
    (cl:cons ':data (data msg))
    (cl:cons ':moving (moving msg))
))
