/*
 * Copyright 2015 Telefonica Investigación y Desarrollo, S.A.U
 *
 * This file is part of iotagent-json
 *
 * iotagent-json is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the License,
 * or (at your option) any later version.
 *
 * iotagent-json is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public
 * License along with iotagent-json.
 * If not, seehttp://www.gnu.org/licenses/.
 *
 * For those usages not covered by the GNU Affero General Public License
 * please contact with::[contacto@tid.es]
 */

const iotAgentIp = process.env.IOT_AGENT_IP || '10.100.111.54';
const contextBrokerIp = process.env.CONTEXT_BROKER_IP || '10.100.111.211';
const mqttIp = process.env.MQTT_IP || '10.100.111.54';
const mongodbIp = process.env.MONGODB_IP || '10.100.111.211';

var config = {};
/**
 * Configuration for the MQTT binding.
 */
config.mqtt = {
    host: mqttIp, // Updated from localhost
    port: 1883,
    protocol: 'mqtt',
    qos: 0,
    retain: false,
    retries: 5,
    retryTime: 5,
    keepalive: 60,
    avoidLeadingSlash: false,
    disabled: false
};

/**
 * Configuration for the AMQP binding.
 */
// config.amqp = {
//     host: amqpIp, // Updated from localhost
//     port: 31004,
//     exchange: 'iota-exchange',
//     queue: 'iotaqueue',
//     options: { durable: true },
//     disabled: false
// };

/**
 * Configuration for the HTTP transport binding.
 */
 /*
config.http = {
    port: 7896
};
*/
/**
 * Configuration for the IoT Agent.
 */
config.iota = {
    logLevel: 'DEBUG',
    timestamp: true,
    contextBroker: {
        host: contextBrokerIp,
        port: '31001',
        service: 'robotService',
    },
    server: {
        port: 31001
    },
    deviceRegistry: {
        type: 'mongodb'
    },
    mongodb: {
        host: mongodbIp,
        port: '31002',
        db: 'iotagent_mqtt'
    },
    types: {
        "RobotState": {
            "service": "robotService",
            "subservice": "/robot",
            "cbHost": contextBrokerIp, 
            "cbPort": "31001",
            "resource": "/iot/json",
            "attributes": [
                { "name": "x", "type": "Number" },
                { "name": "y", "type": "Number" },
                { "name": "angle", "type": "Number" },
                { "name": "timestamp", "type": "String" }
            ],
            "commands": [],
            "lazy": [],
            "staticAttributes": []
        }
    },
    service: 'robotService',
    subservice: '/robot',
    providerUrl: `http://${iotAgentIp}:31001`,
    deviceRegistrationDuration: 'P20Y',
    defaultType: 'RobotState',
    defaultResource: '/iot/json',
    explicitAttrs: false
};

config.jexlTransformations = {};
config.configRetrieval = false;
config.defaultKey = '1234';
config.defaultTransport = 'MQTT';

module.exports = config;
