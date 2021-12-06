// Auto-generated. Do not edit!

// (in-package indy-voice.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class IndyVoice {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data = null;
      this.moving = null;
    }
    else {
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = new Array(8).fill(0);
      }
      if (initObj.hasOwnProperty('moving')) {
        this.moving = initObj.moving
      }
      else {
        this.moving = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IndyVoice
    // Check that the constant length array field [data] has the right length
    if (obj.data.length !== 8) {
      throw new Error('Unable to serialize array field data - length must be 8')
    }
    // Serialize message field [data]
    bufferOffset = _arraySerializer.int16(obj.data, buffer, bufferOffset, 8);
    // Serialize message field [moving]
    bufferOffset = _serializer.int16(obj.moving, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IndyVoice
    let len;
    let data = new IndyVoice(null);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.int16(buffer, bufferOffset, 8)
    // Deserialize message field [moving]
    data.moving = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'indy-voice/IndyVoice';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '926d498bb3e9f898f2a3ff6ed5aff58c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16[8] data
    int16 moving
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IndyVoice(null);
    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = new Array(8).fill(0)
    }

    if (msg.moving !== undefined) {
      resolved.moving = msg.moving;
    }
    else {
      resolved.moving = 0
    }

    return resolved;
    }
};

module.exports = IndyVoice;
