"""Documentation    GENERATED FILE. DO NOT EDIT BY HAND run C_Test/SC_LTEL2/Sct/RobotTests/libs/sack/generate_robot_sack.sh to generate"""

from robot.libraries.BuiltIn import BuiltIn


class generated_messages(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.syscom = BuiltIn().get_library_instance('syscom_rammbock')

    def inner_list(self, name=None, size=None, type=None):
        self.syscom.array(size, type, name)

    def AasyslogControlsSetReqMsg(self, *header_fields):
        self.syscom.new_message('AasyslogControlsSetReqMsg', 'Syscom', 'header:msgId:0x085B', *header_fields)
        self.SAaSysLogCtrlParams('ctrlParams')

    def AasyslogControlsSetRespMsg(self, *header_fields):
        self.syscom.new_message('AasyslogControlsSetRespMsg', 'Syscom', 'header:msgId:0x085C', *header_fields)
        self.syscom.u32('status')
        self.SAaSysLogCtrlParams('ctrlParams')

    def AasyslogControlsGetReqMsg(self, *header_fields):
        self.syscom.new_message('AasyslogControlsGetReqMsg', 'Syscom', 'header:msgId:0x085D', *header_fields)
        self.syscom.u32('dummy')

    def AasyslogControlsGetRespMsg(self, *header_fields):
        self.syscom.new_message('AasyslogControlsGetRespMsg', 'Syscom', 'header:msgId:0x085E', *header_fields)
        self.syscom.u32('status')
        self.SAaSysLogCtrlParams('ctrlParams')

    def SyncNodeRespMsg(self, *header_fields):
        self.syscom.new_message('SyncNodeRespMsg', 'Syscom', 'header:msgId:0x0AA2', *header_fields)
        self.syscom.u32('reqRecBcnHigh')
        self.syscom.u32('reqRecBcnLow')
        self.syscom.u32('respSendBcnHigh')
        self.syscom.u32('respSendBcnLow')
        self.syscom.u32('cpuFreq')
        self.syscom.u32('nodeStatus')
        self.syscom.u32('appStatus')
        self.syscom.u32('transactionId')

    def DsphwapiUlTestmodelDigitalOutputReqMsg(self, *header_fields):
        self.syscom.new_message('DsphwapiUlTestmodelDigitalOutputReqMsg', 'Syscom', 'header:msgId:0x0B90', *header_fields)
        self.syscom.u32('bitAmount')
        self.syscom.u32('bitRate')
        self.syscom.u32('bitPattern')

    def DsphwapiUlTestmodelDigitalOutputRespMsg(self, *header_fields):
        self.syscom.new_message('DsphwapiUlTestmodelDigitalOutputRespMsg', 'Syscom', 'header:msgId:0x0B91', *header_fields)
        self.syscom.u32('status')

    def SrioConfigRespMsg(self, *header_fields):
        self.syscom.new_message('SrioConfigRespMsg', 'Syscom', 'header:msgId:0x0C47', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('addDriverInfo')

    def SrioConfigReqMsg(self, *header_fields):
        self.syscom.new_message('SrioConfigReqMsg', 'Syscom', 'header:msgId:0x0C48', *header_fields)
        self.syscom.u32('skipMulticastCfg')
        self.syscom.u32('skipDaisyChainCfg')
        self.syscom.u32('skipSysComRegCfg')
        self.SSrioMultiCastConfig('multiCastConfig')
        self.SSrioDaisyChainConfig('daisyChainConfig')
        self.syscom.u32('sysComRegTx')
        self.SSrioSysComRegTxConfig('sysComRegTxConfig')
        self.syscom.u32('sysComRegRx')
        self.SSrioSysComRegRxConfig('sysComRegRxConfig')
        self.SSrioBoardPresenceConfig('boardPresenceConfig')

    def SrioInitRespMsg(self, *header_fields):
        self.syscom.new_message('SrioInitRespMsg', 'Syscom', 'header:msgId:0x0C49', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('addDriverInfo')

    def SrioInitReqMsg(self, *header_fields):
        self.syscom.new_message('SrioInitReqMsg', 'Syscom', 'header:msgId:0x0C4A', *header_fields)
        self.syscom.u32('srioMasterCoreNo')
        self.SSrioPhysicalPara('physicalPara')
        self.syscom.u32('msgFragPrio')
        self.syscom.array('16', 'u32', 'resourceConfig')

    def AamemdspPoolInfoReqMsg(self, *header_fields):
        self.syscom.new_message('AamemdspPoolInfoReqMsg', 'Syscom', 'header:msgId:0x0C4D', *header_fields)
        self.syscom.u32('poolType')
        self.syscom.u32('poolIndex')

    def AamemdspPoolStatusReqMsg(self, *header_fields):
        self.syscom.new_message('AamemdspPoolStatusReqMsg', 'Syscom', 'header:msgId:0x0C4F', *header_fields)
        self.syscom.i32('poolId')

    def AamemdspPoolStatusRespMsg(self, *header_fields):
        self.syscom.new_message('AamemdspPoolStatusRespMsg', 'Syscom', 'header:msgId:0x0C50', *header_fields)
        self.syscom.u32('rc')
        self.syscom.u32('numOfPools')
        self.syscom.array('1', 'SAaMemDspPoolStatus', 'statuses')

    def AatraceMonCtrlRespMsg(self, *header_fields):
        self.syscom.new_message('AatraceMonCtrlRespMsg', 'Syscom', 'header:msgId:0x1813', *header_fields)
        self.syscom.u32('successCode')

    def AatraceMonCtrlReqMsg(self, *header_fields):
        self.syscom.new_message('AatraceMonCtrlReqMsg', 'Syscom', 'header:msgId:0x1819', *header_fields)
        self.SAaTraceMonCtrlParams('sAaTraceMonCtrlParams')

    def BrowserIdleMeasurementReq(self, *header_fields):
        self.syscom.new_message('BrowserIdleMeasurementReq', 'Syscom', 'header:msgId:0x1BE6', *header_fields)
        self.syscom.u32('spare')

    def BrowserIdleMeasurementAck(self, *header_fields):
        self.syscom.new_message('BrowserIdleMeasurementAck', 'Syscom', 'header:msgId:0x1BE7', *header_fields)
        self.syscom.u32('idleLoad')
        self.syscom.u32('minIdleLoad')

    def BrowserDspMemoryReq(self, *header_fields):
        self.syscom.new_message('BrowserDspMemoryReq', 'Syscom', 'header:msgId:0x1BEB', *header_fields)
        self.syscom.u32('writeData')
        self.syscom.u32('dataCount')
        self.syscom.u32('dspDataAddress')
        self.syscom.array('1', 'u8', 'dspData')

    def BrowserDspMemoryAck(self, *header_fields):
        self.syscom.new_message('BrowserDspMemoryAck', 'Syscom', 'header:msgId:0x1BEC', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('dataCount')
        self.syscom.u32('dspDataAddress')
        self.syscom.array('1', 'u8', 'dspData')

    def AaconfigRadSetParamsReqMsg(self, *header_fields):
        self.syscom.new_message('AaconfigRadSetParamsReqMsg', 'Syscom', 'header:msgId:0x2011', *header_fields)
        self.syscom.u32('domain')
        self.syscom.u32('settingType')
        self.syscom.u32('noOfParams')
        self.syscom.array('1', 'SAaConfigRadParams', 'params')

    def AaconfigRadSetParamsRespMsg(self, *header_fields):
        self.syscom.new_message('AaconfigRadSetParamsRespMsg', 'Syscom', 'header:msgId:0x2012', *header_fields)
        self.syscom.u32('domain')
        self.syscom.u32('paramState')

    def PhyPdcchSendReqMsg(self, *header_fields):
        self.syscom.new_message('PhyPdcchSendReqMsg', 'Syscom', 'header:msgId:0x2102', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.SPdcchSendReqBuffer('requestMsg')

    def PhyPrachReceiveIndMsg(self, *header_fields):
        self.syscom.new_message('PhyPrachReceiveIndMsg', 'Syscom', 'header:msgId:0x2104', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('preambleFra')
        self.syscom.real32('interferencePower')
        self.syscom.u8('numOfSubCell')
        self.syscom.u8('explicitPadding1')
        self.syscom.u16('explicitPadding2')
        self.syscom.array('6', 'SSubCellMeasurement', 'subCellMeasurement')
        self.syscom.u32('numOfPreamble')
        self.syscom.array('numOfPreamble', 'SPrachPreamble', 'preamble')

    def PhyPuschReceiveReqMsg(self, *header_fields):
        self.syscom.new_message('PhyPuschReceiveReqMsg', 'Syscom', 'header:msgId:0x2106', *header_fields)
        self.SPhyDataHeader('header')
        self.SPuschReceiveReq('message')

    def PhyPuschReceiveRespUMsg(self, *header_fields):
        self.syscom.new_message('PhyPuschReceiveRespUMsg', 'Syscom', 'header:msgId:0x2108', *header_fields)
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u16('lastMsgInTti')
        self.syscom.u16('numOfRespUsInTti')
        self.syscom.u32('numOfUePuschResp')
        self.syscom.array('numOfUePuschResp', 'SPuschUeResp', 'uePuschResp')

    def TupResumeUlTxReqMsg(self, *header_fields):
        self.syscom.new_message('TupResumeUlTxReqMsg', 'Syscom', 'header:msgId:0x2109', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def PhyPhichSendReqMsg(self, *header_fields):
        self.syscom.new_message('PhyPhichSendReqMsg', 'Syscom', 'header:msgId:0x210C', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.SPhichSendReqBuffer('requestMsg')

    def MacCellReconfigurationReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellReconfigurationReqMsg', 'Syscom', 'header:msgId:0x21D1', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('activationTimeSFN')
        self.SCommonCellParams('commonCellParams')
        self.SPhichParams('phichParams')
        self.SPucchConfiguration('pucchParams')
        self.SSoundingRsUlConfigCommon('soundingRsUlConfigCommon')
        self.syscom.u32('hsTrainScenario')
        self.syscom.u32('harqMaxMsg3')
        self.UWmpDcmCellContainer('container')

    def MacCellReconfigurationRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellReconfigurationRespMsg', 'Syscom', 'header:msgId:0x21D2', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacUserModifyReqMsg(self, *header_fields):
        self.syscom.new_message('MacUserModifyReqMsg', 'Syscom', 'header:msgId:0x21D5', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('measGapStopRequired')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('hasAmbrParams')
        self.SAmbrParams('ambrParams')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('hasActNewTransmMode')
        self.syscom.u32('actNewTransmMode')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeInactivityTimer')
        self.syscom.u32('ueInactivityTimer')
        self.syscom.u32('hasTargetBLER')
        self.STargetBLER('targetBLER')
        self.syscom.u32('hasThroughputThresholdMonitoring')
        self.SThroughputThresholdMonitoring('throughputThresholdMonitoring')
        self.syscom.u32('hasConfigId')
        self.syscom.u32('configId')
        self.syscom.u32('hasHarqMaxTrDl')
        self.syscom.u32('harqMaxTrDl')
        self.syscom.u32('hasHarqMaxTrUl')
        self.syscom.u32('harqMaxTrUl')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasUlSpsConfigDedicated')
        self.SUlSpsConfigDedicated('ulSpsConfigDedicated')
        self.syscom.u32('hasEnableNonGbrBufferMonitoring')
        self.syscom.u32('enableNonGbrBufferMonitoring')

    def MacUserModifyRespMsg(self, *header_fields):
        self.syscom.new_message('MacUserModifyRespMsg', 'Syscom', 'header:msgId:0x21D6', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')

    def MacTxAntennaConfChangeReqMsg(self, *header_fields):
        self.syscom.new_message('MacTxAntennaConfChangeReqMsg', 'Syscom', 'header:msgId:0x21F3', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numAvailableTxAntennas')

    def MacTxAntennaConfChangeRespMsg(self, *header_fields):
        self.syscom.new_message('MacTxAntennaConfChangeRespMsg', 'Syscom', 'header:msgId:0x21F4', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacCellDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellDeleteReqMsg', 'Syscom', 'header:msgId:0x2208', *header_fields)
        self.syscom.u32('lnCelId')

    def MacCellDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellDeleteRespMsg', 'Syscom', 'header:msgId:0x2209', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacCellSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellSetupReqMsg', 'Syscom', 'header:msgId:0x220A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('phyCellId')
        self.SCommonCellParams('commonCellParams')
        self.SPhichParams('phichParams')
        self.SPucchConfiguration('pucchParams')
        self.SSoundingRsUlConfigCommon('soundingRsUlConfigCommon')
        self.syscom.u32('hsTrainScenario')
        self.syscom.u32('harqMaxMsg3')
        self.SBufferDiscardParams('bufferDiscardParams')
        self.syscom.u32('hasVoLteThresholdParams')
        self.SVoLteThresholdParams('voLteThresholdParams')
        self.syscom.u32('numOfRlcDlLcpInfo')
        self.syscom.array('16', 'SRlcLcpInfo', 'rlcDlLcpInfo')
        self.syscom.u32('resourcePoolGroupId')
        self.syscom.u32('cellMode')
        self.SCellSlotConf('cellSlotConf')
        self.syscom.u32('numOfScellCandidate')
        self.syscom.array('24', 'u32', 'lnCellIdSCellCandidate')
        self.UWmpDcmCellContainer('container')

    def MacCellSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellSetupRespMsg', 'Syscom', 'header:msgId:0x220B', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('macUser')
        self.syscom.u32('macSgnl')
        self.syscom.u32('macCellMeas')
        self.syscom.u32('macTest')
        self.syscom.u32('macUserPsService')
        self.syscom.u32('macCellPsService')
        self.syscom.u32('macUserL2')
        self.syscom.u32('numOfTestabilityServices')
        self.syscom.array('numOfTestabilityServices', 'SServiceInfo', 'serviceInfo')

    def MacDefaultUserConfigReqMsg(self, *header_fields):
        self.syscom.new_message('MacDefaultUserConfigReqMsg', 'Syscom', 'header:msgId:0x2211', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('l3Address')
        self.SUserInfoMac('userInfo')

    def MacDefaultUserConfigRespMsg(self, *header_fields):
        self.syscom.new_message('MacDefaultUserConfigRespMsg', 'Syscom', 'header:msgId:0x2212', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('numOfNodeAddress')
        self.syscom.array('numOfNodeAddress', 'u16', 'nodeAddress')

    def MacRadioBearerDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerDeleteReqMsg', 'Syscom', 'header:msgId:0x2214', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'u32', 'sRbList')
        self.syscom.u32('numOfAbnormallyReleasedDRbList')
        self.syscom.array('8', 'u32', 'abnormallyReleasedDRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'u32', 'dRbList')

    def MacRadioBearerDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerDeleteRespMsg', 'Syscom', 'header:msgId:0x2215', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def MacRadioBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerSetupReqMsg', 'Syscom', 'header:msgId:0x2216', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SRbInfo', 'drbInfoList')

    def MacRadioBearerSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerSetupRespMsg', 'Syscom', 'header:msgId:0x2217', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def MacUserDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacUserDeleteReqMsg', 'Syscom', 'header:msgId:0x221C', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('validUeId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('numOfAbnormallyReleasedDRbList')
        self.syscom.array('8', 'u32', 'abnormallyReleasedDRbList')
        self.syscom.u32('hasUeReleaseCause')
        self.syscom.u32('ueReleaseCause')
        self.syscom.u32('hasSpecificUeReleaseCause')
        self.syscom.u32('specificUeReleaseCause')

    def MacUserDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacUserDeleteRespMsg', 'Syscom', 'header:msgId:0x221D', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def MacUserSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacUserSetupReqMsg', 'Syscom', 'header:msgId:0x2221', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfScellIds')
        self.syscom.array('2', 'u32', 'lnCelIdSCell')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('handoverType')
        self.SUeSetupParams('ueSetupParams')
        self.UWmpDcmUserContainer('container')
        self.SCqiParams('cqiParams')
        self.SPuschControlOffsets('controlOffsets')
        self.SUeParams('ueParams')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('intraCellInterDataPoolEnabled')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasUlPCUeParams')
        self.SUlPCUeParams('ulPCUeParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')

    def MacUserSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacUserSetupRespMsg', 'Syscom', 'header:msgId:0x2222', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('poolIdPCell')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u32('dlGtpuSicad')
        self.SGcadAddress('dlL2Gcad')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('macUserAddress')
        self.syscom.u32('raPreambleIndex')
        self.syscom.u32('prachMaskIndex')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def MacCellReconfigurationDeltaReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellReconfigurationDeltaReqMsg', 'Syscom', 'header:msgId:0x2223', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('hasDcmContainer')
        self.UWmpDcmCellReconfigurationContainer('dcmContainer')

    def MacCellReconfigurationDeltaRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellReconfigurationDeltaRespMsg', 'Syscom', 'header:msgId:0x2224', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacUeInfoReqMsg(self, *header_fields):
        self.syscom.new_message('MacUeInfoReqMsg', 'Syscom', 'header:msgId:0x2236', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ueInfo')

    def MacUeInfoRespMsg(self, *header_fields):
        self.syscom.new_message('MacUeInfoRespMsg', 'Syscom', 'header:msgId:0x2237', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.UUeInfo('ueInfo')

    def TupCellDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('TupCellDeleteReqMsg', 'Syscom', 'header:msgId:0x2239', *header_fields)
        self.syscom.u32('lnCelId')

    def TupCellDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TupCellDeleteRespMsg', 'Syscom', 'header:msgId:0x223A', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def TupCellSetupReqMsg(self, *header_fields):
        self.syscom.new_message('TupCellSetupReqMsg', 'Syscom', 'header:msgId:0x223B', *header_fields)
        self.syscom.u32('lnCelId')
        self.SPlmnId('primaryPLMNId')
        self.SRohcCellParameters('rohcCellParameters')
        self.syscom.u32('sysTimeCorrectValue')
        self.STupDiscardParameters('bufferDiscardParams')

    def TupCellSetupRespMsg(self, *header_fields):
        self.syscom.new_message('TupCellSetupRespMsg', 'Syscom', 'header:msgId:0x223C', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('tupUserAddress')
        self.syscom.u32('tupSgnlSrbAddress')
        self.syscom.u32('tupCellMeas')
        self.syscom.u32('trswDataMbmsClientSicad')
        self.SGcadAddress('trswDataMbmsClientGcad')

    def MacStartRefSyncSReqMsg(self, *header_fields):
        self.syscom.new_message('MacStartRefSyncSReqMsg', 'Syscom', 'header:msgId:0x229F', *header_fields)
        self.syscom.u32('lnCelId')

    def MacStartRefSyncSRespMsg(self, *header_fields):
        self.syscom.new_message('MacStartRefSyncSRespMsg', 'Syscom', 'header:msgId:0x22A0', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacStopRefSyncSReqMsg(self, *header_fields):
        self.syscom.new_message('MacStopRefSyncSReqMsg', 'Syscom', 'header:msgId:0x22A1', *header_fields)
        self.syscom.u32('lnCelId')

    def MacStopRefSyncSRespMsg(self, *header_fields):
        self.syscom.new_message('MacStopRefSyncSRespMsg', 'Syscom', 'header:msgId:0x22A2', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def TupBearerDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TupBearerDeleteRespMsg', 'Syscom', 'header:msgId:0x2340', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('1', 'STupSrbInfoResp', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def TupBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('TupBearerSetupReqMsg', 'Syscom', 'header:msgId:0x2341', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSecurityInformation')
        self.STupSecurityInformation('securityInformation')
        self.syscom.u32('uecategory')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('1', 'STupSrbInfo', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoBearerSetup', 'rbList')

    def TupBearerSetupRespMsg(self, *header_fields):
        self.syscom.new_message('TupBearerSetupRespMsg', 'Syscom', 'header:msgId:0x2342', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('1', 'STupSrbInfoResp', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def TupErrorIndMsg(self, *header_fields):
        self.syscom.new_message('TupErrorIndMsg', 'Syscom', 'header:msgId:0x2346', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('interfaceInfo')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('1', 'STupSrbInfoResp', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def TupSrbSendReqMsg(self, *header_fields):
        self.syscom.new_message('TupSrbSendReqMsg', 'Syscom', 'header:msgId:0x234F', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasDrxConfigId')
        self.syscom.u32('drxConfigId')
        self.syscom.u32('srbId')
        self.syscom.u32('respFlag')
        self.syscom.u32('harqRespFlag')
        self.syscom.u32('mui')
        self.syscom.u32('integrityActivationPreFlag')
        self.syscom.u32('dlCipherActivationPostFlag')
        self.syscom.u32('numOfL3Payload')
        self.syscom.array('4', 'u8', 'l3Payload')

    def TupSrbSendRespMsg(self, *header_fields):
        self.syscom.new_message('TupSrbSendRespMsg', 'Syscom', 'header:msgId:0x2350', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('srbId')
        self.syscom.u32('mui')
        self.syscom.u32('numOfL3Payload')
        self.syscom.array('1', 'u8', 'l3Payload')

    def TupUserDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('TupUserDeleteReqMsg', 'Syscom', 'header:msgId:0x2351', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupUserDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TupUserDeleteRespMsg', 'Syscom', 'header:msgId:0x2352', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupUserSetupReqMsg(self, *header_fields):
        self.syscom.new_message('TupUserSetupReqMsg', 'Syscom', 'header:msgId:0x2353', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('tupUserAddress')
        self.syscom.u32('tupSgnlSrbAddress')
        self.syscom.u32('macUserAddr')
        self.syscom.u32('handoverType')
        self.syscom.u32('sourceUeId')
        self.syscom.u32('sourceCellId')
        self.syscom.u32('suspendUlTx')
        self.syscom.u32('uecategory')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('2', 'STupSrbInfo', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoUserSetup', 'rbList')

    def TupUserSetupRespMsg(self, *header_fields):
        self.syscom.new_message('TupUserSetupRespMsg', 'Syscom', 'header:msgId:0x2354', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('2', 'STupSrbInfoResp', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def MacCcchDataReceiveIndMsg(self, *header_fields):
        self.syscom.new_message('MacCcchDataReceiveIndMsg', 'Syscom', 'header:msgId:0x235E', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('maxNumOfUes')
        self.syscom.array('1', 'SMsg3Info', 'msg3Info')

    def MacCcchDataSendReqMsg(self, *header_fields):
        self.syscom.new_message('MacCcchDataSendReqMsg', 'Syscom', 'header:msgId:0x235F', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('size')
        self.syscom.array('1', 'u8', 'data')

    def MacInternalAddressReqMsg(self, *header_fields):
        self.syscom.new_message('MacInternalAddressReqMsg', 'Syscom', 'header:msgId:0x2360', *header_fields)
        self.syscom.u32('transactionId')
        self.SNodeAddress('nodeAddress')
        self.syscom.u16('paddingNodeAddress')

    def MacInternalAddressRespMsg(self, *header_fields):
        self.syscom.new_message('MacInternalAddressRespMsg', 'Syscom', 'header:msgId:0x2361', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('transactionId')

    def MacRachSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacRachSetupReqMsg', 'Syscom', 'header:msgId:0x2375', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('lCelId')
        self.SRachParams('rachParams')

    def MacRachSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacRachSetupRespMsg', 'Syscom', 'header:msgId:0x2376', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('hasContainer')
        self.SWmpDcmCaParamsContainer('container')

    def PhyDlPhyDataAddressReqMsg(self, *header_fields):
        self.syscom.new_message('PhyDlPhyDataAddressReqMsg', 'Syscom', 'header:msgId:0x237A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('dlErrorIndAddress')
        self.syscom.u32('pdschRejectedIndAddress')
        self.syscom.u32('pdschErrorIndAddress')

    def PhyDlPhyDataAddressRespMsg(self, *header_fields):
        self.syscom.new_message('PhyDlPhyDataAddressRespMsg', 'Syscom', 'header:msgId:0x237B', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('status')
        self.SDlPhyDataAddressInfo('dlPhyDataAddressInfo')

    def PhyUlPhyDataAddressReqMsg(self, *header_fields):
        self.syscom.new_message('PhyUlPhyDataAddressReqMsg', 'Syscom', 'header:msgId:0x237D', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('prachReceiveIndAddress')
        self.syscom.u32('puschReceiveMeasRespAddress1')
        self.syscom.u32('puschReceiveMeasRespAddress2')
        self.syscom.u32('puschReceiveRespUAddress2')
        self.syscom.u32('pucchReceiveMeasRespAddress1')
        self.syscom.u32('pucchReceiveMeasRespAddress2')
        self.syscom.u32('pucchReceiveRespUAddress')
        self.syscom.u32('srsReceiveRespDAddress')
        self.syscom.u32('srsReceiveRespUAddress')
        self.syscom.u32('puschCellMeasRespAddress')
        self.syscom.u32('pucchCellMeasRespAddress')
        self.syscom.u32('srsCellMeasRespAddress')
        self.syscom.u32('srsBfCovMatrixMeasRespAddress')
        self.syscom.u32('ulResourceUpdateAddress')
        self.syscom.u32('pucchFoMeasRespAddress')
        self.syscom.u32('pucchToMeasRespAddress')
        self.syscom.u32('pucchPwrMeasRespAddress')

    def PhyUlPhyDataAddressRespMsg(self, *header_fields):
        self.syscom.new_message('PhyUlPhyDataAddressRespMsg', 'Syscom', 'header:msgId:0x237E', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('status')
        self.SUlPhyDataAddressInfo('ulPhyDataAddressInfo')
        self.syscom.u32('stWeightVectorAddr')
        self.syscom.u32('numOfSubPools')
        self.syscom.array('2', 'SUlAddrGroupInSubPool', 'ulAddrGroupInSubpool')

    def SimResetReqMsg(self, *header_fields):
        self.syscom.new_message('SimResetReqMsg', 'Syscom', 'header:msgId:0x2418', *header_fields)
        self.syscom.u32('spare')

    def MacMeasurementReportIndMsg(self, *header_fields):
        self.syscom.new_message('MacMeasurementReportIndMsg', 'Syscom', 'header:msgId:0x2486', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')
        self.syscom.u32('poolIdSource')
        self.syscom.u32('startSfn')
        self.syscom.u32('numOfMeasurementGroupTypeList')
        self.syscom.array('27', 'u32', 'measurementGroupTypeList')
        self.syscom.u32('numOfMeasReportValue')
        self.syscom.array('numOfMeasReportValue', 'SMeasReportValue', 'measReportValue')

    def TupDataForwardDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('TupDataForwardDeleteReqMsg', 'Syscom', 'header:msgId:0x248F', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('handoverStatusFlag')

    def TupDataForwardDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TupDataForwardDeleteRespMsg', 'Syscom', 'header:msgId:0x2490', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupDataForwardSetupReqMsg(self, *header_fields):
        self.syscom.new_message('TupDataForwardSetupReqMsg', 'Syscom', 'header:msgId:0x2491', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('destinationUeId')
        self.syscom.u16('destinationUeIndex')
        self.syscom.u16('paddingDestinationUeIndex')
        self.syscom.u32('destinationCellId')
        self.syscom.u32('destinationPoolId')
        self.syscom.u32('transactionId')
        self.syscom.u32('handoverType')
        self.syscom.u32('dcmDlInterRatFoType')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoDataForwardSetup', 'rbList')

    def TupDataForwardSetupRespMsg(self, *header_fields):
        self.syscom.new_message('TupDataForwardSetupRespMsg', 'Syscom', 'header:msgId:0x2492', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoDataForwardSetupResp', 'rbList')

    def TupDataPathSupervisionReqMsg(self, *header_fields):
        self.syscom.new_message('TupDataPathSupervisionReqMsg', 'Syscom', 'header:msgId:0x2493', *header_fields)
        self.syscom.u32('enbcDatapathStatusAddress')
        self.syscom.u32('trswConfigSicad')
        self.syscom.u32('initialStatusReportRequested')
        self.STransportLayerAddress('uPlaneIpAddress')
        self.syscom.u32('gtpuPathSupint')
        self.syscom.u32('gtpuT3Resp')
        self.syscom.u32('gtpuN3Reqs')
        self.syscom.u32('transportNwId')
        self.syscom.u32('numOfSgwIpAddress')
        self.syscom.array('numOfSgwIpAddress', 'STransportLayerAddress', 'sgwIpAddress')

    def TupDataPathSupervisionRespMsg(self, *header_fields):
        self.syscom.new_message('TupDataPathSupervisionRespMsg', 'Syscom', 'header:msgId:0x2494', *header_fields)
        self.SMessageResult('messageResult')

    def TupEndMarkerIndMsg(self, *header_fields):
        self.syscom.new_message('TupEndMarkerIndMsg', 'Syscom', 'header:msgId:0x2495', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('drbId')
        self.syscom.u32('direction')

    def TupPdcpEnableReqMsg(self, *header_fields):
        self.syscom.new_message('TupPdcpEnableReqMsg', 'Syscom', 'header:msgId:0x2499', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('handoverType')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoPdcpEnable', 'rbList')

    def TupPdcpEnableRespMsg(self, *header_fields):
        self.syscom.new_message('TupPdcpEnableRespMsg', 'Syscom', 'header:msgId:0x249A', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def PhyPuschReceiveMeasRespMsg(self, *header_fields):
        self.syscom.new_message('PhyPuschReceiveMeasRespMsg', 'Syscom', 'header:msgId:0x24B1', *header_fields)
        self.SPhyDataHeader('header')
        self.SPuschReceiveMeasResp('message')

    def PhySrsReceiveReqMsg(self, *header_fields):
        self.syscom.new_message('PhySrsReceiveReqMsg', 'Syscom', 'header:msgId:0x24B2', *header_fields)
        self.SPhyDataHeader('header')
        self.SSrsReceiveReq('message')

    def PhySrsReceiveRespUMsg(self, *header_fields):
        self.syscom.new_message('PhySrsReceiveRespUMsg', 'Syscom', 'header:msgId:0x24B4', *header_fields)
        self.SPhyDataHeader('header')
        self.SSrsReceiveRespU('message')

    def MacL2CallConfigReqMsg(self, *header_fields):
        self.syscom.new_message('MacL2CallConfigReqMsg', 'Syscom', 'header:msgId:0x24C4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfScellIds')
        self.syscom.array('2', 'u32', 'lnCelIdSCell')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('handoverType')
        self.SUeSetupParams('ueSetupParams')
        self.UWmpDcmUserContainer('container')
        self.SCqiParams('cqiParams')
        self.SPuschControlOffsets('controlOffsets')
        self.SUeParams('ueParams')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('intraCellInterDataPoolEnabled')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasUlPCUeParams')
        self.SUlPCUeParams('ulPCUeParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')

    def MacL2CallConfigRespMsg(self, *header_fields):
        self.syscom.new_message('MacL2CallConfigRespMsg', 'Syscom', 'header:msgId:0x24C5', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('poolIdPCell')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u32('dlGtpuSicad')
        self.SGcadAddress('dlL2Gcad')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('macUserAddress')
        self.syscom.u32('raPreambleIndex')
        self.syscom.u32('prachMaskIndex')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def MacRadioBearerReleaseIndMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerReleaseIndMsg', 'Syscom', 'header:msgId:0x2610', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('cellResourceGroupId')
        self.syscom.u32('numOfUsers')
        self.syscom.array('numOfUsers', 'SUeList', 'ueList')

    def PhyEventDetectedIndMsg(self, *header_fields):
        self.syscom.new_message('PhyEventDetectedIndMsg', 'Syscom', 'header:msgId:0x2639', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u8('numOfEvents')
        self.syscom.u8('paddingNumOfEvents')
        self.syscom.array('8', 'SMacToPhyEvent', 'event')
        self.syscom.u16('paddingEvent')

    def MacBearerModifyReqMsg(self, *header_fields):
        self.syscom.new_message('MacBearerModifyReqMsg', 'Syscom', 'header:msgId:0x2651', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ttiBmMeasActivate')
        self.syscom.u32('hasAmbrParams')
        self.SAmbrParams('ambrParams')
        self.syscom.u32('hasAmrWbNb')
        self.syscom.u32('amrWbNb')
        self.syscom.u32('numDrbs')
        self.syscom.array('numDrbs', 'SRbModifyInfo', 'drbInfoList')

    def MacBearerModifyRespMsg(self, *header_fields):
        self.syscom.new_message('MacBearerModifyRespMsg', 'Syscom', 'header:msgId:0x2652', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def LteStoreCountersIndMsg(self, *header_fields):
        self.syscom.new_message('LteStoreCountersIndMsg', 'Syscom', 'header:msgId:0x2666', *header_fields)
        self.syscom.u32('restart')
        self.syscom.u32('numOfMeasNames')
        self.syscom.array('numOfMeasNames', 'u32', 'measNames')

    def LteFetchCountersReqMsg(self, *header_fields):
        self.syscom.new_message('LteFetchCountersReqMsg', 'Syscom', 'header:msgId:0x2667', *header_fields)
        self.syscom.u32('numOfMeasNames')
        self.syscom.array('numOfMeasNames', 'u32', 'measNames')

    def LteFetchCountersRespMsg(self, *header_fields):
        self.syscom.new_message('LteFetchCountersRespMsg', 'Syscom', 'header:msgId:0x2668', *header_fields)
        self.syscom.u32('lastMessage')
        self.syscom.u32('numOfObjects')
        self.syscom.array('numOfObjects', 'SPmGeneralObject', 'objects')

    def MacCaUserReconfigurationReqMsg(self, *header_fields):
        self.syscom.new_message('MacCaUserReconfigurationReqMsg', 'Syscom', 'header:msgId:0x2678', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u8('paddingUeIndex')
        self.syscom.u8('eBSR')
        self.syscom.u32('relatedProcedure')
        self.syscom.u32('hasAperiodicCsiTriggerParams')
        self.SAperiodicCsiTriggerParams('aperiodicCsiTriggerParams')
        self.syscom.u32('hasContainer')
        self.UCaUserReconfigurationContainer('container')
        self.syscom.u32('numOfDrbToModify')
        self.syscom.array('8', 'SCaRbInfo', 'drbToModifyList')
        self.syscom.u32('numOfR10n1PucchAnCsList')
        self.syscom.array('2', 'SR10n1PucchAnCsElement', 'r10n1PucchAnCsList')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('hasMaxNumOfLayersPCell')
        self.syscom.u32('maxNumOfLayersPCell')
        self.syscom.u32('maxLayersDeliveredToUePCell')
        self.syscom.u32('layersRestrictedToTwoPCell')
        self.syscom.u32('transmModePCell')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('numOfSCellsRemove')
        self.syscom.array('4', 'SSCellsRemove', 'sCellsRemove')
        self.syscom.u32('numOfSCellsConfiguration')
        self.syscom.array('numOfSCellsConfiguration', 'SSCellsConfiguration', 'sCellsConfiguration')

    def MacCaUserReconfigurationRespMsg(self, *header_fields):
        self.syscom.new_message('MacCaUserReconfigurationRespMsg', 'Syscom', 'header:msgId:0x2679', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numOfSCellResultsForRemoval')
        self.syscom.array('4', 'SSCellResultsParameters', 'sCellResultsForRemoval')
        self.syscom.u32('numOfSCellResultsForConfiguration')
        self.syscom.array('4', 'SSCellResultsParameters', 'sCellResultsForConfiguration')
        self.SMessageResult('messageResult')

    def PsCellDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellDeleteReqMsg', 'Syscom', 'header:msgId:0x268E', *header_fields)
        self.syscom.u32('cellId')

    def PsCellDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellDeleteRespMsg', 'Syscom', 'header:msgId:0x268F', *header_fields)
        self.syscom.u32('cellId')
        self.SMessageResult('messageResult')

    def MacPowerHeadroomBundledIndMsg(self, *header_fields):
        self.syscom.new_message('MacPowerHeadroomBundledIndMsg', 'Syscom', 'header:msgId:0x2692', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('numOfUePhr')
        self.syscom.array('1', 'SUePhr', 'uePhrList')

    def PsBearerModifyReqMsg(self, *header_fields):
        self.syscom.new_message('PsBearerModifyReqMsg', 'Syscom', 'header:msgId:0x2695', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ttiBmMeasActivate')
        self.syscom.u32('hasAmbrParams')
        self.SAmbrParams('ambrParams')
        self.syscom.u32('hasAmrWbNb')
        self.syscom.u32('amrWbNb')
        self.syscom.u32('numDrbs')
        self.syscom.array('numDrbs', 'SRbModifyInfo', 'drbInfoList')

    def PsBearerModifyRespMsg(self, *header_fields):
        self.syscom.new_message('PsBearerModifyRespMsg', 'Syscom', 'header:msgId:0x2696', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def PsCellReconfigInternalReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigInternalReqMsg', 'Syscom', 'header:msgId:0x2697', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('operation')
        self.syscom.u32('numCellsFsp')
        self.syscom.array('6', 'SCellCarrierInfo', 'cellCarrierInfo')

    def PsCellReconfigInternalRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigInternalRespMsg', 'Syscom', 'header:msgId:0x2698', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('operation')

    def PsCellReconfigurationDeltaReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigurationDeltaReqMsg', 'Syscom', 'header:msgId:0x2699', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('hasDcmContainer')
        self.UWmpDcmCellReconfigurationContainer('dcmContainer')

    def PsCellReconfigurationDeltaRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigurationDeltaRespMsg', 'Syscom', 'header:msgId:0x269A', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def PsCellReconfigurationReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigurationReqMsg', 'Syscom', 'header:msgId:0x269B', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('activationTimeSFN')
        self.SCommonCellParams('commonCellParams')
        self.SPhichParams('phichParams')
        self.SPucchConfiguration('pucchParams')
        self.SSoundingRsUlConfigCommon('soundingRsUlConfigCommon')
        self.syscom.u32('hsTrainScenario')
        self.syscom.u32('harqMaxMsg3')
        self.UWmpDcmCellContainer('container')

    def PsCellReconfigurationRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellReconfigurationRespMsg', 'Syscom', 'header:msgId:0x269C', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def PsCellSetupReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellSetupReqMsg', 'Syscom', 'header:msgId:0x269D', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('phyCellId')
        self.SCommonCellParams('commonCellParams')
        self.SPhichParams('phichParams')
        self.SPucchConfiguration('pucchParams')
        self.SSoundingRsUlConfigCommon('soundingRsUlConfigCommon')
        self.syscom.u32('hsTrainScenario')
        self.syscom.u32('harqMaxMsg3')
        self.SBufferDiscardParams('bufferDiscardParams')
        self.syscom.u32('hasVoLteThresholdParams')
        self.SVoLteThresholdParams('voLteThresholdParams')
        self.syscom.u32('numOfRlcDlLcpInfo')
        self.syscom.array('16', 'SRlcLcpInfo', 'rlcDlLcpInfo')
        self.syscom.u32('resourcePoolGroupId')
        self.syscom.u32('cellMode')
        self.SCellSlotConf('cellSlotConf')
        self.syscom.u32('numOfScellCandidate')
        self.syscom.array('24', 'u32', 'lnCellIdSCellCandidate')
        self.UWmpDcmCellContainer('container')

    def PsCellSetupRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellSetupRespMsg', 'Syscom', 'header:msgId:0x269E', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('macSgnl')
        self.syscom.u32('macCellMeas')
        self.syscom.u32('macUserPs')
        self.syscom.u32('macCellPs')
        self.syscom.u32('dataCtrlPdcchClient')
        self.syscom.u32('psUserMgmt')
        self.syscom.u32('psUserUl')
        self.syscom.u32('psUserDl')
        self.syscom.u32('psUserDisableDlAndSCell')
        self.syscom.u32('dataCtrlMbmsClient')
        self.syscom.u32('numOfTestabilityServices')
        self.syscom.array('numOfTestabilityServices', 'SServiceInfo', 'serviceInfo')

    def PsCrntiReleaseReqMsg(self, *header_fields):
        self.syscom.new_message('PsCrntiReleaseReqMsg', 'Syscom', 'header:msgId:0x269F', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ueId')

    def PsDlPhyDataAddressSetReqMsg(self, *header_fields):
        self.syscom.new_message('PsDlPhyDataAddressSetReqMsg', 'Syscom', 'header:msgId:0x26A0', *header_fields)
        self.syscom.u32('cellId')
        self.SDlPhyDataAddressInfo('dlPhyDataAddressInfo')
        self.syscom.u32('raContResoT')

    def PsExternalAddressSetReqMsg(self, *header_fields):
        self.syscom.new_message('PsExternalAddressSetReqMsg', 'Syscom', 'header:msgId:0x26A1', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.STupUserAddress('tupUserAddress')

    def PsHoUeAddReqMsg(self, *header_fields):
        self.syscom.new_message('PsHoUeAddReqMsg', 'Syscom', 'header:msgId:0x26A2', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('poolIdData')
        self.syscom.u16('ueIndexData')
        self.syscom.u16('paddingUeIndexData')
        self.syscom.u32('numOfScellIds')
        self.syscom.array('2', 'u32', 'lnCelIdSCell')
        self.syscom.i32('maxNumberOfHarqTransmissionsMsg3')
        self.SUeSetupParams('ueSetupParams')
        self.UWmpDcmUserContainer('dcmContainer')
        self.SPuschControlOffsets('controlOffsets')
        self.SCqiParams('cqiParams')
        self.syscom.u32('handoverType')
        self.SUeParams('ueParams')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasUlPCUeParams')
        self.SUlPCUeParams('ulPCUeParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('macUserUeClientAddress')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'SRbInfo', 'rbInfoList')

    def PsHoUeAddRespMsg(self, *header_fields):
        self.syscom.new_message('PsHoUeAddRespMsg', 'Syscom', 'header:msgId:0x26A3', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')

    def PsMeasGapStartReqMsg(self, *header_fields):
        self.syscom.new_message('PsMeasGapStartReqMsg', 'Syscom', 'header:msgId:0x26A6', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.UMeasGapOffset('measGapOffset')

    def PsMeasGapStartRespMsg(self, *header_fields):
        self.syscom.new_message('PsMeasGapStartRespMsg', 'Syscom', 'header:msgId:0x26A7', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def PsMeasGapStopReqMsg(self, *header_fields):
        self.syscom.new_message('PsMeasGapStopReqMsg', 'Syscom', 'header:msgId:0x26A8', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def PsMeasGapStopRespMsg(self, *header_fields):
        self.syscom.new_message('PsMeasGapStopRespMsg', 'Syscom', 'header:msgId:0x26A9', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def PsRachParaReqMsg(self, *header_fields):
        self.syscom.new_message('PsRachParaReqMsg', 'Syscom', 'header:msgId:0x26AA', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('ueId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numOfScellIds')
        self.syscom.array('2', 'u32', 'lnCelIdSCell')
        self.syscom.u32('handoverType')
        self.syscom.u32('dedicRaPreExpT')
        self.syscom.u32('ueGroup')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('intentionalContentionbasedRaEnabled')

    def PsRachParaRespMsg(self, *header_fields):
        self.syscom.new_message('PsRachParaRespMsg', 'Syscom', 'header:msgId:0x26AB', *header_fields)
        self.syscom.u32('cellId')
        self.SMessageResult('messageResult')
        self.syscom.u32('ueId')
        self.syscom.u32('crnti')
        self.syscom.u32('raPreambleIndex')
        self.syscom.u32('prachMaskIndex')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def PsRachSetupReqMsg(self, *header_fields):
        self.syscom.new_message('PsRachSetupReqMsg', 'Syscom', 'header:msgId:0x26AC', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('lCelId')
        self.SRachParams('rachParams')

    def PsRachSetupRespMsg(self, *header_fields):
        self.syscom.new_message('PsRachSetupRespMsg', 'Syscom', 'header:msgId:0x26AD', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('puschReceiverAddress')
        self.syscom.u32('hasMacPsCaParamsContainer')
        self.UWmpDcmCaParamsContainer('macPsCaParamsContainer')

    def PsRbAddReqMsg(self, *header_fields):
        self.syscom.new_message('PsRbAddReqMsg', 'Syscom', 'header:msgId:0x26AE', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasCrnti')
        self.syscom.u32('crnti')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'SRbInfo', 'rbInfoList')

    def PsRbAddRespMsg(self, *header_fields):
        self.syscom.new_message('PsRbAddRespMsg', 'Syscom', 'header:msgId:0x26AF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')

    def PsRbDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('PsRbDeleteReqMsg', 'Syscom', 'header:msgId:0x26B0', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'u32', 'srbList')
        self.syscom.array('2', 'u32', 'sLogicalChannelList')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'u32', 'rbList')
        self.syscom.array('10', 'u32', 'logicalChannelId')
        self.syscom.u32('spsCrntiReleaseReq')

    def PsRbDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('PsRbDeleteRespMsg', 'Syscom', 'header:msgId:0x26B1', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')

    def PsStartSchedulingReqMsg(self, *header_fields):
        self.syscom.new_message('PsStartSchedulingReqMsg', 'Syscom', 'header:msgId:0x26B4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def PsStartSchedulingRespMsg(self, *header_fields):
        self.syscom.new_message('PsStartSchedulingRespMsg', 'Syscom', 'header:msgId:0x26B5', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def PsStopSchedulingCellReqMsg(self, *header_fields):
        self.syscom.new_message('PsStopSchedulingCellReqMsg', 'Syscom', 'header:msgId:0x26B8', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('shutDownFlag')

    def PsStopSchedulingCellRespMsg(self, *header_fields):
        self.syscom.new_message('PsStopSchedulingCellRespMsg', 'Syscom', 'header:msgId:0x26B9', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def PsStopSchedulingReqMsg(self, *header_fields):
        self.syscom.new_message('PsStopSchedulingReqMsg', 'Syscom', 'header:msgId:0x26BA', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('handoverType')

    def PsStopSchedulingRespMsg(self, *header_fields):
        self.syscom.new_message('PsStopSchedulingRespMsg', 'Syscom', 'header:msgId:0x26BB', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numBearers')
        self.syscom.array('numBearers', 'SBearerList', 'bearerList')

    def PsStopUeReqMsg(self, *header_fields):
        self.syscom.new_message('PsStopUeReqMsg', 'Syscom', 'header:msgId:0x26BC', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')

    def PsStopUeRespMsg(self, *header_fields):
        self.syscom.new_message('PsStopUeRespMsg', 'Syscom', 'header:msgId:0x26BD', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.SMessageResult('messageResult')

    def PsTxAntennaConfChangeReqMsg(self, *header_fields):
        self.syscom.new_message('PsTxAntennaConfChangeReqMsg', 'Syscom', 'header:msgId:0x26BE', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numAvailableTxAntennas')

    def PsTxAntennaConfChangeRespMsg(self, *header_fields):
        self.syscom.new_message('PsTxAntennaConfChangeRespMsg', 'Syscom', 'header:msgId:0x26BF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def PsUeInfoReqMsg(self, *header_fields):
        self.syscom.new_message('PsUeInfoReqMsg', 'Syscom', 'header:msgId:0x26C0', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ueInfo')

    def PsUeInfoRespMsg(self, *header_fields):
        self.syscom.new_message('PsUeInfoRespMsg', 'Syscom', 'header:msgId:0x26C1', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.UUeInfo('ueInfo')

    def PsUeReconfigReqMsg(self, *header_fields):
        self.syscom.new_message('PsUeReconfigReqMsg', 'Syscom', 'header:msgId:0x26C2', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('ueIndexTemp')
        self.syscom.u32('poolIdData')
        self.syscom.u16('ueIndexData')
        self.syscom.u16('paddingUeIndexData')
        self.syscom.u32('handoverType')
        self.SUeSetupParams('ueSetupParams')
        self.UWmpDcmUserContainer('container')
        self.SPuschControlOffsets('controlOffsets')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasUlPCUeParams')
        self.SUlPCUeParams('ulPCUeParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('macUserUeClientAddress')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'SRbInfo', 'rbInfoList')

    def PsUeReconfigRespMsg(self, *header_fields):
        self.syscom.new_message('PsUeReconfigRespMsg', 'Syscom', 'header:msgId:0x26C3', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')

    def PsUlResourceControlReqMsg(self, *header_fields):
        self.syscom.new_message('PsUlResourceControlReqMsg', 'Syscom', 'header:msgId:0x26C4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasContainer')
        self.UUlResCtrlParamContainer('container')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('numOfCqiParamsScell', 'SCqiParamsScell', 'cqiParamsScell')

    def PsUlResourceControlRespMsg(self, *header_fields):
        self.syscom.new_message('PsUlResourceControlRespMsg', 'Syscom', 'header:msgId:0x26C5', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSCellServCellIndex')
        self.syscom.u32('sCellServCellIndex')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')

    def PsUserModifyReqMsg(self, *header_fields):
        self.syscom.new_message('PsUserModifyReqMsg', 'Syscom', 'header:msgId:0x26C6', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('measGapStopRequired')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('hasUlSpsConfigDedicated')
        self.SUlSpsConfigDedicated('ulSpsConfigDedicated')
        self.syscom.u32('hasAmbrParams')
        self.SAmbrParams('ambrParams')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('hasActNewTransmMode')
        self.syscom.u32('actNewTransmMode')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeInactivityTimer')
        self.syscom.u32('ueInactivityTimer')
        self.syscom.u32('hasTargetBLER')
        self.STargetBLER('targetBLER')
        self.syscom.u32('hasThroughputThresholdMonitoring')
        self.SThroughputThresholdMonitoring('throughputThresholdMonitoring')
        self.syscom.u32('hasConfigId')
        self.syscom.u32('configId')
        self.syscom.u32('hasHarqMaxTrDl')
        self.syscom.u32('harqMaxTrDl')
        self.syscom.u32('hasHarqMaxTrUl')
        self.syscom.u32('harqMaxTrUl')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasEnableNonGbrBufferMonitoring')
        self.syscom.u32('enableNonGbrBufferMonitoring')

    def PsUserModifyRespMsg(self, *header_fields):
        self.syscom.new_message('PsUserModifyRespMsg', 'Syscom', 'header:msgId:0x26C7', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')

    def PsDefaultUserConfigReqMsg(self, *header_fields):
        self.syscom.new_message('PsDefaultUserConfigReqMsg', 'Syscom', 'header:msgId:0x26C8', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('l3Address')
        self.SUserInfoMac('userInfo')

    def PsDefaultUserConfigRespMsg(self, *header_fields):
        self.syscom.new_message('PsDefaultUserConfigRespMsg', 'Syscom', 'header:msgId:0x26C9', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('numOfNodeAddress')
        self.syscom.array('2', 'u16', 'nodeAddress')

    def PsUeDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('PsUeDeleteReqMsg', 'Syscom', 'header:msgId:0x26CA', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')
        self.syscom.u32('validUeId')
        self.syscom.u16('ueIndexPcell')
        self.syscom.u16('paddingUeIndexPcell')

    def PsUeDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('PsUeDeleteRespMsg', 'Syscom', 'header:msgId:0x26CB', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')

    def PsRbModifyReqMsg(self, *header_fields):
        self.syscom.new_message('PsRbModifyReqMsg', 'Syscom', 'header:msgId:0x26CC', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('2', 'SCqiParamsScell', 'cqiParamsScell')
        self.syscom.u32('hasAmrWbNb')
        self.syscom.u32('amrWbNb')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')

    def PsRbModifyRespMsg(self, *header_fields):
        self.syscom.new_message('PsRbModifyRespMsg', 'Syscom', 'header:msgId:0x26CD', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')

    def PsRachUserSetupReqMsg(self, *header_fields):
        self.syscom.new_message('PsRachUserSetupReqMsg', 'Syscom', 'header:msgId:0x26D0', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('subFrameNumber')
        self.SRaPreambleList('RAPreambleList')

    def PsRachUserSetupRespMsg(self, *header_fields):
        self.syscom.new_message('PsRachUserSetupRespMsg', 'Syscom', 'header:msgId:0x26D1', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('subFrameNumber')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.SRaPreambleResList('RAPreambleList')

    def MacBundledContentionResIndMsg(self, *header_fields):
        self.syscom.new_message('MacBundledContentionResIndMsg', 'Syscom', 'header:msgId:0x26D3', *header_fields)
        self.syscom.u32('numberOfContResMsg')
        self.syscom.u32('paddingNumberOfContResMsg')
        self.syscom.array('16', 'SContentionResInd', 'pduMuxContentionResInd')

    def MacConfigChangeIndMsg(self, *header_fields):
        self.syscom.new_message('MacConfigChangeIndMsg', 'Syscom', 'header:msgId:0x26D4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u8('hasDrxConfigId')
        self.syscom.u8('paddingHasDrxConfigId')
        self.syscom.u32('drxConfigId')

    def MacCcchDataIndMsg(self, *header_fields):
        self.syscom.new_message('MacCcchDataIndMsg', 'Syscom', 'header:msgId:0x26D5', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('size')
        self.syscom.u32('tempUeNeeded')
        self.syscom.u32('macCeFlag')
        self.syscom.u32('hasCriPayload')
        self.syscom.array('6', 'u8', 'criPayload')
        self.syscom.u16('paddingCriPayload')

    def MacDlBufferStatusBundleIndMsg(self, *header_fields):
        self.syscom.new_message('MacDlBufferStatusBundleIndMsg', 'Syscom', 'header:msgId:0x26D7', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('numOfLchHaveData')
        self.syscom.u32('numOfMessages')
        self.syscom.array('numOfMessages', 'SDlBufferStatusInd', 'dlBsr')

    def MacHarqReleaseReqMsg(self, *header_fields):
        self.syscom.new_message('MacHarqReleaseReqMsg', 'Syscom', 'header:msgId:0x26D8', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('enbId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('numOfHarqReleaseInfo')
        self.syscom.array('numOfHarqReleaseInfo', 'SHarqReleaseInfo', 'harqReleaseInfo')

    def MacMacCrntiCeIndMsg(self, *header_fields):
        self.syscom.new_message('MacMacCrntiCeIndMsg', 'Syscom', 'header:msgId:0x26D9', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('tempCrnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('tempUeIndex')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')

    def MacMeasInitReqMsg(self, *header_fields):
        self.syscom.new_message('MacMeasInitReqMsg', 'Syscom', 'header:msgId:0x26DA', *header_fields)
        self.syscom.u32('reportClientSicad')
        self.syscom.u32('cellId')
        self.syscom.u32('startSfn')
        self.syscom.u32('reportId')
        self.syscom.u32('period')
        self.syscom.u32('samplingPeriod')
        self.syscom.u32('groupCount')
        self.syscom.array('groupCount', 'u32', 'groupList')

    def MacMeasInitRespMsg(self, *header_fields):
        self.syscom.new_message('MacMeasInitRespMsg', 'Syscom', 'header:msgId:0x26DB', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('reportId')
        self.SMessageResult('messageResult')

    def MacMeasTermReqMsg(self, *header_fields):
        self.syscom.new_message('MacMeasTermReqMsg', 'Syscom', 'header:msgId:0x26DE', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('reportId')

    def MacMeasTermRespMsg(self, *header_fields):
        self.syscom.new_message('MacMeasTermRespMsg', 'Syscom', 'header:msgId:0x26DF', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('reportId')
        self.SMessageResult('messageResult')

    def MacPdumuxBundledDataReqMsg(self, *header_fields):
        self.syscom.new_message('MacPdumuxBundledDataReqMsg', 'Syscom', 'header:msgId:0x26E1', *header_fields)
        self.syscom.u16('cellId')
        self.syscom.u16('paddingCellId')
        self.syscom.u32('enbId')
        self.syscom.u16('frameNumber')
        self.syscom.u8('subFrameNumber')
        self.syscom.u8('cfi')
        self.syscom.u8('lastTbInTti')
        self.syscom.u8('latencyBudgetExceeded')
        self.syscom.u8('numOfBundledPduMuxMsgs')
        self.syscom.u8('paddingNumOfBundledPduMuxMsgs')
        self.syscom.array('numOfBundledPduMuxMsgs', 'SPduMuxDataReq', 'data')

    def MacPdumuxDataRespMsg(self, *header_fields):
        self.syscom.new_message('MacPdumuxDataRespMsg', 'Syscom', 'header:msgId:0x26E2', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('frameNumber')
        self.syscom.u16('subFrameNumber')
        self.syscom.u32('resLength')
        self.syscom.array('resLength', 'SPduMuxDataResultEntry', 'resArray')

    def MacTcrntiDeleteIndMsg(self, *header_fields):
        self.syscom.new_message('MacTcrntiDeleteIndMsg', 'Syscom', 'header:msgId:0x26E3', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('sendDeleteReqToMacData')

    def PsCaUserReconfigurationReqMsg(self, *header_fields):
        self.syscom.new_message('PsCaUserReconfigurationReqMsg', 'Syscom', 'header:msgId:0x26EB', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('relatedProcedure')
        self.syscom.u32('hasAperiodicCsiTriggerParams')
        self.SAperiodicCsiTriggerParams('aperiodicCsiTriggerParams')
        self.syscom.u32('hasContainer')
        self.UCaUserReconfigurationContainer('container')
        self.syscom.u32('numOfR10n1PucchAnCsList')
        self.syscom.array('2', 'SR10n1PucchAnCsElement', 'r10n1PucchAnCsList')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('hasMaxNumOfLayersPCell')
        self.syscom.u32('maxNumOfLayersPCell')
        self.syscom.u32('maxLayersDeliveredToUePCell')
        self.syscom.u32('layersRestrictedToTwoPCell')
        self.syscom.u32('transmModePCell')
        self.syscom.u32('numOfSCellsRemove')
        self.syscom.array('4', 'SSCellsRemove', 'sCellsRemove')
        self.syscom.u32('numOfServingCellConfiguration')
        self.syscom.array('numOfServingCellConfiguration', 'SServingCellConfiguration', 'servingCellConfiguration')

    def PsCaUserReconfigurationRespMsg(self, *header_fields):
        self.syscom.new_message('PsCaUserReconfigurationRespMsg', 'Syscom', 'header:msgId:0x26EC', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numOfSCellResultsForRemoval')
        self.syscom.array('4', 'SSCellResultsParameters', 'sCellResultsForRemoval')
        self.syscom.u32('numOfSCellResultsForConfiguration')
        self.syscom.array('4', 'SSCellResultsParameters', 'sCellResultsForConfiguration')
        self.SMessageResult('messageResult')

    def MacRadioBearerModifyReqMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerModifyReqMsg', 'Syscom', 'header:msgId:0x2758', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('2', 'SCqiParamsScell', 'cqiParamsScell')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')

    def MacRadioBearerModifyRespMsg(self, *header_fields):
        self.syscom.new_message('MacRadioBearerModifyRespMsg', 'Syscom', 'header:msgId:0x2759', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSpsCrnti')
        self.syscom.u32('spsCrnti')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def MacRadioLinkStatusIndMsg(self, *header_fields):
        self.syscom.new_message('MacRadioLinkStatusIndMsg', 'Syscom', 'header:msgId:0x275A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('paddingServingCellIndex')
        self.syscom.u32('hasSrbId')
        self.syscom.u32('srbId')
        self.syscom.u32('hasDrbId')
        self.syscom.u32('drbId')
        self.syscom.u32('hasTimingAdvanceType2')
        self.syscom.u32('timingAdvanceType2')
        self.syscom.u32('rlsCause')

    def MacStartUlTestModelReqMsg(self, *header_fields):
        self.syscom.new_message('MacStartUlTestModelReqMsg', 'Syscom', 'header:msgId:0x275B', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('referenceChannelNumber')
        self.syscom.u32('resourceBlockOffset')
        self.syscom.u32('reportingTimeInterval')
        self.syscom.u32('harqUsed')
        self.syscom.u32('digitalOutputEnabled')
        self.SUlTestModelsDigitalOutputParams('ulTestModelDigitalOutputParams')
        self.syscom.u32('hasAdditionalMeasurementParameters')
        self.UAdditionalMeasurementParameters('additionalMeasurementParameters')

    def MacStartUlTestModelRespMsg(self, *header_fields):
        self.syscom.new_message('MacStartUlTestModelRespMsg', 'Syscom', 'header:msgId:0x275C', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacStopUlTestModelReqMsg(self, *header_fields):
        self.syscom.new_message('MacStopUlTestModelReqMsg', 'Syscom', 'header:msgId:0x275D', *header_fields)
        self.syscom.u32('lnCelId')

    def MacStopUlTestModelRespMsg(self, *header_fields):
        self.syscom.new_message('MacStopUlTestModelRespMsg', 'Syscom', 'header:msgId:0x275E', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacThroughputMeasurementReportIndMsg(self, *header_fields):
        self.syscom.new_message('MacThroughputMeasurementReportIndMsg', 'Syscom', 'header:msgId:0x275F', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('resultStatus')
        self.syscom.u32('throughputResult')
        self.syscom.u32('paddingThroughputResult')
        self.SResultCounters('resultCounters')
        self.syscom.u32('hasThroughputResultStationaryUe')
        self.syscom.u32('throughputResultStationaryUe')
        self.syscom.u32('hasResultCountersStationaryUe')
        self.syscom.u32('paddingHasResultCountersStationaryUe')
        self.SResultCounters('resultCountersStationaryUe')

    def MacUlResourceControlReqMsg(self, *header_fields):
        self.syscom.new_message('MacUlResourceControlReqMsg', 'Syscom', 'header:msgId:0x2760', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasContainer')
        self.UUlResCtrlParamContainer('container')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('numOfCqiParamsScell', 'SCqiParamsScell', 'cqiParamsScell')

    def MacUlResourceControlRespMsg(self, *header_fields):
        self.syscom.new_message('MacUlResourceControlRespMsg', 'Syscom', 'header:msgId:0x2761', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSCellServCellIndex')
        self.syscom.u32('sCellServCellIndex')
        self.syscom.u32('hasContainer')
        self.UUlTfrParamContainer('container')

    def TupMaxCountIndMsg(self, *header_fields):
        self.syscom.new_message('TupMaxCountIndMsg', 'Syscom', 'header:msgId:0x276B', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbId')
        self.syscom.u32('countStatus')

    def TupProceedLockStepReqMsg(self, *header_fields):
        self.syscom.new_message('TupProceedLockStepReqMsg', 'Syscom', 'header:msgId:0x276C', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupProceedLockStepRespMsg(self, *header_fields):
        self.syscom.new_message('TupProceedLockStepRespMsg', 'Syscom', 'header:msgId:0x276D', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupSecurityActivationReqMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityActivationReqMsg', 'Syscom', 'header:msgId:0x276E', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupSecurityActivationRespMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityActivationRespMsg', 'Syscom', 'header:msgId:0x276F', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def MacErrorIndMsg(self, *header_fields):
        self.syscom.new_message('MacErrorIndMsg', 'Syscom', 'header:msgId:0x2778', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSRbList', 'sRbList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SDRbList', 'dRbList')

    def LteBrowserConnectionReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserConnectionReqMsg', 'Syscom', 'header:msgId:0x2779', *header_fields)
        self.syscom.u32('clientName')
        self.syscom.u32('measurementReportingMode')
        self.syscom.u32('changeNotifFlag')

    def LteBrowserConnectionRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserConnectionRespMsg', 'Syscom', 'header:msgId:0x277A', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('sessionId')

    def LteBrowserDisconnectionReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserDisconnectionReqMsg', 'Syscom', 'header:msgId:0x277B', *header_fields)
        self.syscom.u32('sessionId')

    def LteBrowserDisconnectionRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserDisconnectionRespMsg', 'Syscom', 'header:msgId:0x277C', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('sessionId')

    def LteBrowserObjectsReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserObjectsReqMsg', 'Syscom', 'header:msgId:0x277D', *header_fields)
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('parentObjectHandle')

    def LteBrowserObjectsRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserObjectsRespMsg', 'Syscom', 'header:msgId:0x277E', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('numOfAssociatedObjects')
        self.syscom.u32('itemSize')
        self.syscom.array('numOfAssociatedObjects', 'u32', 'dynamicData')

    def LteBrowserStartReportReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserStartReportReqMsg', 'Syscom', 'header:msgId:0x2780', *header_fields)
        self.SBrowserRequestor('requestor')
        self.syscom.u32('reportName')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('itemCollectCount')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('reportingDuration')
        self.syscom.u32('objectHandler')
        self.syscom.u32('paramsTableSize')
        self.syscom.array('1', 'u32', 'dynamicData')

    def LteBrowserStartReportRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserStartReportRespMsg', 'Syscom', 'header:msgId:0x2781', *header_fields)
        self.syscom.u32('reportName')
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')

    def LteBrowserReportIndMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserReportIndMsg', 'Syscom', 'header:msgId:0x2782', *header_fields)
        self.SAaTime('timeStamp')
        self.syscom.u32('sequenceNumber')
        self.syscom.u32('reportName')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('itemCount')
        self.syscom.u32('totalSize')
        self.syscom.array('1', 'u32', 'dynamicData')

    def LteBrowserStopReportReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserStopReportReqMsg', 'Syscom', 'header:msgId:0x2783', *header_fields)
        self.syscom.u32('reportName')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('objectHandler')

    def LteBrowserStopReportRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserStopReportRespMsg', 'Syscom', 'header:msgId:0x2784', *header_fields)
        self.syscom.u32('reportName')
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')

    def LteBrowserListReqMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserListReqMsg', 'Syscom', 'header:msgId:0x2785', *header_fields)
        self.syscom.u32('listName')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('objectHandler')

    def LteBrowserListRespMsg(self, *header_fields):
        self.syscom.new_message('LteBrowserListRespMsg', 'Syscom', 'header:msgId:0x2786', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('numberOfItems')
        self.syscom.u32('itemSize')
        self.syscom.array('1', 'u32', 'dynamicData')

    def MacStartUlCtrlChannelMeasReqMsg(self, *header_fields):
        self.syscom.new_message('MacStartUlCtrlChannelMeasReqMsg', 'Syscom', 'header:msgId:0x27BE', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measType')
        self.syscom.u32('reportingTimeInterval')
        self.syscom.u32('receptionSubframe')
        self.syscom.u32('expectionSubframe')
        self.UUlCtrlChannelParams('ulCtrlChannelParams')

    def MacStartUlCtrlChannelMeasRespMsg(self, *header_fields):
        self.syscom.new_message('MacStartUlCtrlChannelMeasRespMsg', 'Syscom', 'header:msgId:0x27BF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacStopUlCtrlChannelMeasReqMsg(self, *header_fields):
        self.syscom.new_message('MacStopUlCtrlChannelMeasReqMsg', 'Syscom', 'header:msgId:0x27C0', *header_fields)
        self.syscom.u32('lnCelId')

    def MacStopUlCtrlChannelMeasRespMsg(self, *header_fields):
        self.syscom.new_message('MacStopUlCtrlChannelMeasRespMsg', 'Syscom', 'header:msgId:0x27C1', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def MacUlCtrlChannelMeasReportIndMsg(self, *header_fields):
        self.syscom.new_message('MacUlCtrlChannelMeasReportIndMsg', 'Syscom', 'header:msgId:0x27C2', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('resultStatus')
        self.SUlCtrlChannelMeasCounters('UlCtrlChannelMeasCounters')
        self.syscom.u32('hasContainer')
        self.UlCtrlChannelMeasReportContainer('container')

    def TupMeasurementInitiationReqMsg(self, *header_fields):
        self.syscom.new_message('TupMeasurementInitiationReqMsg', 'Syscom', 'header:msgId:0x27D2', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('samplingPeriod')
        self.syscom.u32('numOfMeasurementGroupTypeList')
        self.syscom.array('numOfMeasurementGroupTypeList', 'u32', 'measurementGroupTypeList')

    def TupMeasurementInitiationRespMsg(self, *header_fields):
        self.syscom.new_message('TupMeasurementInitiationRespMsg', 'Syscom', 'header:msgId:0x27D3', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def TupMeasurementReportIndMsg(self, *header_fields):
        self.syscom.new_message('TupMeasurementReportIndMsg', 'Syscom', 'header:msgId:0x27D4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')
        self.syscom.u32('numOfMeasGroupReportList')
        self.syscom.array('2', 'u32', 'measGroupReportList')
        self.syscom.u32('poolIdSource')
        self.syscom.u32('startSfn')
        self.syscom.u32('numOfMeasReportValue')
        self.syscom.array('numOfMeasReportValue', 'SMeasReportValue', 'measReportValue')

    def TupMeasurementTerminationReqMsg(self, *header_fields):
        self.syscom.new_message('TupMeasurementTerminationReqMsg', 'Syscom', 'header:msgId:0x27D5', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def TupMeasurementTerminationRespMsg(self, *header_fields):
        self.syscom.new_message('TupMeasurementTerminationRespMsg', 'Syscom', 'header:msgId:0x27D6', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def TupPathSwitchReqMsg(self, *header_fields):
        self.syscom.new_message('TupPathSwitchReqMsg', 'Syscom', 'header:msgId:0x27D7', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoPathSwitch', 'rbList')

    def TupPathSwitchRespMsg(self, *header_fields):
        self.syscom.new_message('TupPathSwitchRespMsg', 'Syscom', 'header:msgId:0x27D8', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def TupSecurityConfReqMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityConfReqMsg', 'Syscom', 'header:msgId:0x27D9', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSecurityInformation')
        self.STupSecurityInformation('securityInformation')

    def TupSecurityConfRespMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityConfRespMsg', 'Syscom', 'header:msgId:0x27DA', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def MacMeasGapStartReqMsg(self, *header_fields):
        self.syscom.new_message('MacMeasGapStartReqMsg', 'Syscom', 'header:msgId:0x27E7', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.UMeasGapOffset('measGapOffset')

    def MacMeasGapStartRespMsg(self, *header_fields):
        self.syscom.new_message('MacMeasGapStartRespMsg', 'Syscom', 'header:msgId:0x27E8', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def MacMeasGapStopReqMsg(self, *header_fields):
        self.syscom.new_message('MacMeasGapStopReqMsg', 'Syscom', 'header:msgId:0x27E9', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def MacMeasGapStopRespMsg(self, *header_fields):
        self.syscom.new_message('MacMeasGapStopRespMsg', 'Syscom', 'header:msgId:0x27EA', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupResumeReqMsg(self, *header_fields):
        self.syscom.new_message('TupResumeReqMsg', 'Syscom', 'header:msgId:0x27EB', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupResumeRespMsg(self, *header_fields):
        self.syscom.new_message('TupResumeRespMsg', 'Syscom', 'header:msgId:0x27EC', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupBearerModifyReqMsg(self, *header_fields):
        self.syscom.new_message('TupBearerModifyReqMsg', 'Syscom', 'header:msgId:0x27F9', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoBearerModify', 'rbList')

    def TupBearerModifyRespMsg(self, *header_fields):
        self.syscom.new_message('TupBearerModifyRespMsg', 'Syscom', 'header:msgId:0x27FA', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoResp', 'rbList')

    def TupSecurityDeactivationReqMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityDeactivationReqMsg', 'Syscom', 'header:msgId:0x27FB', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def TupSecurityDeactivationRespMsg(self, *header_fields):
        self.syscom.new_message('TupSecurityDeactivationRespMsg', 'Syscom', 'header:msgId:0x27FC', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')

    def AatraceMonIndMsg(self, *header_fields):
        self.syscom.new_message('AatraceMonIndMsg', 'Syscom', 'header:msgId:0x2991', *header_fields)
        self.syscom.u32('type')
        self.syscom.u32('mode')
        self.syscom.u32('sequence')
        self.syscom.array('4', 'u32', 'extra')
        self.syscom.u32('dataLen')
        self.syscom.array('dataLen', 'u32', 'data')

    def ApiOmDspSwDlMsg(self, *header_fields):
        self.syscom.new_message('ApiOmDspSwDlMsg', 'Syscom', 'header:msgId:0x29C1', *header_fields)
        self.syscom.u32('target_board')
        self.syscom.u32('target_cpu')
        self.syscom.array('48', 'u8', 'file_1')
        self.syscom.array('48', 'u8', 'file_2')
        self.syscom.array('48', 'u8', 'file_3')
        self.syscom.array('48', 'u8', 'file_4')
        self.syscom.array('48', 'u8', 'file_5')
        self.syscom.array('48', 'u8', 'file_6')
        self.syscom.array('48', 'u8', 'file_7')
        self.syscom.array('48', 'u8', 'file_8')

    def ApiOmSwDlRespMsg(self, *header_fields):
        self.syscom.new_message('ApiOmSwDlRespMsg', 'Syscom', 'header:msgId:0x29C4', *header_fields)
        self.syscom.u32('success_code')
        self.syscom.u32('target_board')
        self.syscom.u32('target_cpu')

    def ApiOmI2CDeviceCfgCtrlMsg(self, *header_fields):
        self.syscom.new_message('ApiOmI2CDeviceCfgCtrlMsg', 'Syscom', 'header:msgId:0x2B27', *header_fields)
        self.syscom.u32('targetBoard')
        self.syscom.u32('targetUnit')
        self.syscom.u32('targetSubunit')
        self.syscom.u32('cfgCtrlType')
        self.syscom.u32('cfgCtrlDataLen')
        self.syscom.array('1', 'u32', 'cfgCtrlData')

    def ApiOmI2CDeviceCfgCtrlRespMsg(self, *header_fields):
        self.syscom.new_message('ApiOmI2CDeviceCfgCtrlRespMsg', 'Syscom', 'header:msgId:0x2B28', *header_fields)
        self.syscom.u32('targetBoard')
        self.syscom.u32('targetUnit')
        self.syscom.u32('targetSubunit')
        self.syscom.u32('successCode')
        self.syscom.u32('cfgCtrlType')
        self.syscom.u32('cfgCtrlDataLen')
        self.syscom.array('1', 'u32', 'cfgCtrlData')

    def ApiResetMsg(self, *header_fields):
        self.syscom.new_message('ApiResetMsg', 'Syscom', 'header:msgId:0x2B81', *header_fields)
        self.syscom.u32('target_board')
        self.syscom.u32('target_cpu')
        self.syscom.u32('reset_state')
        self.syscom.u32('reset_extra')

    def ApiResetRespMsg(self, *header_fields):
        self.syscom.new_message('ApiResetRespMsg', 'Syscom', 'header:msgId:0x2B82', *header_fields)
        self.syscom.u32('success_code')
        self.syscom.u32('target_board')
        self.syscom.u32('target_cpu')
        self.syscom.u32('reset_state')
        self.syscom.u32('reset_extra')

    def AasyscomGwRegReqMsg(self, *header_fields):
        self.syscom.new_message('AasyscomGwRegReqMsg', 'Syscom', 'header:msgId:0x2BD3', *header_fields)
        self.syscom.u32('localSicAddr')
        self.syscom.u32('remoteSicAddr')
        self.SAaSysComGwIpAddress('localIP')
        self.SAaSysComGwIpAddress('remoteIP')
        self.syscom.u32('protocol')
        self.syscom.u32('retainMsgHeader')
        self.syscom.u32('msgID')
        self.syscom.u32('reliability')

    def AasyscomGwRegReplyMsg(self, *header_fields):
        self.syscom.new_message('AasyscomGwRegReplyMsg', 'Syscom', 'header:msgId:0x2BD4', *header_fields)
        self.syscom.u32('localSicAddr')
        self.syscom.u32('remoteSicAddr')
        self.SAaSysComGwIpAddress('localIP')
        self.SAaSysComGwIpAddress('remoteIP')
        self.syscom.u32('protocol')
        self.syscom.u32('retainMsgHeader')
        self.syscom.u32('msgID')
        self.syscom.u32('reliability')
        self.syscom.u32('status')
        self.syscom.u32('routeId')
        self.syscom.u32('port')

    def AasyscomGwRegDefRouteReqMsg(self, *header_fields):
        self.syscom.new_message('AasyscomGwRegDefRouteReqMsg', 'Syscom', 'header:msgId:0x2BD9', *header_fields)
        self.SAaSysComGwIpAddress('address')
        self.syscom.u32('receiver')
        self.syscom.u32('protocol')
        self.syscom.u32('msgID')

    def AasyscomGwRegDefRouteReplyMsg(self, *header_fields):
        self.syscom.new_message('AasyscomGwRegDefRouteReplyMsg', 'Syscom', 'header:msgId:0x2BDA', *header_fields)
        self.SAaSysComGwIpAddress('address')
        self.syscom.u32('receiver')
        self.syscom.u32('protocol')
        self.syscom.u32('msgID')
        self.syscom.u32('status')
        self.syscom.u32('port')

    def TrswDataPathSupervisionConfReqMsg(self, *header_fields):
        self.syscom.new_message('TrswDataPathSupervisionConfReqMsg', 'Syscom', 'header:msgId:0x3422', *header_fields)
        self.syscom.u32('masterTupuSicad')
        self.UIpAddr('eNBUpApplicationIpAddress')
        self.syscom.u32('numOfSgwIpAddressList')
        self.syscom.array('numOfSgwIpAddressList', 'UIpAddr', 'sgwIpAddressList')

    def TrswDataPathSupervisionConfRespMsg(self, *header_fields):
        self.syscom.new_message('TrswDataPathSupervisionConfRespMsg', 'Syscom', 'header:msgId:0x3423', *header_fields)
        self.syscom.u32('status')
        self.UIpAddr('eNBUpApplicationIpAddress')
        self.syscom.u32('numOfSgwMappingList')
        self.syscom.array('numOfSgwMappingList', 'SIpSicAddr', 'sgwMappingList')

    def LomFmFaultHistoryReq(self, *header_fields):
        self.syscom.new_message('LomFmFaultHistoryReq', 'Syscom', 'header:msgId:0x35F2', *header_fields)
        self.syscom.u32('resetHistory')

    def LomFmFaultHistoryResp(self, *header_fields):
        self.syscom.new_message('LomFmFaultHistoryResp', 'Syscom', 'header:msgId:0x35F3', *header_fields)
        self.syscom.u32('faultsDelivered')
        self.syscom.u32('totalFaultsInHistory')
        self.syscom.array('10', 'LomFm_MinimalFaultInd', 'faults')

    def LomMtuTcpMssClampingInd(self, *header_fields):
        self.syscom.new_message('LomMtuTcpMssClampingInd', 'Syscom', 'header:msgId:0x35FD', *header_fields)
        self.syscom.u32('internalMtu')
        self.syscom.u32('actUserLayerTCPMSSClamping')

    def MacUlVolteReceptionIndMsg(self, *header_fields):
        self.syscom.new_message('MacUlVolteReceptionIndMsg', 'Syscom', 'header:msgId:0x4004', *header_fields)
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('numUes')
        self.syscom.array('numUes', 'SUeInfo', 'ueInfoList')

    def PsUeIndexMgmtReqMsg(self, *header_fields):
        self.syscom.new_message('PsUeIndexMgmtReqMsg', 'Syscom', 'header:msgId:0x400B', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCell')
        self.syscom.u32('relatedPcellEnbId')
        self.syscom.u32('enbIdServCell')
        self.syscom.u32('ueId')
        self.syscom.u32('crnti')
        self.syscom.u32('operationType')
        self.syscom.u16('ueIndex')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u16('ueIndexData')
        self.syscom.u16('paddingUeIndexData')

    def PsUeIndexMgmtRespMsg(self, *header_fields):
        self.syscom.new_message('PsUeIndexMgmtRespMsg', 'Syscom', 'header:msgId:0x400C', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCell')
        self.syscom.u32('relatedPcellEnbId')
        self.syscom.u32('enbIdServCell')
        self.syscom.u32('ueId')
        self.syscom.u32('crnti')
        self.syscom.u32('operationType')
        self.syscom.u16('ueIndex')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u32('ueGroup')

    def PsStopUesInCellReqMsg(self, *header_fields):
        self.syscom.new_message('PsStopUesInCellReqMsg', 'Syscom', 'header:msgId:0x4024', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCellId')
        self.syscom.u32('numOfUeToStop')
        self.syscom.array('numOfUeToStop', 'u16', 'ueToStop')

    def PsStopUesInCellRespMsg(self, *header_fields):
        self.syscom.new_message('PsStopUesInCellRespMsg', 'Syscom', 'header:msgId:0x4025', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCellId')
        self.SMessageResult('messageResult')

    def PsDeleteUesInCellReqMsg(self, *header_fields):
        self.syscom.new_message('PsDeleteUesInCellReqMsg', 'Syscom', 'header:msgId:0x4026', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCellId')
        self.syscom.u32('numOfUeToDelete')
        self.syscom.array('numOfUeToDelete', 'u16', 'ueToDelete')

    def PsDeleteUesInCellRespMsg(self, *header_fields):
        self.syscom.new_message('PsDeleteUesInCellRespMsg', 'Syscom', 'header:msgId:0x4027', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('relatedPCellId')
        self.SMessageResult('messageResult')

    def MacUlDataReceivedReqMsg(self, *header_fields):
        self.syscom.new_message('MacUlDataReceivedReqMsg', 'Syscom', 'header:msgId:0x4029', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numOfData')
        self.syscom.array('numOfData', 'SDataReceived', 'data')

    def MacUlDataReceivedRespMsg(self, *header_fields):
        self.syscom.new_message('MacUlDataReceivedRespMsg', 'Syscom', 'header:msgId:0x402A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numOfData')
        self.syscom.array('numOfData', 'SDataReceived', 'data')

    def PsInitSetupCollectorIndMsg(self, *header_fields):
        self.syscom.new_message('PsInitSetupCollectorIndMsg', 'Syscom', 'header:msgId:0x4037', *header_fields)
        self.SMemBuffer('cellSetupBuffer')
        self.SMemBuffer('ueSetupBuffer')
        self.SMemBuffer('rbSetupBuffer')

    def L2IntCellAnnounceInd(self, *header_fields):
        self.syscom.new_message('L2IntCellAnnounceInd', 'Syscom', 'header:msgId:0x4045', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('cellIndex')
        self.syscom.u32('hasRachParams')
        self.syscom.u32('raContResoT')
        self.syscom.u32('hasRntiTimer')
        self.syscom.u32('rntiTimer')
        self.syscom.u32('raCrntiReuseT')
        self.syscom.u32('rlpDetMaxTDl')
        self.syscom.u32('rlpDetMaxNoDl')
        self.syscom.u32('rlpDetEndNoDl')
        self.syscom.u32('hasRaMsg3Thr')
        self.syscom.u32('raMsg3Thr')
        self.syscom.u32('numOfRlcDlLcpInfo')
        self.syscom.array('16', 'SRlcLcpInfo', 'rlcLcpInfo')
        self.SFrameConfTdd('frameConfTdd')
        self.syscom.u32('hasBufferDiscardParams')
        self.SBufferDiscardParams('bufferDiscardParams')
        self.syscom.u32('hasPlmnId')
        self.syscom.u32('numOfPlmnIdList')
        self.SPlmnId('primaryPLMNId')
        self.syscom.array('5', 'SPlmnId', 'plmnIdList')
        self.syscom.u32('raNondedPreamb')
        self.syscom.u32('dlChBw')
        self.syscom.u32('timerRaComp')
        self.syscom.u32('hasVoLteThresholdParams')
        self.SVoLteThresholdParams('voLteThresholdParams')
        self.syscom.u32('actDLCAggr')
        self.syscom.u32('hasDlCarrierAggrParams')
        self.SCarrierAggrParams('carrierAggrParams')
        self.SMsg3DiscardData('msg3DiscardData')
        self.syscom.u32('hasFrameConfTdd')
        self.syscom.u32('sdlEnable')
        self.syscom.u32('actL1PM')
        self.syscom.u32('cellType')
        self.syscom.u32('sCellType')
        self.syscom.u32('numOfScellCandidate')

    def MgmtUserSetupResp(self, *header_fields):
        self.syscom.new_message('MgmtUserSetupResp', 'Syscom', 'header:msgId:0x4047', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndexCtrlContinuous')
        self.syscom.u16('ueIndexData')
        self.syscom.u32('numUserData')
        self.syscom.u32('rlcSupportUlQueId')

    def MgmtUserAmountReqMsg(self, *header_fields):
        self.syscom.new_message('MgmtUserAmountReqMsg', 'Syscom', 'header:msgId:0x4048', *header_fields)
        self.syscom.u32('lnCelId')

    def MgmtUserAmountRespMsg(self, *header_fields):
        self.syscom.new_message('MgmtUserAmountRespMsg', 'Syscom', 'header:msgId:0x4049', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numOfPermanentUsers')
        self.syscom.u32('numOfTempUsers')

    def MgmtUserDeleteReq(self, *header_fields):
        self.syscom.new_message('MgmtUserDeleteReq', 'Syscom', 'header:msgId:0x404A', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u32('validUeId')
        self.syscom.u32('specificUeReleaseCause')
        self.syscom.u32('clearSDLdata')
        self.syscom.u32('numRbs')
        self.syscom.array('10', 'u32', 'rbIndexList')

    def MgmtRadioBearerSetupReq(self, *header_fields):
        self.syscom.new_message('MgmtRadioBearerSetupReq', 'Syscom', 'header:msgId:0x405E', *header_fields)
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ueCategory')
        self.syscom.u32('transmMode')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'u32', 'sRbIndexList')
        self.syscom.array('1', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'u32', 'rbIndexList')
        self.syscom.array('1', 'SRbInfo', 'rbInfoList')

    def MgmtRadioBearerSetupResp(self, *header_fields):
        self.syscom.new_message('MgmtRadioBearerSetupResp', 'Syscom', 'header:msgId:0x405F', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def MgmtDefaultUserConfigReq(self, *header_fields):
        self.syscom.new_message('MgmtDefaultUserConfigReq', 'Syscom', 'header:msgId:0x4069', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('l3Address')
        self.SUserInfoMac('userInfo')

    def MgmtDiscardUlPacketsReqMsg(self, *header_fields):
        self.syscom.new_message('MgmtDiscardUlPacketsReqMsg', 'Syscom', 'header:msgId:0x407E', *header_fields)
        self.syscom.u16('ueIndex')
        self.syscom.u32('numDRbs')
        self.syscom.array('8', 'SRbStopSchedulingInfo', 'rbStopSchedulingInfo')
        self.syscom.array('8', 'u32', 'rbUlForwarding')

    def MgmtDiscardUlPacketsRespMsg(self, *header_fields):
        self.syscom.new_message('MgmtDiscardUlPacketsRespMsg', 'Syscom', 'header:msgId:0x407F', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndex')

    def MacDcmUlBufferStatusInd(self, *header_fields):
        self.syscom.new_message('MacDcmUlBufferStatusInd', 'Syscom', 'header:msgId:0x4089', *header_fields)
        self.SMacMessageHeader('header')
        self.SUlBufStatusIndPayload('payload')

    def L2FetchBufferUtilMeasureResp(self, *header_fields):
        self.syscom.new_message('L2FetchBufferUtilMeasureResp', 'Syscom', 'header:msgId:0x4090', *header_fields)
        self.syscom.u32('minFreeHWDescriptors')
        self.syscom.u32('maxAllocatedUlDescriptors')
        self.syscom.u32('maxAllocatedDlDescriptors')

    def L2BufferUtilMeasureRestartInd(self, *header_fields):
        self.syscom.new_message('L2BufferUtilMeasureRestartInd', 'Syscom', 'header:msgId:0x4091', *header_fields)
        self.syscom.u32('padding')

    def L2IntUedctCellDeleteReq(self, *header_fields):
        self.syscom.new_message('L2IntUedctCellDeleteReq', 'Syscom', 'header:msgId:0x4092', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('cellIndex')

    def L2IntUeDiscardDataMsg(self, *header_fields):
        self.syscom.new_message('L2IntUeDiscardDataMsg', 'Syscom', 'header:msgId:0x4198', *header_fields)
        self.syscom.u32('cellIndex')
        self.syscom.array('16', 'u32', 'isPrioritized')
        self.MAC_BundledContentionResInd('bundledContentionResIndForward')
        self.MAC_CcchDataReceiveInd('ccchDataReceiveIndForward')

    def L2IntMacApiMeasurementInitReq(self, *header_fields):
        self.syscom.new_message('L2IntMacApiMeasurementInitReq', 'Syscom', 'header:msgId:0x41A1', *header_fields)
        self.syscom.u32('pCellL2Manager')
        self.syscom.u32('routeInitToRemotePool')
        self.syscom.u32('remotePoolSicad')
        self.syscom.u32('reportClientSicad')
        self.syscom.u32('cellId')
        self.syscom.u32('startSfn')
        self.syscom.u32('reportId')
        self.syscom.u32('period')
        self.syscom.u32('samplingPeriod')
        self.syscom.u32('groupCount')
        self.syscom.array('groupCount', 'u32', 'groupList')

    def L2IntMacApiMeasurementInitResp(self, *header_fields):
        self.syscom.new_message('L2IntMacApiMeasurementInitResp', 'Syscom', 'header:msgId:0x41A2', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('reportId')
        self.SMessageResult('messageResult')

    def L2IntMacApiMeasurementTermReq(self, *header_fields):
        self.syscom.new_message('L2IntMacApiMeasurementTermReq', 'Syscom', 'header:msgId:0x41A5', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('reportId')

    def L2IntMacApiMeasurementTermResp(self, *header_fields):
        self.syscom.new_message('L2IntMacApiMeasurementTermResp', 'Syscom', 'header:msgId:0x41A6', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('reportId')
        self.SMessageResult('messageResult')

    def L2IntTupApiMeasurementInitReq(self, *header_fields):
        self.syscom.new_message('L2IntTupApiMeasurementInitReq', 'Syscom', 'header:msgId:0x41AA', *header_fields)
        self.syscom.u32('pCellL2Manager')
        self.syscom.u32('routeInitToRemotePool')
        self.syscom.u32('remotePoolSicad')
        self.syscom.u32('lnCelId')
        self.syscom.u32('reportClientSicad')
        self.syscom.u32('startSfn')
        self.syscom.u32('measurementId')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('samplingPeriod')
        self.syscom.u32('numOfMeasurementGroupTypeList')
        self.syscom.array('numOfMeasurementGroupTypeList', 'u32', 'measurementGroupTypeList')

    def L2IntTupApiMeasurementInitResp(self, *header_fields):
        self.syscom.new_message('L2IntTupApiMeasurementInitResp', 'Syscom', 'header:msgId:0x41AB', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def L2IntTupApiMeasurementTermReq(self, *header_fields):
        self.syscom.new_message('L2IntTupApiMeasurementTermReq', 'Syscom', 'header:msgId:0x41AE', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def L2IntTupApiMeasurementTermResp(self, *header_fields):
        self.syscom.new_message('L2IntTupApiMeasurementTermResp', 'Syscom', 'header:msgId:0x41AF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')

    def MacAddressConfigReqMsg(self, *header_fields):
        self.syscom.new_message('MacAddressConfigReqMsg', 'Syscom', 'header:msgId:0x420D', *header_fields)
        self.syscom.u32('transactionId')
        self.syscom.u32('enbId')
        self.SPoolConf('poolConf')

    def MacAddressConfigRespMsg(self, *header_fields):
        self.syscom.new_message('MacAddressConfigRespMsg', 'Syscom', 'header:msgId:0x420E', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('transactionId')

    def MacMbmsBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacMbmsBearerSetupReqMsg', 'Syscom', 'header:msgId:0x4252', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('transactionId')
        self.syscom.u32('lcid')
        self.syscom.u32('sessionId')
        self.syscom.u32('mbmsSyncPeriod')
        self.syscom.u32('gtpDlTeid')
        self.syscom.u32('mbmsSyncRefHigh')
        self.syscom.u32('mbmsSyncRefLow')

    def MacMbmsBearerSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacMbmsBearerSetupRespMsg', 'Syscom', 'header:msgId:0x4253', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('transactionId')

    def MacMbmsBearerReleaseReqMsg(self, *header_fields):
        self.syscom.new_message('MacMbmsBearerReleaseReqMsg', 'Syscom', 'header:msgId:0x4254', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('transactionId')
        self.syscom.u32('lcid')
        self.syscom.u32('sessionId')

    def MacMbmsBearerReleaseRespMsg(self, *header_fields):
        self.syscom.new_message('MacMbmsBearerReleaseRespMsg', 'Syscom', 'header:msgId:0x4255', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('transactionId')

    def LteDctStartReportReqMsg(self, *header_fields):
        self.syscom.new_message('LteDctStartReportReqMsg', 'Syscom', 'header:msgId:0x4256', *header_fields)
        self.syscom.u32('reportReceiver')
        self.syscom.u32('reportName')
        self.SBrowserObjectPath('objectPath')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('itemCollectCount')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('reportingDuration')
        self.syscom.u32('numOfParams')
        self.syscom.array('numOfParams', 'u32', 'params')

    def LteDctStartReportRespMsg(self, *header_fields):
        self.syscom.new_message('LteDctStartReportRespMsg', 'Syscom', 'header:msgId:0x4257', *header_fields)
        self.syscom.u32('reportName')
        self.SBrowserObjectPath('objectPath')
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')

    def PsUserDeleteIndMsg(self, *header_fields):
        self.syscom.new_message('PsUserDeleteIndMsg', 'Syscom', 'header:msgId:0x4266', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('validUeId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('numOfAbnormallyReleasedDRbList')
        self.syscom.array('8', 'u32', 'abnormallyReleasedDRbList')
        self.syscom.u32('hasUeReleaseCause')
        self.syscom.u32('ueReleaseCause')
        self.syscom.u32('hasSpecificUeReleaseCause')
        self.syscom.u32('specificUeReleaseCause')

    def PsAddressConfigReqMsg(self, *header_fields):
        self.syscom.new_message('PsAddressConfigReqMsg', 'Syscom', 'header:msgId:0x4267', *header_fields)
        self.syscom.u32('ulCellMac')
        self.syscom.u32('ulSchedulerMac')
        self.syscom.u32('dlCellMac')
        self.syscom.u32('dlSchedulerMac')
        self.syscom.u32('numOfUeGroups')
        self.syscom.u32('ueGroups')
        self.syscom.u32('numOfUeGroupsPerPool')
        self.syscom.array('16', 'u32', 'dataCtrlUl')
        self.syscom.array('16', 'u32', 'dataCtrlDlData')
        self.syscom.array('16', 'u32', 'dataCtrlScellDataTransf')
        self.syscom.array('16', 'u32', 'dataCtrlDiscard')
        self.syscom.array('16', 'u32', 'puschReceiveRespUAddress')
        self.syscom.u32('macUser')
        self.syscom.u32('dataMeas')
        self.syscom.u32('psCellClient')
        self.syscom.u32('psUserClient')
        self.syscom.u32('enbId')
        self.SPoolConf('poolConf')

    def PsAddressConfigRespMsg(self, *header_fields):
        self.syscom.new_message('PsAddressConfigRespMsg', 'Syscom', 'header:msgId:0x4268', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('numOfUeGroups')
        self.syscom.array('16', 'u32', 'dataCtrlUlClient')
        self.syscom.array('16', 'u32', 'dataCtrlDlClient')
        self.syscom.array('16', 'u32', 'dataCtrlRachClient')

    def PsRrcConnectionReconfCompletedReqMsg(self, *header_fields):
        self.syscom.new_message('PsRrcConnectionReconfCompletedReqMsg', 'Syscom', 'header:msgId:0x4269', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('relatedProcedure')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('4', 'SCqiParamsScell', 'cqiParamsScell')
        self.syscom.u32('hasTmSwitch')
        self.STmSwitch('tmSwitch')
        self.syscom.u32('hasNewTmSwitch')
        self.syscom.array('5', 'u32', 'newTmSwitch')
        self.syscom.u32('hasModNumOfLayers')
        self.syscom.array('5', 'SModNumOfLayers', 'modNumOfLayers')
        self.syscom.u32('hasEnableNonGbrBufferMonitoring')
        self.syscom.u32('enableNonGbrBufferMonitoring')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('hasMeasGapStopRequired')
        self.syscom.u32('measGapStopRequired')

    def MacRemoveUesInCellReqMsg(self, *header_fields):
        self.syscom.new_message('MacRemoveUesInCellReqMsg', 'Syscom', 'header:msgId:0x4270', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('pCelId')
        self.syscom.u32('numOfUeToRemove')
        self.syscom.array('numOfUeToRemove', 'u16', 'ueToRemove')

    def MacRemoveUesInCellRespMsg(self, *header_fields):
        self.syscom.new_message('MacRemoveUesInCellRespMsg', 'Syscom', 'header:msgId:0x4271', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')

    def LteDctStopReportReqMsg(self, *header_fields):
        self.syscom.new_message('LteDctStopReportReqMsg', 'Syscom', 'header:msgId:0x4273', *header_fields)
        self.syscom.u32('reportName')
        self.SBrowserObjectPath('objectPath')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')

    def LteDctStopReportRespMsg(self, *header_fields):
        self.syscom.new_message('LteDctStopReportRespMsg', 'Syscom', 'header:msgId:0x4274', *header_fields)
        self.syscom.u32('reportName')
        self.SBrowserObjectPath('objectPath')
        self.syscom.u32('status')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')

    def MacCaUserReconfigurationCompleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacCaUserReconfigurationCompleteReqMsg', 'Syscom', 'header:msgId:0x4275', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('procedureResults')

    def MacCaUserReconfigurationCompleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacCaUserReconfigurationCompleteRespMsg', 'Syscom', 'header:msgId:0x4276', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def MacRrcConnectionReconfCompletedReqMsg(self, *header_fields):
        self.syscom.new_message('MacRrcConnectionReconfCompletedReqMsg', 'Syscom', 'header:msgId:0x4277', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('relatedProcedure')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('numOfCqiParamsScell')
        self.syscom.array('4', 'SCqiParamsScell', 'cqiParamsScell')
        self.syscom.u32('hasTmSwitch')
        self.STmSwitch('tmSwitch')
        self.syscom.u32('hasNewTmSwitch')
        self.syscom.array('5', 'u32', 'newTmSwitch')
        self.syscom.u32('hasModNumOfLayers')
        self.syscom.array('5', 'SModNumOfLayers', 'modNumOfLayers')
        self.syscom.u32('hasEnableNonGbrBufferMonitoring')
        self.syscom.u32('enableNonGbrBufferMonitoring')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.u32('hasMeasGapStopRequired')
        self.syscom.u32('measGapStopRequired')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')

    def PsCaUserReconfigurationCompleteReqMsg(self, *header_fields):
        self.syscom.new_message('PsCaUserReconfigurationCompleteReqMsg', 'Syscom', 'header:msgId:0x4280', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('procedureResults')

    def PsCaUserReconfigurationCompleteRespMsg(self, *header_fields):
        self.syscom.new_message('PsCaUserReconfigurationCompleteRespMsg', 'Syscom', 'header:msgId:0x4281', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def MacPdumuxExceptionIndMsg(self, *header_fields):
        self.syscom.new_message('MacPdumuxExceptionIndMsg', 'Syscom', 'header:msgId:0x4284', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u16('frameNumber')
        self.syscom.u16('subFrameNumber')
        self.syscom.u32('numOfResponses')
        self.syscom.array('numOfResponses', 'SPduMuxDataResultEntry', 'resArray')

    def MacMbmsPduMuxDataReqMsg(self, *header_fields):
        self.syscom.new_message('MacMbmsPduMuxDataReqMsg', 'Syscom', 'header:msgId:0x428F', *header_fields)
        self.syscom.u16('cellId')
        self.syscom.u16('frameNumber')
        self.syscom.u8('subFrameNumber')
        self.syscom.u8('cfi')
        self.syscom.u8('lastTbInTti')
        self.syscom.u8('needsToBeMuted')
        self.syscom.u32('allowedTimeStampLow')
        self.syscom.u32('allowedTimeStampHigh')
        self.syscom.i32('mbsfnRsPower')
        self.SPduMuxDataReq('mbmsdata')
        self.SMbmsPduCtrlReq('mbmsctrl')

    def MacL2SdlIndMsg(self, *header_fields):
        self.syscom.new_message('MacL2SdlIndMsg', 'Syscom', 'header:msgId:0x4290', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('amDlRlcNewBytes')
        self.syscom.u32('tmDlRlcNewBytes')
        self.syscom.u32('umDlRlcNewBytes')
        self.syscom.u32('amDlRlcRexmitBytes')
        self.syscom.u32('amUlRlcNewBytes')
        self.syscom.u32('tmUlRlcNewBytes')
        self.syscom.u32('umUlRlcNewBytes')
        self.syscom.u32('gtpuUlNewBytes')
        self.syscom.u32('gtpuDlNewBytes')

    def MacSyncMeasurementReportIndMsg(self, *header_fields):
        self.syscom.new_message('MacSyncMeasurementReportIndMsg', 'Syscom', 'header:msgId:0x429C', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')
        self.syscom.u32('startSfn')
        self.syscom.u32('numOfMacSduReport')
        self.syscom.array('numOfMacSduReport', 'SMacSduReport', 'macSduReport')

    def TupGtpuDammariDiagnosticsReqMsg(self, *header_fields):
        self.syscom.new_message('TupGtpuDammariDiagnosticsReqMsg', 'Syscom', 'header:msgId:0x42DE', *header_fields)
        self.syscom.u16('remoteDeviceId')
        self.syscom.u16('paddingDeviceId')

    def TupGtpuDammariDiagnosticsRespMsg(self, *header_fields):
        self.syscom.new_message('TupGtpuDammariDiagnosticsRespMsg', 'Syscom', 'header:msgId:0x42DF', *header_fields)
        self.syscom.u16('remoteDeviceId')
        self.syscom.u16('paddingDeviceId')
        self.syscom.u32('numOfResultList')
        self.syscom.array('numOfResultList', 'SGtpuPathDiagnosticsResult', 'resultList')

    def PsUlPrbsAvailIndMsg(self, *header_fields):
        self.syscom.new_message('PsUlPrbsAvailIndMsg', 'Syscom', 'header:msgId:0x42E0', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('startFrameNumber')
        self.syscom.u32('startSubFrameNumber')
        self.syscom.u32('endFrameNumber')
        self.syscom.u32('endSubFrameNumber')
        self.syscom.u32('counterUlPrbsAvail')

    def PsDlPrbsAvailIndMsg(self, *header_fields):
        self.syscom.new_message('PsDlPrbsAvailIndMsg', 'Syscom', 'header:msgId:0x42E1', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('startFrameNumber')
        self.syscom.u32('startSubFrameNumber')
        self.syscom.u32('endFrameNumber')
        self.syscom.u32('endSubFrameNumber')
        self.syscom.u32('counterDlPrbsAvail')

    def MacCellToPoolAttachReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellToPoolAttachReqMsg', 'Syscom', 'header:msgId:0x4348', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')
        self.syscom.u32('useInterSiteCA')
        self.SWmpDcmCaParamsContainer('container')

    def MacCellToPoolAttachRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellToPoolAttachRespMsg', 'Syscom', 'header:msgId:0x4349', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')

    def MacCellToPoolDetachReqMsg(self, *header_fields):
        self.syscom.new_message('MacCellToPoolDetachReqMsg', 'Syscom', 'header:msgId:0x434A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')

    def MacCellToPoolDetachRespMsg(self, *header_fields):
        self.syscom.new_message('MacCellToPoolDetachRespMsg', 'Syscom', 'header:msgId:0x434B', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')

    def MacPduMuxCombinedReqMsg(self, *header_fields):
        self.syscom.new_message('MacPduMuxCombinedReqMsg', 'Syscom', 'header:msgId:0x4362', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('enbId')
        self.syscom.u16('frameNumber')
        self.syscom.u8('subFrameNumber')
        self.syscom.u8('numOfHarqReleaseCombInfo')
        self.syscom.u8('numOfPduMuxDataCombReq')
        self.syscom.u8('numOfTddPduMuxDataCombReq')
        self.syscom.u8('lastTbInTti')
        self.syscom.u8('latencyBudgetExceeded')
        self.syscom.array('1', 'u32', 'dynamicData')

    def PsCellToPoolAttachReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellToPoolAttachReqMsg', 'Syscom', 'header:msgId:0x4363', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')
        self.syscom.u32('useInterSiteCA')
        self.UWmpDcmCaParamsContainer('macPsCaParamsContainer')

    def PsCellToPoolAttachRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellToPoolAttachRespMsg', 'Syscom', 'header:msgId:0x4364', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u32('transactionId')

    def PsCellToPoolDetachReqMsg(self, *header_fields):
        self.syscom.new_message('PsCellToPoolDetachReqMsg', 'Syscom', 'header:msgId:0x4365', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('relatedCelId')
        self.syscom.u32('relatedEnbId')
        self.syscom.u32('transactionId')

    def PsCellToPoolDetachRespMsg(self, *header_fields):
        self.syscom.new_message('PsCellToPoolDetachRespMsg', 'Syscom', 'header:msgId:0x4366', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('relatedCelId')
        self.syscom.u32('relatedEnbId')
        self.SMessageResult('messageResult')
        self.syscom.u32('transactionId')

    def PsStopRelatedUesReqMsg(self, *header_fields):
        self.syscom.new_message('PsStopRelatedUesReqMsg', 'Syscom', 'header:msgId:0x4399', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('relatedCelId')
        self.syscom.u32('relatedEnbId')

    def PsStopRelatedUesRespMsg(self, *header_fields):
        self.syscom.new_message('PsStopRelatedUesRespMsg', 'Syscom', 'header:msgId:0x439A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('relatedCelId')
        self.syscom.u32('relatedEnbId')
        self.SMessageResult('messageResult')

    def MacUlBufferStatusBundleIndMsg(self, *header_fields):
        self.syscom.new_message('MacUlBufferStatusBundleIndMsg', 'Syscom', 'header:msgId:0x43A9', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('numberOfUes')
        self.syscom.array('numberOfUes', 'SUlUeBufferStatus', 'ueIdInfo')

    def PsCrntiReleaseRespMsg(self, *header_fields):
        self.syscom.new_message('PsCrntiReleaseRespMsg', 'Syscom', 'header:msgId:0x43AD', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('ueId')

    def MacPduMuxUegroupBundleReqMsg(self, *header_fields):
        self.syscom.new_message('MacPduMuxUegroupBundleReqMsg', 'Syscom', 'header:msgId:0x43B9', *header_fields)
        self.syscom.u32('numOfCellSpecificMessages')
        self.syscom.array('12', 'u16', 'sizeOfMessage')
        self.syscom.array('1', 'u32', 'dynamicData')

    def PsCaUeAddInScellReqMsg(self, *header_fields):
        self.syscom.new_message('PsCaUeAddInScellReqMsg', 'Syscom', 'header:msgId:0x43C1', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('ueIndexData')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('poolIdData')
        self.syscom.u32('relatedProcedure')
        self.SPCellParams('pCellParams')
        self.SOtherSCellUeParams('otherSCellUeParams')
        self.SPCellUeParams('pCellUeParams')
        self.SSCellUeParams('sCellUeParams')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')

    def PsCaUeAddInScellRespMsg(self, *header_fields):
        self.syscom.new_message('PsCaUeAddInScellRespMsg', 'Syscom', 'header:msgId:0x43C2', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')
        self.SMessageResult('messageResult')

    def PsCaUeScellReconfigReqMsg(self, *header_fields):
        self.syscom.new_message('PsCaUeScellReconfigReqMsg', 'Syscom', 'header:msgId:0x43C3', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')
        self.syscom.u32('relatedProcedure')
        self.SPCellParams('pCellParams')
        self.SSCellUeParams('sCellUeParams')
        self.SOtherSCellUeParams('otherSCellUeParams')

    def PsCaUeScellReconfigRespMsg(self, *header_fields):
        self.syscom.new_message('PsCaUeScellReconfigRespMsg', 'Syscom', 'header:msgId:0x43C4', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('enbId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('crnti')
        self.SMessageResult('messageResult')

    def MacResourcesUsageInfoReqMsg(self, *header_fields):
        self.syscom.new_message('MacResourcesUsageInfoReqMsg', 'Syscom', 'header:msgId:0x43FE', *header_fields)
        self.syscom.u32('poolId')
        self.syscom.u32('requestType')

    def MacResourcesUsageInfoRespMsg(self, *header_fields):
        self.syscom.new_message('MacResourcesUsageInfoRespMsg', 'Syscom', 'header:msgId:0x43FF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('poolId')
        self.syscom.u32('numCells')
        self.syscom.array('8', 'SUserResourcesPerCell', 'userResourcesPerCell')
        self.SUserResourcesSummary('userResourcesPerPool')
        self.syscom.u32('numContextInfos')
        self.syscom.array('numContextInfos', 'SContextInfo', 'contextInfoList')

    def L2IntRachsetupind(self, *header_fields):
        self.syscom.new_message('L2IntRachsetupind', 'Syscom', 'header:msgId:0x4407', *header_fields)
        self.syscom.u32('cellIndex')
        self.syscom.u32('raContResoT')
        self.syscom.u32('raCrntiReuseT')
        self.syscom.u32('raMsg3Thr')
        self.syscom.u32('raNondedPreamb')
        self.syscom.u32('timerRaComp')
        self.syscom.u32('pdschEventQueueId')
        self.syscom.u32('hasRaMsg3Thr')
        self.syscom.u32('hasRaMsg3ThrLowParameters')
        self.SRaMsg3ThrCntParameters('raMsg3ThrCntParameters')
        self.SRaMsg3ThrLowParameters('raMsg3ThrLowParameters')
        self.syscom.u32('hasRaMsg3ThrCntParameters')
        self.syscom.u32('cntId')

    def L2IntReceivedPsAddressesInd(self, *header_fields):
        self.syscom.new_message('L2IntReceivedPsAddressesInd', 'Syscom', 'header:msgId:0x4421', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('cellIndex')
        self.syscom.u32('macSgnl')
        self.syscom.u32('macCellMeas')
        self.syscom.u32('macUserPs')
        self.syscom.u32('dataCtrlPdcchClient')
        self.syscom.u32('dataCtrlMbmsClient')
        self.syscom.u32('psUserMgmt')
        self.syscom.u32('psUserUl')
        self.syscom.u32('psUserDl')
        self.syscom.u32('psUserDisableDlAndSCell')

    def PsSrbUeReconfigReqMsg(self, *header_fields):
        self.syscom.new_message('PsSrbUeReconfigReqMsg', 'Syscom', 'header:msgId:0x44FE', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('ueIndexTemp')
        self.syscom.u32('poolIdData')
        self.syscom.u16('ueIndexData')
        self.syscom.u16('paddingUeIndexData')

    def PsSrbUeReconfigRespMsg(self, *header_fields):
        self.syscom.new_message('PsSrbUeReconfigRespMsg', 'Syscom', 'header:msgId:0x44FF', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def MacScellUserSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellUserSetupReqMsg', 'Syscom', 'header:msgId:0x4527', *header_fields)
        self.syscom.u32('cellIdSCell')
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexDataSCell')
        self.syscom.u32('enbIdSCell')
        self.syscom.u32('poolId')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('enbIdPCell')
        self.syscom.u32('cellIdPCell')
        self.syscom.u32('ueCategory')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfoSCell', 'rbInfoList')

    def MacScellUserSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacScellUserSetupRespMsg', 'Syscom', 'header:msgId:0x452A', *header_fields)
        self.syscom.u32('cellIdSCell')
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexDataSCell')
        self.syscom.u32('poolIdData')
        self.syscom.u32('enbIdSCell')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u16('paddingUeIndex')
        self.SMessageResult('messageResult')

    def MacScellUserDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellUserDeleteReqMsg', 'Syscom', 'header:msgId:0x452B', *header_fields)
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexPCell')

    def MacScellRlcPduReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellRlcPduReqMsg', 'Syscom', 'header:msgId:0x452D', *header_fields)
        self.syscom.u32('logicalChannelId')
        self.syscom.u16('ueIndexDataSCell')
        self.syscom.u16('rlcPduSize')
        self.syscom.array('rlcPduSize', 'u8', 'rlcPdu')

    def MacScellUserDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacScellUserDeleteRespMsg', 'Syscom', 'header:msgId:0x452F', *header_fields)
        self.syscom.u16('ueIndexPCell')
        self.syscom.u16('ueIndexSCell')
        self.SMessageResult('messageResult')

    def MacScellRadioBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellRadioBearerSetupReqMsg', 'Syscom', 'header:msgId:0x4530', *header_fields)
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u32('ueCategory')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SRbInfoSCell', 'drbInfoList')

    def MacScellRadioBearerSetupRespMsg(self, *header_fields):
        self.syscom.new_message('MacScellRadioBearerSetupRespMsg', 'Syscom', 'header:msgId:0x4559', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexPCell')

    def MacScellRadioBearerDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellRadioBearerDeleteReqMsg', 'Syscom', 'header:msgId:0x4562', *header_fields)
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexPCell')
        self.syscom.u32('numRbs')
        self.syscom.array('8', 'u8', 'rbList')

    def MacScellRadioBearerDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('MacScellRadioBearerDeleteRespMsg', 'Syscom', 'header:msgId:0x4563', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('ueIndexPCell')

    def MacPoolToPoolDetachReqMsg(self, *header_fields):
        self.syscom.new_message('MacPoolToPoolDetachReqMsg', 'Syscom', 'header:msgId:0x4585', *header_fields)
        self.syscom.u32('poolId')

    def MacPoolToPoolDetachRespMsg(self, *header_fields):
        self.syscom.new_message('MacPoolToPoolDetachRespMsg', 'Syscom', 'header:msgId:0x4586', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('poolId')

    def MacWmpMacPduDumpStartReqMsg(self, *header_fields):
        self.syscom.new_message('MacWmpMacPduDumpStartReqMsg', 'Syscom', 'header:msgId:0x4593', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')
        self.syscom.u32('targetSicad')

    def MacWmpMacPduDumpStartRespMsg(self, *header_fields):
        self.syscom.new_message('MacWmpMacPduDumpStartRespMsg', 'Syscom', 'header:msgId:0x4594', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')

    def MacWmpMacPduDumpStopReqMsg(self, *header_fields):
        self.syscom.new_message('MacWmpMacPduDumpStopReqMsg', 'Syscom', 'header:msgId:0x4595', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')

    def MacWmpMacPduDumpStopRespMsg(self, *header_fields):
        self.syscom.new_message('MacWmpMacPduDumpStopRespMsg', 'Syscom', 'header:msgId:0x4596', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('lnCelId')
        self.syscom.u32('ueId')

    def PsResourcesUsageInfoReqMsg(self, *header_fields):
        self.syscom.new_message('PsResourcesUsageInfoReqMsg', 'Syscom', 'header:msgId:0x4597', *header_fields)
        self.syscom.u32('macPsInstanceId')
        self.syscom.u32('requestType')

    def PsResourcesUsageInfoRespMsg(self, *header_fields):
        self.syscom.new_message('PsResourcesUsageInfoRespMsg', 'Syscom', 'header:msgId:0x4598', *header_fields)
        self.syscom.u32('macPsInstanceId')
        self.syscom.u32('numCells')
        self.syscom.array('8', 'SUserResourcesPerCell', 'userResourcesPerCell')
        self.syscom.u32('numContextInfos')
        self.syscom.array('numContextInfos', 'SContextInfo', 'contextInfoList')

    def MacUlUePowerInfoIndMsg(self, *header_fields):
        self.syscom.new_message('MacUlUePowerInfoIndMsg', 'Syscom', 'header:msgId:0x45A6', *header_fields)
        self.syscom.u32('lnCelId')
        self.SUlUePowerInfo('ulUePowerInfo')

    def MacScellDataTransferReqMsg(self, *header_fields):
        self.syscom.new_message('MacScellDataTransferReqMsg', 'Syscom', 'header:msgId:0x45A7', *header_fields)
        self.syscom.u32('numOfScellDataTransferData')
        self.syscom.array('numOfScellDataTransferData', 'SScellDataTransferData', 'scellDataTransferData')

    def PsPoolToPoolDetachReqMsg(self, *header_fields):
        self.syscom.new_message('PsPoolToPoolDetachReqMsg', 'Syscom', 'header:msgId:0x45B2', *header_fields)
        self.syscom.u32('poolId')

    def PsPoolToPoolDetachRespMsg(self, *header_fields):
        self.syscom.new_message('PsPoolToPoolDetachRespMsg', 'Syscom', 'header:msgId:0x45B3', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('poolId')

    def MacUserSetPlmnReqMsg(self, *header_fields):
        self.syscom.new_message('MacUserSetPlmnReqMsg', 'Syscom', 'header:msgId:0x4608', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.SPlmnId('plmnId')

    def MacMacSduRateMeasurementReportIndMsg(self, *header_fields):
        self.syscom.new_message('MacMacSduRateMeasurementReportIndMsg', 'Syscom', 'header:msgId:0x4611', *header_fields)
        self.syscom.u32('poolIdSource')
        self.syscom.u32('startSfn')
        self.syscom.u32('numOfMacSduRateReport')
        self.syscom.array('numOfMacSduRateReport', 'SMacSduRateReport', 'macSduRateReport')

    def PhyStubInitializeReqMsg(self, *header_fields):
        self.syscom.new_message('PhyStubInitializeReqMsg', 'Syscom', 'header:msgId:0x5400', *header_fields)
        self.syscom.u32('packetReordering')

    def PhyStubInitializeRespMsg(self, *header_fields):
        self.syscom.new_message('PhyStubInitializeRespMsg', 'Syscom', 'header:msgId:0x5401', *header_fields)
        self.syscom.u32('status')

    def PhyStubConfigureReqMsg(self, *header_fields):
        self.syscom.new_message('PhyStubConfigureReqMsg', 'Syscom', 'header:msgId:0x5402', *header_fields)
        self.syscom.u32('numOfCells')
        self.syscom.array('1', 'PHYSTUB_CellData', 'cellData')

    def PhyStubConfigureRespMsg(self, *header_fields):
        self.syscom.new_message('PhyStubConfigureRespMsg', 'Syscom', 'header:msgId:0x5403', *header_fields)
        self.syscom.u32('status')

    def PhyStubConfigureUserRespMsg(self, *header_fields):
        self.syscom.new_message('PhyStubConfigureUserRespMsg', 'Syscom', 'header:msgId:0x5405', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('robotTesterBufferPtr')

    def PhyStubTbStatsReq(self, *header_fields):
        self.syscom.new_message('PhyStubTbStatsReq', 'Syscom', 'header:msgId:0x5408', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('resetStats')

    def PhyStubTbStatsResp(self, *header_fields):
        self.syscom.new_message('PhyStubTbStatsResp', 'Syscom', 'header:msgId:0x5409', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('numOfTb')
        self.syscom.u32('numOfSdu')
        self.syscom.u32('totalKb')
        self.syscom.u32('curBitRateKb')
        self.syscom.u32('maxBitRateKb')
        self.syscom.u32('lastNir')
        self.syscom.u32('numOfTTI')
        self.syscom.u32('initTxTb')
        self.syscom.u32('initTxKb')
        self.syscom.u32('reTxTb')
        self.syscom.u32('reTxKb')
        self.syscom.u32('discardedTb')
        self.syscom.u32('discardedKb')
        self.syscom.u32('maxNumOfTbPerTti')
        self.syscom.u32('occurencesOfMaxNumOfTbPerTti')
        self.syscom.u32('crntiWhenFirstTBAdded')
        self.syscom.array('10', 'u32', 'crntiTable')

    def PhyStubDeleteUserReq(self, *header_fields):
        self.syscom.new_message('PhyStubDeleteUserReq', 'Syscom', 'header:msgId:0x540A', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')

    def PhyStubDeleteUserResp(self, *header_fields):
        self.syscom.new_message('PhyStubDeleteUserResp', 'Syscom', 'header:msgId:0x540B', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')

    def RlcMacCellSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcMacCellSetupReqMsg', 'Syscom', 'header:msgId:0x5410', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('lCelId')
        self.syscom.u32('dlChBw')
        self.syscom.u32('ulChBw')
        self.syscom.u32('mimoMode')
        self.syscom.u32('dlPhyDataAddress')
        self.syscom.u32('ulPhyDataAddress')
        self.syscom.u32('maxNumUeDl')
        self.syscom.u32('maxNumUeUl')
        self.syscom.u32('MacCellInterfaceAddress')
        self.syscom.u32('thOverflowDiscard')
        self.syscom.u32('flagOverflowDiscard')
        self.syscom.u32('discBuffThrAct')
        self.syscom.u32('discBuffHighThr')

    def RlcRachSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcRachSetupReqMsg', 'Syscom', 'header:msgId:0x5411', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('lCelId')
        self.syscom.u32('MacCellInterfaceAddress')
        self.syscom.u32('hasRaMsg3Thr')
        self.syscom.u32('raMsg3Thr')
        self.syscom.u32('timerRaComp')

    def PhyStubAddPuschRespReceiverReqMsg(self, *header_fields):
        self.syscom.new_message('PhyStubAddPuschRespReceiverReqMsg', 'Syscom', 'header:msgId:0x5412', *header_fields)
        self.syscom.u32('index')
        self.syscom.u32('nodeId')
        self.syscom.u32('sicad')

    def RlcTupCellSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcTupCellSetupReqMsg', 'Syscom', 'header:msgId:0x5414', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('tupDlSicad')

    def RlcTupUserSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcTupUserSetupReqMsg', 'Syscom', 'header:msgId:0x5416', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('macUserAddr')
        self.syscom.u32('tupDlSicad')
        self.syscom.u32('qci')
        self.syscom.u32('srbRlcMode')
        self.syscom.u32('drbRlcMode')
        self.syscom.u32('numSRbs')

    def RlcTupBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcTupBearerSetupReqMsg', 'Syscom', 'header:msgId:0x5418', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('srbId')
        self.syscom.u32('drbId')
        self.syscom.u32('tupDlSicad')
        self.syscom.u32('qci')
        self.syscom.u32('srbRlcMode')
        self.syscom.u32('drbRlcMode')

    def PhyStubSequencerConfPrachMsg(self, *header_fields):
        self.syscom.new_message('PhyStubSequencerConfPrachMsg', 'Syscom', 'header:msgId:0x5419', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('macTestInterface')

    def RlcRadioBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('RlcRadioBearerSetupReqMsg', 'Syscom', 'header:msgId:0x541A', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('srbRlcMode')
        self.syscom.u32('numSRbs')
        self.syscom.u32('srbId')
        self.syscom.u32('numDRbs')
        self.syscom.u32('drbId')
        self.syscom.u32('drbRlcMode')
        self.syscom.u32('dlSupportUeSicad')
        self.syscom.u32('drbType')
        self.syscom.u32('lcId')
        self.syscom.u32('lcgId')
        self.syscom.u32('ueParams_transmMode')
        self.syscom.u32('drb_rlcAmParameters_maxRlcReTrans')
        self.syscom.u32('ueCategory')

    def RlcMgmtRadioBearerSetupReq(self, *header_fields):
        self.syscom.new_message('RlcMgmtRadioBearerSetupReq', 'Syscom', 'header:msgId:0x541B', *header_fields)
        self.syscom.u32('ueId')
        self.syscom.u32('numSRbs')
        self.syscom.u32('numRbs')
        self.syscom.u32('drbId')
        self.syscom.u32('msgReceiver')

    def RlcRadioBearerModifyReqMsg(self, *header_fields):
        self.syscom.new_message('RlcRadioBearerModifyReqMsg', 'Syscom', 'header:msgId:0x541C', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('srbRlcMode')
        self.syscom.u32('numSRbs')
        self.syscom.u32('srbId')
        self.syscom.u32('numRbs')
        self.syscom.u32('drbId')
        self.syscom.u32('drbRlcMode')
        self.syscom.u32('dlSupportUeSicad')
        self.syscom.u32('drbType')
        self.syscom.u32('lcId')
        self.syscom.u32('lcgId')
        self.syscom.u32('lcIndex')
        self.syscom.u32('ueCategory')

    def RlcRadioBearerDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('RlcRadioBearerDeleteReqMsg', 'Syscom', 'header:msgId:0x541D', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('numSRbs')
        self.syscom.u32('srbId')
        self.syscom.u32('numRbs')
        self.syscom.u32('drbId')
        self.syscom.u32('dlSupportUeSicad')
        self.syscom.u32('ueCategory')

    def RlcTupBearerDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('RlcTupBearerDeleteReqMsg', 'Syscom', 'header:msgId:0x541E', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('srbId')
        self.syscom.u32('drbId')
        self.syscom.u32('tupDlSicad')

    def PhyStubDiscardTbsReq(self, *header_fields):
        self.syscom.new_message('PhyStubDiscardTbsReq', 'Syscom', 'header:msgId:0x5420', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('tbDiscardSequence')
        self.syscom.u32('discardInitialHarqTx')
        self.syscom.u32('continuous')

    def PhyStubDiscardTbsResp(self, *header_fields):
        self.syscom.new_message('PhyStubDiscardTbsResp', 'Syscom', 'header:msgId:0x5421', *header_fields)
        self.syscom.u32('status')

    def PhyStubDataReceivedIndMsg(self, *header_fields):
        self.syscom.new_message('PhyStubDataReceivedIndMsg', 'Syscom', 'header:msgId:0x5422', *header_fields)
        self.syscom.u32('crnti')
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')

    def PhyStubPuschRecRespUResp(self, *header_fields):
        self.syscom.new_message('PhyStubPuschRecRespUResp', 'Syscom', 'header:msgId:0x5423', *header_fields)
        self.syscom.u32('correctedSfn')
        self.syscom.u32('correctedSubFrame')

    def PhyStubPhyPuschReceiveRespUSequenceMsg(self, *header_fields):
        self.syscom.new_message('PhyStubPhyPuschReceiveRespUSequenceMsg', 'Syscom', 'header:msgId:0x5424', *header_fields)
        self.syscom.u32('periodFrame')
        self.PHY_PuschReceiveRespU('respUSequenceMsg')
        self.syscom.array('8', 'u8', 'data')

    def PhyStubPhyPuschReceiveRespUSequenceMsgResp(self, *header_fields):
        self.syscom.new_message('PhyStubPhyPuschReceiveRespUSequenceMsgResp', 'Syscom', 'header:msgId:0x5425', *header_fields)
        self.syscom.u32('waitFrames')
        self.syscom.array('20', 'u16', 'sequence')

    def PhyStubConfSequencerReqMsg(self, *header_fields):
        self.syscom.new_message('PhyStubConfSequencerReqMsg', 'Syscom', 'header:msgId:0x5426', *header_fields)
        self.syscom.u32('product')
        self.syscom.u32('measType')
        self.syscom.u32('measurementObject')
        self.syscom.u32('carrierBandwidth')
        self.syscom.u32('receptionSubframes')
        self.syscom.u32('expectionSubframes')
        self.syscom.u32('missedSubframes')
        self.syscom.u32('wrongTimingSubframes')
        self.syscom.u32('preambleNotExpected')
        self.syscom.u32('wrongPaSubframes')
        self.syscom.u32('reportingTimeInterval')
        self.syscom.u32('harqAckNotAttempted')
        self.syscom.u32('harqAckTxNegative')
        self.syscom.u32('harqAckInvalid')

    def PhyStubConfSequencerRespMsg(self, *header_fields):
        self.syscom.new_message('PhyStubConfSequencerRespMsg', 'Syscom', 'header:msgId:0x5427', *header_fields)
        self.syscom.u32('status')

    def PhyStubSequencerStatReqMsg(self, *header_fields):
        self.syscom.new_message('PhyStubSequencerStatReqMsg', 'Syscom', 'header:msgId:0x5428', *header_fields)

    def PhyStubSequencerStatRespMsg(self, *header_fields):
        self.syscom.new_message('PhyStubSequencerStatRespMsg', 'Syscom', 'header:msgId:0x5429', *header_fields)
        self.syscom.u32('latestResult')
        self.syscom.array('5', 'PHYSTUB_sequencerStats', 'results')

    def PhyStubMbmsStatsReq(self, *header_fields):
        self.syscom.new_message('PhyStubMbmsStatsReq', 'Syscom', 'header:msgId:0x5430', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('resetStats')

    def PhyStubMbmsStatsResp(self, *header_fields):
        self.syscom.new_message('PhyStubMbmsStatsResp', 'Syscom', 'header:msgId:0x5431', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('numOfTb')
        self.syscom.u32('numOfTTI')
        self.syscom.u32('lastFrameNumber')
        self.syscom.u32('lastSubFrameNumber')
        self.syscom.u32('lastTbSize')
        self.syscom.u32('mcchSize')
        self.syscom.u32('msiSize')
        self.syscom.u32('mcchSn')
        self.syscom.array('10', 'SMchScheduleInfo', 'msiData')
        self.syscom.array('29', 'SDlSchPduMuxAmountOctets', 'pduOctets')

    def PhystubUlPhyDataAddressReqMsg(self, *header_fields):
        self.syscom.new_message('PhystubUlPhyDataAddressReqMsg', 'Syscom', 'header:msgId:0x5510', *header_fields)
        self.syscom.u32('lnCelId')
        self.syscom.u32('prachReceiveIndAddress')
        self.syscom.u32('receiveRespDAddress')
        self.syscom.u32('receiveCqiRespDAddress')
        self.syscom.u32('puschReceiveMeasRespAddress1')
        self.syscom.u32('puschReceiveMeasRespAddress2')
        self.syscom.u32('numOfUeGroups')
        self.syscom.array('16', 'u32', 'puschReceiveRespUAddress')
        self.syscom.u32('puschReceiveRespUAddress2')
        self.syscom.u32('pucchReceiveMeasRespAddress1')
        self.syscom.u32('pucchReceiveMeasRespAddress2')
        self.syscom.u32('pucchReceiveRespUAddress')
        self.syscom.u32('srsReceiveRespDAddress')
        self.syscom.u32('srsReceiveRespUAddress')
        self.syscom.u32('puschCellMeasRespAddress')
        self.syscom.u32('pucchCellMeasRespAddress')
        self.syscom.u32('srsCellMeasRespAddress')
        self.syscom.u32('srsBfCovMatrixMeasRespAddress')
        self.syscom.u32('ulResourceUpdateAddress')

    def GtpGenericRespMsg(self, *header_fields):
        self.syscom.new_message('GtpGenericRespMsg', 'Syscom', 'header:msgId:0x7000', *header_fields)
        self.syscom.u32('dontCare')

    def GtpReceiverAddressConfigReqMsg(self, *header_fields):
        self.syscom.new_message('GtpReceiverAddressConfigReqMsg', 'Syscom', 'header:msgId:0x7001', *header_fields)
        self.SGtpAddressesOfLteL2('sut')
        self.SGtpAddressesOfLteL2('ueSim1')
        self.SGtpAddressesOfLteL2('ueSim2')

    def GtpBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('GtpBearerSetupReqMsg', 'Syscom', 'header:msgId:0x7002', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.SProtocolStackProfile('protoStackProfile')
        self.syscom.u32('e')
        self.syscom.u32('numberOfUeSims')
        self.syscom.u32('drbId')
        self.syscom.u32('enbX2DlTeid')
        self.syscom.u32('enbX2UlTeid')
        self.syscom.u32('maxNumUeGroup')
        self.syscom.u32('numOfManuallyActivatedUeGroups')
        self.syscom.array('24', 'u32', 'manuallyActiveUegroups')
        self.syscom.u32('numOfUsers')
        self.syscom.array('numOfUsers', 'SGtpUser', 'users')

    def FaultManagerInitReqMsg(self, *header_fields):
        self.syscom.new_message('FaultManagerInitReqMsg', 'Syscom', 'header:msgId:0x800B', *header_fields)
        self.syscom.u32('recAddressForFaults')
        self.syscom.u32('blockAllFaults')
        self.syscom.u32('numberOfFaultFilteringElements')
        self.syscom.array('1', 'SFaultFiltering', 'faultFiltering')

    def FaultManagerInitAckMsg(self, *header_fields):
        self.syscom.new_message('FaultManagerInitAckMsg', 'Syscom', 'header:msgId:0x800C', *header_fields)
        self.syscom.u32('status')

    def FaultAckMsg(self, *header_fields):
        self.syscom.new_message('FaultAckMsg', 'Syscom', 'header:msgId:0x8018', *header_fields)
        self.syscom.u32('faultId')
        self.syscom.u32('faultState')

    def FaultReqMsg(self, *header_fields):
        self.syscom.new_message('FaultReqMsg', 'Syscom', 'header:msgId:0x802A', *header_fields)
        self.syscom.u32('faultId')
        self.syscom.u32('faultyUnit')
        self.syscom.u32('faultySubUnit')
        self.syscom.u32('faultyCpid')
        self.syscom.u32('faultState')
        self.syscom.u32('faultSeverity')
        self.syscom.u32('objectType')
        self.syscom.u32('detectingUnit')
        self.syscom.u32('detectingSubUnit')
        self.syscom.array('14', 'u32', 'faultInfo')

    def Rp3ConfReqMsg(self, *header_fields):
        self.syscom.new_message('Rp3ConfReqMsg', 'Syscom', 'header:msgId:0x80E3', *header_fields)
        self.syscom.u32('ownNodeAddress')
        self.syscom.u32('tBusLatencyForExtension')
        self.syscom.u32('txTimingAdjustment')
        self.syscom.u32('burstShiftValue')
        self.syscom.array('7', 'SCrossReferenceTable', 'crossReferenceTable')
        self.syscom.u32('dlDelayFactor')
        self.syscom.u32('ulDelayFactor')
        self.syscom.u32('numOfUsedRp3Links')
        self.syscom.array('numOfUsedRp3Links', 'SRp3Link', 'rp3Link')

    def Rp3ConfRespMsg(self, *header_fields):
        self.syscom.new_message('Rp3ConfRespMsg', 'Syscom', 'header:msgId:0x80E4', *header_fields)
        self.syscom.u32('status')

    def Rp3SyncReqMsg(self, *header_fields):
        self.syscom.new_message('Rp3SyncReqMsg', 'Syscom', 'header:msgId:0x80E5', *header_fields)
        self.syscom.u32('txRxIndicator')
        self.syscom.array('6', 'u32', 'linkIndex')

    def Rp3SyncRespMsg(self, *header_fields):
        self.syscom.new_message('Rp3SyncRespMsg', 'Syscom', 'header:msgId:0x80E6', *header_fields)
        self.syscom.u32('txRxIndicator')
        self.syscom.array('6', 'UTxRxSyncStatus', 'txRxlinkStatus')

    def RlcCreateUsersToMacReq(self, *header_fields):
        self.syscom.new_message('RlcCreateUsersToMacReq', 'Syscom', 'header:msgId:0x9A00', *header_fields)
        self.syscom.u32('receiverAddress')
        self.syscom.u32('numOfUsers')
        self.MAC_UserSetupReq('userTemplate')

    def RlcCreateUsersToMacResp(self, *header_fields):
        self.syscom.new_message('RlcCreateUsersToMacResp', 'Syscom', 'header:msgId:0x9A01', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('firstAllocatedCrnti')
        self.syscom.u32('numOfPoolId')
        self.syscom.array('numOfPoolId', 'u32', 'poolId')

    def RlcCreateUsersToTupReq(self, *header_fields):
        self.syscom.new_message('RlcCreateUsersToTupReq', 'Syscom', 'header:msgId:0x9A02', *header_fields)
        self.syscom.u32('numOfUsers')
        self.TUP_UserSetupReq('userTemplate')

    def RlcCreateUsersToTupResp(self, *header_fields):
        self.syscom.new_message('RlcCreateUsersToTupResp', 'Syscom', 'header:msgId:0x9A03', *header_fields)
        self.syscom.u32('status')

    def RlcMassSignallingResp(self, *header_fields):
        self.syscom.new_message('RlcMassSignallingResp', 'Syscom', 'header:msgId:0x9A05', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('firstAllocatedCrnti')

    def RlcRadioBearerSetupToMacUsersReq(self, *header_fields):
        self.syscom.new_message('RlcRadioBearerSetupToMacUsersReq', 'Syscom', 'header:msgId:0x9A06', *header_fields)
        self.syscom.u32('receiverAddress')
        self.syscom.u32('numOfUsers')
        self.MAC_RadioBearerSetupReq('userTemplate')

    def RlcMassTupUserDeletionReq(self, *header_fields):
        self.syscom.new_message('RlcMassTupUserDeletionReq', 'Syscom', 'header:msgId:0x9A07', *header_fields)
        self.syscom.u32('receiverAddress')
        self.TUP_UserDeleteReq('userTemplate')
        self.syscom.u32('useUeLists')
        self.syscom.u32('numOfUsers')
        self.syscom.array('numOfUsers', 'u32', 'ueIdList')

    def RlcConfigureMassSignallingReq(self, *header_fields):
        self.syscom.new_message('RlcConfigureMassSignallingReq', 'Syscom', 'header:msgId:0x9A09', *header_fields)
        self.syscom.u32('maxNumOfUsersInOneBurst')
        self.syscom.u32('delayInMilliSecondsAfterEachBurst')

    def RlcConfigureMassSignallingResp(self, *header_fields):
        self.syscom.new_message('RlcConfigureMassSignallingResp', 'Syscom', 'header:msgId:0x9A0A', *header_fields)
        self.syscom.u32('status')

    def RlcCellUpReq(self, *header_fields):
        self.syscom.new_message('RlcCellUpReq', 'Syscom', 'header:msgId:0x9A0E', *header_fields)
        self.syscom.u32('numOfIterations')
        self.syscom.u32('numOfCellsPerIteration')
        self.syscom.u32('macCellInterface')
        self.syscom.u32('macUserInterface')

    def RlcMassMacUserDeletionReq(self, *header_fields):
        self.syscom.new_message('RlcMassMacUserDeletionReq', 'Syscom', 'header:msgId:0x9A0F', *header_fields)
        self.syscom.u32('receiverAddress')
        self.MAC_UserDeleteReq('userTemplate')
        self.syscom.u32('msgId')
        self.syscom.u32('useUeLists')
        self.syscom.u32('numOfUsers')
        self.syscom.array('numOfUsers', 'u32', 'ueIdList')

    def L2SctCreateDrbsToTupUsersReq(self, *header_fields):
        self.syscom.new_message('L2SctCreateDrbsToTupUsersReq', 'Syscom', 'header:msgId:0x9A10', *header_fields)
        self.syscom.u32('numOfUsers')
        self.syscom.u32('tupAddress')
        self.TUP_BearerSetupReq('bearerTemplate')

    def L2SctCreateDrbsToTupUsersResp(self, *header_fields):
        self.syscom.new_message('L2SctCreateDrbsToTupUsersResp', 'Syscom', 'header:msgId:0x9A11', *header_fields)
        self.syscom.u32('status')

    def RlcFillUpTbMemoryWithPhyPuschRespU(self, *header_fields):
        self.syscom.new_message('RlcFillUpTbMemoryWithPhyPuschRespU', 'Syscom', 'header:msgId:0x9A12', *header_fields)
        self.syscom.u32('numOfUsers')
        self.syscom.u32('numOfDrbs')
        self.syscom.u32('numOfTBsPerBearer')
        self.syscom.u32('startSN')
        self.PHY_PuschReceiveRespU('userTemplate')
        self.syscom.array('8', 'u8', 'data')

    def RlcMassMsg3(self, *header_fields):
        self.syscom.new_message('RlcMassMsg3', 'Syscom', 'header:msgId:0x9A13', *header_fields)
        self.syscom.u32('numOfMsgs')
        self.syscom.u32('numOfCells')
        self.syscom.array('6', 'u32', 'puschReceiveRespUAddress')
        self.syscom.u32('expectedMsgCountPer10ms')
        self.syscom.u32('limitGroups')
        self.syscom.u32('delayBetweenMsgs')
        self.syscom.u32('delayBetweenSequences')
        self.PHY_PuschReceiveRespU('userTemplate')
        self.syscom.array('8', 'u8', 'data')

    def RlcUplinkAmRlcSequenceReq(self, *header_fields):
        self.syscom.new_message('RlcUplinkAmRlcSequenceReq', 'Syscom', 'header:msgId:0x9A14', *header_fields)
        self.syscom.u32('numOfUsers')
        self.syscom.u32('firstCrnti')
        self.syscom.u32('numOfDrbsPerUser')
        self.syscom.u32('firstLcId')
        self.syscom.u32('numSequences')
        self.syscom.array('20', 'RlcPduSequence', 'sequences')
        self.AmRlcSequenceBurstControl('burstControl')
        self.syscom.array('6', 'u32', 'puschReceiveRespUAddress')
        self.syscom.u32('lastUeInCell1')
        self.syscom.u32('framingInfo')

    def L2SctMassSecurityActionReq(self, *header_fields):
        self.syscom.new_message('L2SctMassSecurityActionReq', 'Syscom', 'header:msgId:0x9A15', *header_fields)
        self.Tup_Uesim_header('header')
        self.TUP_SrbSendReq('userTemplate')

    def TupMassSecurityActivationReq(self, *header_fields):
        self.syscom.new_message('TupMassSecurityActivationReq', 'Syscom', 'header:msgId:0x9A16', *header_fields)
        self.Tup_Uesim_header('header')
        self.TUP_SecurityActivationReq('userTemplate')

    def StartLtel2UserCreateDeleteLooping(self, *header_fields):
        self.syscom.new_message('StartLtel2UserCreateDeleteLooping', 'Syscom', 'header:msgId:0x9A17', *header_fields)
        self.syscom.u32('numberOfUsers')
        self.syscom.u32('macUserAddress')
        self.syscom.u32('tupUserAddress')
        self.syscom.u32('macUserDeleteMsgId')
        self.syscom.u32('intervalDelayInMilliseconds')
        self.syscom.u32('intervalDelayInMicroseconds')
        self.syscom.u32('numberOfCells')
        self.MAC_UserSetupReq('macUserTemplate')
        self.TupUserSetupReq_UserCreateDeleteLooping('tupUserSetupTemplate')
        self.MacBearerSetup_UserCreateDeleteLooping('macBearerSetupTemplate')
        self.TupBearerSetupReq_UserCreateDeleteLooping('tupBearerSetupTemplate')
        self.MacUlResourceControlReq_UserCreateDeleteLooping('macUlResourceControlReqTemplate')

    def StopLtel2UserCreateDeleteLooping(self, *header_fields):
        self.syscom.new_message('StopLtel2UserCreateDeleteLooping', 'Syscom', 'header:msgId:0x9A18', *header_fields)
        self.syscom.u32('dummy')

    def MessageSequenceGenericResp(self, *header_fields):
        self.syscom.new_message('MessageSequenceGenericResp', 'Syscom', 'header:msgId:0x9A19', *header_fields)
        self.syscom.u32('status')

    def MessageLoopingStats(self, *header_fields):
        self.syscom.new_message('MessageLoopingStats', 'Syscom', 'header:msgId:0x9A1A', *header_fields)
        self.syscom.u32('numOfLoops')
        self.syscom.u32('loopingDurationInMicroseconds')
        self.syscom.u32('totalNumofProcedures')
        self.Durations('attachProcedureDurations')
        self.Durations('hoProcedureDurations')
        self.Durations('macSetupDurations')
        self.Durations('tupSetupDurations')
        self.Durations('macBearerSetupDurations')
        self.Durations('macUlResourceControlDurations')
        self.Durations('tupBearerSetupDurations')
        self.Durations('macDeleteDurations')
        self.Durations('tupDeleteDurations')

    def L2SctMassDataForwardingReq(self, *header_fields):
        self.syscom.new_message('L2SctMassDataForwardingReq', 'Syscom', 'header:msgId:0x9A1B', *header_fields)
        self.syscom.u32('sutAddress')
        self.syscom.u32('uesimAddress')
        self.syscom.u32('uesim2Address')
        self.syscom.u32('numOfUesim')
        self.syscom.u32('numOfUsers')
        self.TUP_DataForwardSetupReq('userTemplate')

    def L2SctUeindexSet(self, *header_fields):
        self.syscom.new_message('L2SctUeindexSet', 'Syscom', 'header:msgId:0x9A1C', *header_fields)
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')

    def StartHandoverAndDataForwardingLooping(self, *header_fields):
        self.syscom.new_message('StartHandoverAndDataForwardingLooping', 'Syscom', 'header:msgId:0x9A21', *header_fields)
        self.syscom.u32('testTargetDCM')
        self.syscom.u32('handoversPerCellInSecond')
        self.syscom.u32('numberOfUsers')
        self.syscom.u32('numberOfCells')
        self.syscom.u32('macUserAddress')
        self.syscom.u32('tupUserAddress')
        self.syscom.u32('macUserDeleteMsgId')
        self.syscom.u32('intervalDelayInMilliseconds')
        self.syscom.u32('intervalDelayInMicroseconds')
        self.MAC_UserSetupReq('macUserTemplate')
        self.TupUserSetupReq_UserCreateDeleteLooping('tupUserSetupTemplate')
        self.MacBearerSetup_UserCreateDeleteLooping('macBearerSetupTemplate')
        self.TupBearerSetupReq_UserCreateDeleteLooping('tupBearerSetupTemplate')
        self.L2SCT_TupDataForwardSetupReq('tupDataForwardSetupTemplate')

    def StopHandoverAndDataForwardingLooping(self, *header_fields):
        self.syscom.new_message('StopHandoverAndDataForwardingLooping', 'Syscom', 'header:msgId:0x9A22', *header_fields)
        self.syscom.u32('dummy')

    def L2SctTupSrbReceiveIndMsg(self, *header_fields):
        self.syscom.new_message('L2SctTupSrbReceiveIndMsg', 'Syscom', 'header:msgId:0x9A23', *header_fields)
        self.syscom.u32('numOfUsers')
        self.syscom.u32('ueId')
        self.PHY_PuschReceiveRespU('userTemplate')
        self.syscom.array('16', 'u8', 'data')

    def L2SctTupSecurityConfReqMsg(self, *header_fields):
        self.syscom.new_message('L2SctTupSecurityConfReqMsg', 'Syscom', 'header:msgId:0x9A24', *header_fields)
        self.syscom.u32('receiverAddress')
        self.syscom.u32('numOfUsers')
        self.TUP_SecurityConfReq('userTemplate')

    def L2SctCpuLoadMeasConfigReq(self, *header_fields):
        self.syscom.new_message('L2SctCpuLoadMeasConfigReq', 'Syscom', 'header:msgId:0x9A25', *header_fields)
        self.syscom.u32('numOfConfigs')
        self.syscom.array('numOfConfigs', 'SCpuLoadMeasurementConfig', 'configs')

    def L2SctCpuLoadMeasConfigResp(self, *header_fields):
        self.syscom.new_message('L2SctCpuLoadMeasConfigResp', 'Syscom', 'header:msgId:0x9A26', *header_fields)
        self.syscom.u32('status')

    def L2SctCpuLoadMeasReportReq(self, *header_fields):
        self.syscom.new_message('L2SctCpuLoadMeasReportReq', 'Syscom', 'header:msgId:0x9A27', *header_fields)
        self.syscom.u32('sicad')
        self.syscom.u32('getIdleMeasurements')

    def L2SctCpuLoadMeasReportResp(self, *header_fields):
        self.syscom.new_message('L2SctCpuLoadMeasReportResp', 'Syscom', 'header:msgId:0x9A28', *header_fields)
        self.syscom.u32('sicad')
        self.syscom.u32('status')
        self.syscom.u32('moreToSend')
        self.SCpuMeasLoads('cpuloads')
        self.syscom.u16('startMilliseconds')
        self.syscom.u16('lastMeasurementIndex')
        self.syscom.u16('numidleMeasurements')
        self.syscom.array('numidleMeasurements', 'u16', 'idleMeasurements')

    def L2SctCpuLoadMeasCommandInd(self, *header_fields):
        self.syscom.new_message('L2SctCpuLoadMeasCommandInd', 'Syscom', 'header:msgId:0x9A29', *header_fields)
        self.syscom.u32('measGroupId')
        self.syscom.u32('command')

    def SchstubConfigureReq(self, *header_fields):
        self.syscom.new_message('SchstubConfigureReq', 'Syscom', 'header:msgId:0x9BBD', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('startWithSfn')
        self.syscom.array('1', 'u32', 'subFrameToScheduleList')
        self.syscom.u32('tbMode')
        self.syscom.u32('tbMinSize')
        self.syscom.u32('tbMaxSize')
        self.syscom.u32('tbSwitchTimeTTI')
        self.syscom.u32('tbCalculatingMode')
        self.syscom.u32('schedulingMode')
        self.syscom.u32('ulBufStatusIndMode')
        self.syscom.u32('mimoUePercentPerTti')
        self.syscom.u32('numOfScheduledUesPerTti')
        self.syscom.u32('maxHarqReTx')
        self.syscom.u32('maxNumOfUes')
        self.syscom.u32('numOfPools')
        self.syscom.u32('ping')
        self.syscom.u32('forwardPduMuxExceptionIndToRobot')
        self.syscom.u32('uesimInstance')
        self.syscom.u32('sendTicks')
        self.syscom.u32('maxNumUeGroup')
        self.syscom.u32('numOfManuallySetUeGroups')
        self.syscom.array('24', 'u32', 'listOfActiveUeGroups')
        self.SCHSTUB_UeSimInstanceInfo('ueSimInstanceInfo')

    def SchstubConfigureResp(self, *header_fields):
        self.syscom.new_message('SchstubConfigureResp', 'Syscom', 'header:msgId:0x9BBE', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('robotTesterBufferPtr')
        self.syscom.u32('ueIndexAllocationByStub')

    def SchstubSupportCellConfig(self, *header_fields):
        self.syscom.new_message('SchstubSupportCellConfig', 'Syscom', 'header:msgId:0x9BBF', *header_fields)
        self.syscom.u32('routeMessagesToRobot')

    def RlcLteDctStartReportReq(self, *header_fields):
        self.syscom.new_message('RlcLteDctStartReportReq', 'Syscom', 'header:msgId:0x9BCA', *header_fields)
        self.LteDctStartReportReq('request')
        self.syscom.u32('immediateSfnEnabled')
        self.syscom.u32('sfnOffset')
        self.syscom.u32('realReceiver')

    def RlcLteDctStartReportResp(self, *header_fields):
        self.syscom.new_message('RlcLteDctStartReportResp', 'Syscom', 'header:msgId:0x9BCB', *header_fields)
        self.syscom.u32('startSfn')

    def RlcLteBrowserStartReportReq(self, *header_fields):
        self.syscom.new_message('RlcLteBrowserStartReportReq', 'Syscom', 'header:msgId:0x9BCC', *header_fields)
        self.LteBrowserStartReportReq('request')
        self.syscom.u32('immediateSfnEnabled')
        self.syscom.u32('sfnOffset')
        self.syscom.u32('realReceiver')

    def RlcLteBrowserStartReportResp(self, *header_fields):
        self.syscom.new_message('RlcLteBrowserStartReportResp', 'Syscom', 'header:msgId:0x9BCD', *header_fields)
        self.syscom.u32('startSfn')

    def RlcDctOverAllReportReq(self, *header_fields):
        self.syscom.new_message('RlcDctOverAllReportReq', 'Syscom', 'header:msgId:0x9C00', *header_fields)
        self.syscom.u32('dctMeasName')

    def RlcDctUlSchData1OverAllReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlSchData1OverAllReportResp', 'Syscom', 'header:msgId:0x9C01', *header_fields)
        self.syscom.u32('numOfDctUlSchData1CumulativeResults')
        self.syscom.u32('totalAmountOfPadding')
        self.SDctUserInfo('userInfo')
        self.syscom.u32('numOfDctUlSchData1Reports')
        self.syscom.array('5', 'SDctUlschData1', 'dctUlschData1Reports')

    def RlcDctReportReq(self, *header_fields):
        self.syscom.new_message('RlcDctReportReq', 'Syscom', 'header:msgId:0x9C02', *header_fields)
        self.syscom.u32('dummy')

    def RlcDctReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctReportResp', 'Syscom', 'header:msgId:0x9C03', *header_fields)
        self.syscom.array('10', 'SDctMeasurementGroupRespInformation', 'groupIdList')

    def RlcDctInitReq(self, *header_fields):
        self.syscom.new_message('RlcDctInitReq', 'Syscom', 'header:msgId:0x9C04', *header_fields)
        self.syscom.u32('enableSfnCheck')
        self.syscom.u32('measuredCellId')

    def RlcDctMacPduDumpReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctMacPduDumpReportResp', 'Syscom', 'header:msgId:0x9C05', *header_fields)
        self.syscom.array('10', 'SMacPduDumpResults', 'ueList')

    def RlcDctDlSchData1OverAllReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlSchData1OverAllReportResp', 'Syscom', 'header:msgId:0x9C06', *header_fields)
        self.syscom.u32('totNumOfDctDlschData1Results')
        self.syscom.i32('dctDlSchData1CompareResult')
        self.syscom.u32('cumulativeDctG6m24')
        self.syscom.u32('cumulativeDctG6m25')
        self.syscom.array('2', 'SCellSpecificReports', 'cellSpecificAmountOfDctDlschData1Reports')
        self.SDctDlschData1('dctDlschData1')

    def RlcDctUlSch1ReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlSch1ReportResp', 'Syscom', 'header:msgId:0x9C07', *header_fields)
        self.syscom.array('60', 'u32', 'sfn')
        self.syscom.u32('numOfDctUlsch1Reports')
        self.syscom.array('60', 'SDctUlsch1Result', 'dctUlsch1Reports')

    def RlcDctUlSch1TmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlSch1TmReportResp', 'Syscom', 'header:msgId:0x9C08', *header_fields)
        self.syscom.u32('numOfDctUlsch1TmReports')
        self.syscom.array('5', 'SDctUlSch1TmReport', 'dctUlSch1TmReports')

    def RlcDctDlsch1TmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlsch1TmReportResp', 'Syscom', 'header:msgId:0x9C09', *header_fields)
        self.syscom.u32('numOfDlsch1TmReports')
        self.syscom.array('5', 'SDlsch1TmResult', 'dctDlsch1Reports')

    def RlcDctDlschData2TmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlschData2TmReportResp', 'Syscom', 'header:msgId:0x9C0A', *header_fields)
        self.syscom.u32('hasPucchFormat1A')
        self.syscom.u32('numOfDctDlSchData2TmReports')
        self.syscom.array('5', 'SDctDlSchData2TmReport', 'dctDlSchData2Reports')
        self.syscom.u32('hasPucchFormat1B')
        self.syscom.u32('failDetected')

    def RlcDctUlschData1TmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlschData1TmReportResp', 'Syscom', 'header:msgId:0x9C0B', *header_fields)
        self.syscom.u32('numOfDctUlschData1TmReports')
        self.syscom.array('5', 'SDctUlSchData1TmReport', 'dctUlschData1Reports')

    def RlcDctUlLevL1CellTmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlLevL1CellTmReportResp', 'Syscom', 'header:msgId:0x9C0C', *header_fields)
        self.syscom.u32('numOfDctUlLevL1CellTmReport')

    def RlcDctUlschData2TmReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlschData2TmReportResp', 'Syscom', 'header:msgId:0x9C0D', *header_fields)
        self.syscom.u32('numOfDctUlSchData2TmReports')
        self.syscom.array('5', 'SDctUlSchData2TmReport', 'dctUlSchData2Reports')

    def RlcDctUlRlcAmPduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlRlcAmPduReportResp', 'Syscom', 'header:msgId:0x9C0E', *header_fields)
        self.syscom.u32('numOfDctUlRlcAmPduReports')
        self.syscom.array('20', 'SUlRbsAmResult', 'dctUlRlcAmPduReports')

    def RlcDctUlRlcUmPduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlRlcUmPduReportResp', 'Syscom', 'header:msgId:0x9C0F', *header_fields)
        self.syscom.u32('numOfDctUlRlcUmPduReports')
        self.syscom.array('20', 'SUlRbsUmResult', 'dctUlRlcUmPduReports')

    def RlcDctDlRlcAmPduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlRlcAmPduReportResp', 'Syscom', 'header:msgId:0x9C10', *header_fields)
        self.syscom.u32('numOfDctDlRlcAmPduReports')
        self.syscom.array('20', 'SDlRbsAmResult', 'dctDlRlcAmPduReports')

    def RlcDctDlRlcUmPduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlRlcUmPduReportResp', 'Syscom', 'header:msgId:0x9C11', *header_fields)
        self.syscom.u32('numOfDctDlRlcUmPduReports')
        self.syscom.array('20', 'SDlRbsUmResult', 'dctDlRlcUmPduReports')

    def RlcDctDlRlcSduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlRlcSduReportResp', 'Syscom', 'header:msgId:0x9C12', *header_fields)
        self.syscom.u32('numOfDctDlRlcSduReports')
        self.syscom.array('20', 'SDctDlRlcSdu', 'dctDlRlcSduReports')

    def RlcGetDctReportAmountReq(self, *header_fields):
        self.syscom.new_message('RlcGetDctReportAmountReq', 'Syscom', 'header:msgId:0x9C13', *header_fields)
        self.syscom.u32('measType')

    def RlcGetDctReportAmountResp(self, *header_fields):
        self.syscom.new_message('RlcGetDctReportAmountResp', 'Syscom', 'header:msgId:0x9C14', *header_fields)
        self.syscom.u32('measType')
        self.syscom.u32('amount')

    def RlcDctDlPdcpSduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctDlPdcpSduReportResp', 'Syscom', 'header:msgId:0x9C15', *header_fields)
        self.syscom.u32('numOfDctDlPdcpSduReports')
        self.syscom.array('20', 'SDctDlPdcpSduHdbde', 'dctDlPdcpSduReports')

    def RlcDctUlPdcpPduReportResp(self, *header_fields):
        self.syscom.new_message('RlcDctUlPdcpPduReportResp', 'Syscom', 'header:msgId:0x9C16', *header_fields)
        self.syscom.u32('numOfDctUlPdcpPduReports')
        self.syscom.array('20', 'SDctUlPdcpPdu', 'dctUlPdcpPduReports')

    def DctDlPdcpSduHdbdeCombinedReportResp(self, *header_fields):
        self.syscom.new_message('DctDlPdcpSduHdbdeCombinedReportResp', 'Syscom', 'header:msgId:0x9C18', *header_fields)
        self.syscom.u32('totalNumOfDctDlPdcpSduHdbdeResults')
        self.syscom.array('10', 'DctDlPdcpSduHdbdeCombinedReport', 'combinedReports')

    def RlcApiMeasCollectorActivationReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasCollectorActivationReq', 'Syscom', 'header:msgId:0x9C50', *header_fields)
        self.syscom.u32('activate')
        self.syscom.u32('discardZeroValueReports')
        self.syscom.u32('terminateMeasInCellDelete')
        self.syscom.u32('reportIdToBeTerminatedInCellDelete')

    def RlcApiMeasCollectorActivationResp(self, *header_fields):
        self.syscom.new_message('RlcApiMeasCollectorActivationResp', 'Syscom', 'header:msgId:0x9C51', *header_fields)
        self.syscom.u32('dummy')

    def RlcApiMeasAmountReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasAmountReq', 'Syscom', 'header:msgId:0x9C52', *header_fields)
        self.syscom.u32('reportId')

    def RlcApiMeasAmountResp(self, *header_fields):
        self.syscom.new_message('RlcApiMeasAmountResp', 'Syscom', 'header:msgId:0x9C53', *header_fields)
        self.syscom.u32('numOfMeasurementReports')

    def RlcApiMeasReportReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasReportReq', 'Syscom', 'header:msgId:0x9C54', *header_fields)
        self.syscom.u32('reportId')

    def RlcApiMeasInitReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasInitReq', 'Syscom', 'header:msgId:0x9C55', *header_fields)
        self.MAC_MeasInitReq('measInitReq')
        self.syscom.u32('sfnOffset')
        self.syscom.u32('realReceiver')

    def RlcApiMeasInitResp(self, *header_fields):
        self.syscom.new_message('RlcApiMeasInitResp', 'Syscom', 'header:msgId:0x9C56', *header_fields)
        self.syscom.u32('startSfn')

    def RlcApiMeasSduRateReportReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasSduRateReportReq', 'Syscom', 'header:msgId:0x9C57', *header_fields)
        self.syscom.u32('reportId')

    def RlcApiMeasSduRateReportResp(self, *header_fields):
        self.syscom.new_message('RlcApiMeasSduRateReportResp', 'Syscom', 'header:msgId:0x9C58', *header_fields)
        self.syscom.u32('startSfnValidation')
        self.syscom.array('3', 'ApiMacSduCount', 'apiMacSDuCountServingCell')
        self.syscom.array('3', 'ApiMacSduCount', 'apiMacSDuCountSCell')
        self.syscom.array('3', 'ApiMacSduCount', 'apiMacSDuCountUplink')

    def RlcApiMeasManualDataSendReq(self, *header_fields):
        self.syscom.new_message('RlcApiMeasManualDataSendReq', 'Syscom', 'header:msgId:0x9C59', *header_fields)
        self.syscom.u32('l2Address')
        self.syscom.u32('cellId')
        self.syscom.u32('reqType')
        self.syscom.u32('ueIndexData')
        self.syscom.u32('macCeIncluded')
        self.syscom.u32('dataAmount')
        self.syscom.u32('newDataIndicator')

    def SchstubEnterTransparentModeReq(self, *header_fields):
        self.syscom.new_message('SchstubEnterTransparentModeReq', 'Syscom', 'header:msgId:0x9D03', *header_fields)
        self.syscom.u32('dummy')

    def SchstubExitTransparentModeReq(self, *header_fields):
        self.syscom.new_message('SchstubExitTransparentModeReq', 'Syscom', 'header:msgId:0x9D04', *header_fields)
        self.syscom.u32('dummy')

    def SchstubTransparentModeResp(self, *header_fields):
        self.syscom.new_message('SchstubTransparentModeResp', 'Syscom', 'header:msgId:0x9D05', *header_fields)
        self.syscom.u32('ueIndexAllocationByStub')

    def SchstubUeIndexReq(self, *header_fields):
        self.syscom.new_message('SchstubUeIndexReq', 'Syscom', 'header:msgId:0x9D06', *header_fields)
        self.syscom.u32('numOfUeIndex')
        self.syscom.u32('crnti')

    def SchstubUeIndexResp(self, *header_fields):
        self.syscom.new_message('SchstubUeIndexResp', 'Syscom', 'header:msgId:0x9D07', *header_fields)
        self.syscom.u32('crnti')
        self.syscom.u32('ueIndexData')
        self.syscom.u32('numOfUeIndex')
        self.syscom.array('numOfUeIndex', 'u32', 'ueIndex')

    def SchstubAddTempUeReq(self, *header_fields):
        self.syscom.new_message('SchstubAddTempUeReq', 'Syscom', 'header:msgId:0x9D0B', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('padding')

    def SchstubAddTempUeResp(self, *header_fields):
        self.syscom.new_message('SchstubAddTempUeResp', 'Syscom', 'header:msgId:0x9D0C', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u16('padding')

    def SchstubScheduleTtisReq(self, *header_fields):
        self.syscom.new_message('SchstubScheduleTtisReq', 'Syscom', 'header:msgId:0x9D0D', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('tbSizeInBytes')
        self.syscom.u32('schedulingInterval')
        self.syscom.u32('numOfTTIsToSchedule')
        self.syscom.u32('delaySchedulingStart')
        self.syscom.u32('manuallySetFrameAndSubFrame')
        self.syscom.u32('manuallySetUpdateFrameAndSubframe')
        self.syscom.u32('useActualTime')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')

    def SchstubScheduleTtisResp(self, *header_fields):
        self.syscom.new_message('SchstubScheduleTtisResp', 'Syscom', 'header:msgId:0x9D0E', *header_fields)
        self.syscom.u32('status')

    def SchstubOkResp(self, *header_fields):
        self.syscom.new_message('SchstubOkResp', 'Syscom', 'header:msgId:0x9D14', *header_fields)
        self.syscom.u32('nothing')

    def SchstubCcchSchedulingReq(self, *header_fields):
        self.syscom.new_message('SchstubCcchSchedulingReq', 'Syscom', 'header:msgId:0x9D15', *header_fields)
        self.syscom.u32('activate')

    def SchstubMbmsConfigureReq(self, *header_fields):
        self.syscom.new_message('SchstubMbmsConfigureReq', 'Syscom', 'header:msgId:0x9D18', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('mbmsActivated')
        self.syscom.u32('numOfMbmsSessions')
        self.syscom.u32('mbmsPduSize')

    def SchstubMbmsConfigureResp(self, *header_fields):
        self.syscom.new_message('SchstubMbmsConfigureResp', 'Syscom', 'header:msgId:0x9D19', *header_fields)
        self.syscom.u32('status')
        self.syscom.u32('dataCtrlMbmsService')

    def SchstubStatsReq(self, *header_fields):
        self.syscom.new_message('SchstubStatsReq', 'Syscom', 'header:msgId:0x9D1A', *header_fields)
        self.syscom.u32('cellId')

    def SchstubStatsResp(self, *header_fields):
        self.syscom.new_message('SchstubStatsResp', 'Syscom', 'header:msgId:0x9D1B', *header_fields)
        self.syscom.u32('cellId')
        self.TtiStats('ttiStats')
        self.PduMuxMessageStats('pduMuxStats')

    def SchstubInstanceConfigReq(self, *header_fields):
        self.syscom.new_message('SchstubInstanceConfigReq', 'Syscom', 'header:msgId:0x9D1C', *header_fields)
        self.syscom.u32('stubSecondInstanceUsed')

    def SchstubInstanceConfigResp(self, *header_fields):
        self.syscom.new_message('SchstubInstanceConfigResp', 'Syscom', 'header:msgId:0x9D1D', *header_fields)
        self.syscom.u32('status')

    def SchstubUeConfigReq(self, *header_fields):
        self.syscom.new_message('SchstubUeConfigReq', 'Syscom', 'header:msgId:0x9D1E', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u32('ueIndex')
        self.syscom.u32('ulBsrMode')
        self.syscom.u32('ulBsrIndex')
        self.syscom.u32('ulBsrLcgId')

    def SchstubUeConfigResp(self, *header_fields):
        self.syscom.new_message('SchstubUeConfigResp', 'Syscom', 'header:msgId:0x9D1F', *header_fields)
        self.syscom.u32('cellId')
        self.syscom.u16('ueIndex')
        self.syscom.u32('status')

    def SchstubDispatcherConfigReq(self, *header_fields):
        self.syscom.new_message('SchstubDispatcherConfigReq', 'Syscom', 'header:msgId:0x9D21', *header_fields)
        self.syscom.u32('numOfInstances')
        self.syscom.u32('dlBufStatusHandleType')
        self.syscom.array('3', 'SSchStubInstanceConfig', 'instanceConfigs')

    def SchstubDispatcherConfigResp(self, *header_fields):
        self.syscom.new_message('SchstubDispatcherConfigResp', 'Syscom', 'header:msgId:0x9D22', *header_fields)
        self.syscom.u32('status')

    def SchstubResetReq(self, *header_fields):
        self.syscom.new_message('SchstubResetReq', 'Syscom', 'header:msgId:0x9D23', *header_fields)
        self.syscom.u32('dummy')

    def SchstubResetResp(self, *header_fields):
        self.syscom.new_message('SchstubResetResp', 'Syscom', 'header:msgId:0x9D24', *header_fields)
        self.syscom.u32('dummy')

    def MgmtCpuLoadMeasurementReq(self, *header_fields):
        self.syscom.new_message('MgmtCpuLoadMeasurementReq', 'Syscom', 'header:msgId:0xABBA', *header_fields)
        self.syscom.u8('reset')
        self.syscom.u8('getIdleMeasurements')
        self.syscom.u8('recordIdleMeasurementsForIntervalOnly')
        self.syscom.u8('padding')
        self.syscom.u16('startDelayMs')
        self.syscom.u16('intervalMs')

    def MgmtCpuLoadMeasurementResp(self, *header_fields):
        self.syscom.new_message('MgmtCpuLoadMeasurementResp', 'Syscom', 'header:msgId:0xABBB', *header_fields)
        self.SCpuLoads('cpuloads')
        self.syscom.u16('startMilliseconds')
        self.syscom.u16('lastMeasurementIndex')
        self.syscom.u16('numidleMeasurements')
        self.syscom.array('numidleMeasurements', 'u16', 'idleMeasurements')

    def MgmtIntervalCpuLoadMeasurementReq(self, *header_fields):
        self.syscom.new_message('MgmtIntervalCpuLoadMeasurementReq', 'Syscom', 'header:msgId:0xABBC', *header_fields)
        self.syscom.u32('interval')

    def AmRlcSequenceBurstControl(self, name):
        self.syscom.new_struct('AmRlcSequenceBurstControl', name)
        self.syscom.u32('numOfPuschMessagesInBurst')
        self.syscom.u32('delayAfterBurst')
        self.syscom.end_struct()

    def ApiMacSduCount(self, name):
        self.syscom.new_struct('ApiMacSduCount', name)
        self.syscom.u32('cellId')
        self.syscom.u32('reportId')
        self.syscom.array('16', 'u32', 'macSduCountSum')
        self.syscom.array('16', 'u32', 'ttiBitUpAmount')
        self.syscom.end_struct()

    def DctDlPdcpSduHdbdeCombinedReport(self, name):
        self.syscom.new_struct('DctDlPdcpSduHdbdeCombinedReport', name)
        self.syscom.u32('ueId')
        self.syscom.u32('cumulativeDctG11M1')
        self.syscom.u32('cumulativeDctG11M2')
        self.syscom.u32('cumulativeDctG11M3')
        self.syscom.u32('cumulativeDctG11M4')
        self.syscom.u32('cumulativeDctG11M5')
        self.syscom.u32('cumulativeDctG11M6')
        self.syscom.u32('cumulativeDctG11M7')
        self.syscom.u32('maxDctG11M9')
        self.syscom.u32('maxDctG11M10')
        self.syscom.u32('maxDctG11M11')
        self.syscom.end_struct()

    def Durations(self, name):
        self.syscom.new_struct('Durations', name)
        self.syscom.u32('longest')
        self.syscom.u32('shortest')
        self.syscom.u32('latest')
        self.syscom.end_struct()

    def TproxyBearerSetupReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerSetupReqMsg', 'Syscom', 'header:msgId:0xEE10', *header_fields)
        self.syscom.u32('transactionId')
        self.syscom.u32('bearerGroupId')
        self.SProtocolStackProfile('protoStackProfile')
        self.syscom.u32('useInternalDataGenerator')
        self.syscom.u32('numOfBearerList')
        self.syscom.array('numOfBearerList', 'SBearerInfo', 'bearerList')

    def TproxyBearerSetupRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerSetupRespMsg', 'Syscom', 'header:msgId:0xEE11', *header_fields)
        self.syscom.u32('transactionId')
        self.SMessageResult('messageResult')
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('dlPortGenToTproxy')
        self.syscom.u32('dlPortTproxyToGen')
        self.syscom.u32('ulPortGenToTproxy')
        self.syscom.u32('ulPortTproxyToGen')

    def TproxyBearerDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerDeleteReqMsg', 'Syscom', 'header:msgId:0xEE12', *header_fields)
        self.syscom.u32('transactionId')
        self.syscom.u32('bearerGroupId')

    def TproxyBearerDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerDeleteRespMsg', 'Syscom', 'header:msgId:0xEE13', *header_fields)
        self.syscom.u32('transactionId')
        self.SMessageResult('messageResult')

    def TproxyStartupReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyStartupReqMsg', 'Syscom', 'header:msgId:0xEE16', *header_fields)
        self.syscom.u16('SutCpid')
        self.syscom.u32('numOfRoutList')
        self.syscom.array('1', 'SRouteDef', 'routeList')

    def TproxyStartupRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyStartupRespMsg', 'Syscom', 'header:msgId:0xEE17', *header_fields)
        self.SMessageResult('messageResult')
        self.syscom.u32('ulGtpQueue')

    def TproxyBearerStatsReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerStatsReqMsg', 'Syscom', 'header:msgId:0xEE18', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('resetStats')

    def TproxyBearerStatsRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerStatsRespMsg', 'Syscom', 'header:msgId:0xEE19', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('padding_for_u64')
        self.SBearerGroupStats('groupStats')

    def TproxyStartGeneratingDataReq(self, *header_fields):
        self.syscom.new_message('TproxyStartGeneratingDataReq', 'Syscom', 'header:msgId:0xEE1B', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.SPacketSendingMode('packetSendingMode')
        self.syscom.u32('packetsPerSecond')
        self.syscom.u32('packetSize')
        self.syscom.u32('direction')
        self.syscom.u32('verifyGtpuPayload')
        self.syscom.u32('ping')
        self.syscom.u32('firstSn')
        self.syscom.array('32', 'u8', 'data')

    def TproxyStartGeneratingDataResp(self, *header_fields):
        self.syscom.new_message('TproxyStartGeneratingDataResp', 'Syscom', 'header:msgId:0xEE1C', *header_fields)
        self.syscom.u32('bearerGroupId')

    def TproxyStopGeneratingDataReq(self, *header_fields):
        self.syscom.new_message('TproxyStopGeneratingDataReq', 'Syscom', 'header:msgId:0xEE1D', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('direction')

    def TproxyStopGeneratingDataResp(self, *header_fields):
        self.syscom.new_message('TproxyStopGeneratingDataResp', 'Syscom', 'header:msgId:0xEE1E', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('direction')
        self.syscom.u32('status')

    def TproxyBearerGroupDeleteReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerGroupDeleteReqMsg', 'Syscom', 'header:msgId:0xEE21', *header_fields)
        self.syscom.u32('groupId')

    def TproxyBearerGroupDeleteRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyBearerGroupDeleteRespMsg', 'Syscom', 'header:msgId:0xEE22', *header_fields)
        self.syscom.u32('groupId')
        self.syscom.u32('status')

    def TproxyStartDataBurstReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyStartDataBurstReqMsg', 'Syscom', 'header:msgId:0xEE23', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('packetsPerSecond')
        self.syscom.u32('packetSize')
        self.syscom.u32('direction')
        self.syscom.u32('startDealy')
        self.syscom.u32('duration')
        self.syscom.u32('iteration')

    def TproxyStartDataBurstRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyStartDataBurstRespMsg', 'Syscom', 'header:msgId:0xEE24', *header_fields)
        self.SMessageResult('messageResult')

    def TproxyStopDataBurstReqMsg(self, *header_fields):
        self.syscom.new_message('TproxyStopDataBurstReqMsg', 'Syscom', 'header:msgId:0xEE25', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('packetsPerSecond')
        self.syscom.u32('packetSize')
        self.syscom.u32('direction')
        self.syscom.u32('startDealy')
        self.syscom.u32('duration')
        self.syscom.u32('iteration')

    def ExecuteDelayedDataBurstInd(self, *header_fields):
        self.syscom.new_message('ExecuteDelayedDataBurstInd', 'Syscom', 'header:msgId:0xEE26', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('packetsPerSecond')
        self.syscom.u32('packetSize')
        self.syscom.u32('direction')
        self.syscom.u32('startDealy')
        self.syscom.u32('duration')
        self.syscom.u32('iteration')

    def TproxyStopDataBurstRespMsg(self, *header_fields):
        self.syscom.new_message('TproxyStopDataBurstRespMsg', 'Syscom', 'header:msgId:0xEE27', *header_fields)
        self.syscom.u32('bearerGroupId')
        self.syscom.u32('direction')

    def TproxyExecutePendingGroupsMsg(self, *header_fields):
        self.syscom.new_message('TproxyExecutePendingGroupsMsg', 'Syscom', 'header:msgId:0xEE28', *header_fields)
        self.syscom.u32('delayForExecution')
        self.syscom.u32('start_activity')
        self.syscom.u32('target_activity')
        self.syscom.u32('activity_stepping')
        self.syscom.u32('activity_increase_perioid')

    def FaultHistoryReq(self, *header_fields):
        self.syscom.new_message('FaultHistoryReq', 'Syscom', 'header:msgId:0xF032', *header_fields)
        self.syscom.u32('resetHistory')

    def FaultHistoryAck(self, *header_fields):
        self.syscom.new_message('FaultHistoryAck', 'Syscom', 'header:msgId:0xF033', *header_fields)
        self.syscom.u32('faultAmount')
        self.syscom.u32('totalFaultAmount')
        self.syscom.array('10', 'FaultInd', 'faultHistory')

    def L1AntennaMappingReqMsg(self, *header_fields):
        self.syscom.new_message('L1AntennaMappingReqMsg', 'Syscom', 'header:msgId:0xF068', *header_fields)
        self.syscom.array('6', 'u32', 'txLinkBufferPtr')
        self.syscom.array('6', 'u32', 'rxLinkBufferPtr')
        self.syscom.u32('transmissionBandwidth')
        self.syscom.u32('typeOfAntennaBus')
        self.syscom.u32('timingOffsetLink')
        self.syscom.u32('linkDirection')
        self.syscom.u32('numberOfLocalCells')
        self.syscom.array('numberOfLocalCells', 'SLocalCellResMapToAntennaBus', 'localCellResMapToBus')

    def L1AntennaMappingRespMsg(self, *header_fields):
        self.syscom.new_message('L1AntennaMappingRespMsg', 'Syscom', 'header:msgId:0xF069', *header_fields)
        self.syscom.u32('status')

    def DctMeasStreamerEnableReqMsg(self, *header_fields):
        self.syscom.new_message('DctMeasStreamerEnableReqMsg', 'Syscom', 'header:msgId:0xFACC', *header_fields)
        self.syscom.array('8', 'u8', 'destMacAddr')
        self.syscom.array('4', 'u8', 'destIpAddr')
        self.syscom.u16('destUdpPort')
        self.syscom.u16('destHwPort')

    def DctMeasStreamerEnableRespMsg(self, *header_fields):
        self.syscom.new_message('DctMeasStreamerEnableRespMsg', 'Syscom', 'header:msgId:0xFACD', *header_fields)
        self.syscom.u32('response')

    def FaultInd(self, name):
        self.syscom.new_struct('FaultInd', name)
        self.syscom.u32('faultId')
        self.syscom.u32('faultState')
        self.SMessageAddress('faultSource')
        self.syscom.array('14', 'u32', 'faultInfo')
        self.syscom.end_struct()

    def L2SCT_TupDataForwardSetupReq(self, name):
        self.syscom.new_struct('L2SCT_TupDataForwardSetupReq', name)
        self.syscom.u32('sutAddress')
        self.syscom.u32('uesimAddress')
        self.syscom.u32('uesim2Address')
        self.syscom.u32('numOfUesim')
        self.syscom.u32('numOfUsers')
        self.TUP_DataForwardSetupReq('userTemplate')
        self.syscom.end_struct()

    def LteBrowserStartReportReq(self, name):
        self.syscom.new_struct('LteBrowserStartReportReq', name)
        self.SBrowserRequestor('requestor')
        self.syscom.u32('reportName')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('itemCollectCount')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('reportingDuration')
        self.syscom.u32('objectHandler')
        self.syscom.u32('paramsTableSize')
        self.syscom.array('1', 'u32', 'dynamicData')
        self.syscom.end_struct()

    def LteDctStartReportReq(self, name):
        self.syscom.new_struct('LteDctStartReportReq', name)
        self.syscom.u32('reportReceiver')
        self.syscom.u32('reportName')
        self.SBrowserObjectPath('objectPath')
        self.syscom.u32('contextId')
        self.syscom.u32('procedureId')
        self.syscom.u32('sessionId')
        self.syscom.u32('itemCollectCount')
        self.syscom.u32('reportPeriod')
        self.syscom.u32('reportingDuration')
        self.syscom.u32('numOfParams')
        self.syscom.array('numOfParams', 'u32', 'params')
        self.syscom.end_struct()

    def MAC_BundledContentionResInd(self, name):
        self.syscom.new_struct('MAC_BundledContentionResInd', name)
        self.syscom.u32('numberOfContResMsg')
        self.syscom.u32('paddingNumberOfContResMsg')
        self.syscom.array('16', 'SContentionResInd', 'pduMuxContentionResInd')
        self.syscom.end_struct()

    def MAC_CcchDataReceiveInd(self, name):
        self.syscom.new_struct('MAC_CcchDataReceiveInd', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('maxNumOfUes')
        self.syscom.array('1', 'SMsg3Info', 'msg3Info')
        self.syscom.end_struct()

    def MAC_MeasInitReq(self, name):
        self.syscom.new_struct('MAC_MeasInitReq', name)
        self.syscom.u32('reportClientSicad')
        self.syscom.u32('cellId')
        self.syscom.u32('startSfn')
        self.syscom.u32('reportId')
        self.syscom.u32('period')
        self.syscom.u32('samplingPeriod')
        self.syscom.u32('groupCount')
        self.syscom.array('groupCount', 'u32', 'groupList')
        self.syscom.end_struct()

    def MAC_RadioBearerSetupReq(self, name):
        self.syscom.new_struct('MAC_RadioBearerSetupReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('hasUeSetupParams')
        self.SUeSetupParams('ueSetupParams')
        self.syscom.u32('hasContainer')
        self.UWmpDcmUserContainer('container')
        self.syscom.u32('hasCqiParams')
        self.SCqiParams('cqiParams')
        self.syscom.u32('hasUeParams')
        self.SUeParams('ueParams')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numSRbs')
        self.syscom.array('1', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numDRbs')
        self.syscom.array('numDRbs', 'SRbInfo', 'drbInfoList')
        self.syscom.end_struct()

    def MAC_UserDeleteReq(self, name):
        self.syscom.new_struct('MAC_UserDeleteReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('validUeId')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('spsCrntiReleaseReq')
        self.syscom.u32('numOfAbnormallyReleasedDRbList')
        self.syscom.array('8', 'u32', 'abnormallyReleasedDRbList')
        self.syscom.u32('hasUeReleaseCause')
        self.syscom.u32('ueReleaseCause')
        self.syscom.u32('hasSpecificUeReleaseCause')
        self.syscom.u32('specificUeReleaseCause')
        self.syscom.end_struct()

    def MAC_UserSetupReq(self, name):
        self.syscom.new_struct('MAC_UserSetupReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('ueGroup')
        self.syscom.u32('poolIdData')
        self.syscom.u32('transactionId')
        self.syscom.u32('numOfScellIds')
        self.syscom.array('2', 'u32', 'lnCelIdSCell')
        self.syscom.u32('spsCrntiAllocationReq')
        self.syscom.u32('handoverType')
        self.SUeSetupParams('ueSetupParams')
        self.UWmpDcmUserContainer('container')
        self.SCqiParams('cqiParams')
        self.SPuschControlOffsets('controlOffsets')
        self.SUeParams('ueParams')
        self.syscom.u32('ttiBundlingEnable')
        self.syscom.u32('multiClusterInUlSupported')
        self.syscom.u32('intraCellInterDataPoolEnabled')
        self.syscom.u32('hasTpcPdcchConfigParams')
        self.STpcPdcchConfigParams('tpcPdcchConfigParams')
        self.syscom.u32('hasUlPCUeParams')
        self.SUlPCUeParams('ulPCUeParams')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.u32('numSRbs')
        self.syscom.array('2', 'SSrbInfo', 'sRbInfoList')
        self.syscom.u32('numRbs')
        self.syscom.array('numRbs', 'SRbInfo', 'rbInfoList')
        self.syscom.end_struct()

    def MacBearerSetup_UserCreateDeleteLooping(self, name):
        self.syscom.new_struct('MacBearerSetup_UserCreateDeleteLooping', name)
        self.SRbInfo('drbInfo')
        self.syscom.end_struct()

    def MacUlResourceControlReq_UserCreateDeleteLooping(self, name):
        self.syscom.new_struct('MacUlResourceControlReq_UserCreateDeleteLooping', name)
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.end_struct()

    def PHYSTUB_CellData(self, name):
        self.syscom.new_struct('PHYSTUB_CellData', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crcFailMode')
        self.syscom.u32('crcNackAmount')
        self.syscom.u32('crcNackUserAmount')
        self.syscom.end_struct()

    def PHYSTUB_sequencerStats(self, name):
        self.syscom.new_struct('PHYSTUB_sequencerStats', name)
        self.syscom.u32('detectedCounter')
        self.syscom.u32('correctTACommands')
        self.syscom.u32('missedCounter')
        self.syscom.u32('falseCounter')
        self.syscom.u32('idlePeriodCounter')
        self.syscom.u32('crcOks')
        self.syscom.u32('crcNoks')
        self.syscom.u32('crcTransmissionUnreliable')
        self.SUlCtrlChannelMeasCountersMissedPrach('prachCounters')
        self.syscom.u32('total')
        self.syscom.end_struct()

    def PHY_PuschReceiveRespU(self, name):
        self.syscom.new_struct('PHY_PuschReceiveRespU', name)
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u16('lastMsgInTti')
        self.syscom.u16('numOfRespUsInTti')
        self.syscom.u32('numOfUePuschResp')
        self.syscom.array('numOfUePuschResp', 'SPuschUeResp', 'uePuschResp')
        self.syscom.end_struct()

    def PduMuxMessageStats(self, name):
        self.syscom.new_struct('PduMuxMessageStats', name)
        self.syscom.u32('schedulingGrantsOnPrimaryCell')
        self.syscom.u32('schedulingGrantsOnSecondaryCell')
        self.syscom.u32('totalTbSizeOnPrimaryCell')
        self.syscom.u32('totalTbSizeOnSecondaryCell')
        self.syscom.end_struct()

    def RlcPduSequence(self, name):
        self.syscom.new_struct('RlcPduSequence', name)
        self.syscom.u32('startSN')
        self.syscom.u32('numOfPdus')
        self.syscom.u32('numOfAmdPduSegmentsPerSN')
        self.syscom.u32('dataBytesPerSegment')
        self.syscom.u32('endFI')
        self.syscom.end_struct()

    def SAaConfigRadParams(self, name):
        self.syscom.new_struct('SAaConfigRadParams', name)
        self.syscom.u32('index')
        self.syscom.u32('size')
        self.syscom.u32('value')
        self.syscom.end_struct()

    def SAaMemDspPoolStatus(self, name):
        self.syscom.new_struct('SAaMemDspPoolStatus', name)
        self.syscom.u32('type')
        self.syscom.u32('index')
        self.syscom.u32('address')
        self.syscom.u32('sizeInBytes')
        self.syscom.u32('maxUsedInBytes')
        self.syscom.u32('unUsedInBytes')
        self.syscom.u32('releasedInBytes')
        self.syscom.u32('maxAllocSize')
        self.syscom.end_struct()

    def SAaSysComGwIpAddress(self, name):
        self.syscom.new_struct('SAaSysComGwIpAddress', name)
        self.syscom.chars('16', 'address')
        self.syscom.u32('port')
        self.syscom.end_struct()

    def SAaSysLogCtrlParams(self, name):
        self.syscom.new_struct('SAaSysLogCtrlParams', name)
        self.syscom.u32('inputLevel')
        self.syscom.u32('outputLevel')
        self.syscom.u32('outputMode')
        self.syscom.array('4', 'u8', 'targetIpAddr')
        self.syscom.u32('targetPortNumber')
        self.syscom.u32('targetSicAddress')
        self.syscom.end_struct()

    def SAaTime(self, name):
        self.syscom.new_struct('SAaTime', name)
        self.syscom.u32('year')
        self.syscom.u32('month')
        self.syscom.u32('day')
        self.syscom.u32('hour')
        self.syscom.u32('minute')
        self.syscom.u32('second')
        self.syscom.u32('millisec')
        self.syscom.end_struct()

    def SAaTraceMonCtrlParams(self, name):
        self.syscom.new_struct('SAaTraceMonCtrlParams', name)
        self.syscom.u32('mode')
        self.syscom.u32('type')
        self.SAaTraceMsgIdFilter('sAaTraceMsgIdFilter')
        self.SAaTraceMsgIdHeavyLoadFilter('sAaTraceMsgIdHeavyLoadFilter')
        self.SMessageAddress('routingTarget')
        self.syscom.u32('ifFormat')
        self.syscom.end_struct()

    def SAaTraceMsgIdFilter(self, name):
        self.syscom.new_struct('SAaTraceMsgIdFilter', name)
        self.syscom.array('128', 'u32', 'msgId')
        self.syscom.array('64', 'u8', 'msgIdRange')
        self.syscom.end_struct()

    def SAaTraceMsgIdHeavyLoadFilter(self, name):
        self.syscom.new_struct('SAaTraceMsgIdHeavyLoadFilter', name)
        self.syscom.array('8', 'u32', 'msgId2')
        self.syscom.array('8', 'u32', 'extraFilter')
        self.syscom.end_struct()

    def SAddressInfo(self, name):
        self.syscom.new_struct('SAddressInfo', name)
        self.syscom.u32('addressName')
        self.syscom.u32('address')
        self.syscom.end_struct()

    def SAmbrParams(self, name):
        self.syscom.new_struct('SAmbrParams', name)
        self.syscom.array('2', 'u32', 'ambrUl')
        self.syscom.array('2', 'u32', 'ambrDl')
        self.syscom.end_struct()

    def SAntennaBusParametersForRfBus(self, name):
        self.syscom.new_struct('SAntennaBusParametersForRfBus', name)
        self.syscom.u32('busIndex')
        self.syscom.u32('antennaIndex')
        self.syscom.end_struct()

    def SAntennaBusParametersForRp3(self, name):
        self.syscom.new_struct('SAntennaBusParametersForRp3', name)
        self.syscom.u32('antennaNodeAddress')
        self.syscom.u32('virtualAntennaNodeAddress')
        self.syscom.u32('linkIndex')
        self.syscom.u32('carrierIndex')
        self.syscom.u32('virtualAntennaMapping')
        self.syscom.u32('measurementMessageNodeAddress')
        self.syscom.u32('measurementIndex')
        self.syscom.end_struct()

    def SAperiodicCqiParamsDcm(self, name):
        self.syscom.new_struct('SAperiodicCqiParamsDcm', name)
        self.syscom.u32('aperiodicCqiTimer')
        self.syscom.u32('aperiodicCqiLifetime')
        self.syscom.array('16', 'u32', 'aperiodicCqiUsageTable')
        self.syscom.array('4', 'u32', 'aperiodicCqiNotTriggeredTimer')
        self.syscom.array('3', 'u16', 'numOfUELimit')
        self.syscom.u16('minTotalDLBufferSize')
        self.syscom.end_struct()

    def SAperiodicCsiTriggerParams(self, name):
        self.syscom.new_struct('SAperiodicCsiTriggerParams', name)
        self.syscom.u8('aperiodicCsiTrigger1')
        self.syscom.u8('aperiodicCsiTrigger2')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SArrayOfOaMUlsPuschMask(self, name):
        self.syscom.new_struct('SArrayOfOaMUlsPuschMask', name)
        self.syscom.u32('hasUlsPuschMask')
        self.syscom.u32('numOfUlsPuschMask')
        self.syscom.array('2', 'SOaMUlsPuschMask', 'ulsPuschMask')
        self.syscom.end_struct()

    def SAssuredPucchInfoDl(self, name):
        self.syscom.new_struct('SAssuredPucchInfoDl', name)
        self.syscom.u16('thTimeCqiRiDropForDcmAlgorithmDl')
        self.syscom.u16('thTimeCqiRiDropForHst1Dl')
        self.syscom.u16('thTimeCqiRiDropForHst3Dl')
        self.syscom.u16('padding')
        self.syscom.u32('thTimeCqiRiDropForDcmAlgorithmDlSCell')
        self.syscom.u32('thTimeCqiRiDropForHst1DlSCell')
        self.syscom.u32('thTimeCqiRiDropForHst3DlSCell')
        self.syscom.end_struct()

    def SAssuredPucchInfoUl(self, name):
        self.syscom.new_struct('SAssuredPucchInfoUl', name)
        self.syscom.u16('thTimeCqiRiDropForDcmAlgorithmUl')
        self.syscom.u16('thTimeCqiRiDropForHst1Ul')
        self.syscom.u16('thTimeCqiRiDropForHst3Ul')
        self.syscom.u16('padding')
        self.syscom.u32('thTimeCqiRiDropForDcmAlgorithmUlSCell')
        self.syscom.u32('thTimeCqiRiDropForHst1UlSCell')
        self.syscom.u32('thTimeCqiRiDropForHst3UlSCell')
        self.syscom.end_struct()

    def SBackoffIndicatorInfoDcm(self, name):
        self.syscom.new_struct('SBackoffIndicatorInfoDcm', name)
        self.syscom.u16('thNumUp')
        self.syscom.u16('thNumDown')
        self.syscom.u16('thCntUp')
        self.syscom.u16('thCntDown')
        self.syscom.end_struct()

    def SBbmodSfp(self, name):
        self.syscom.new_struct('SBbmodSfp', name)
        self.syscom.u16('bbmod')
        self.syscom.u16('sfp')
        self.syscom.end_struct()

    def SBeamformingCtrlParams(self, name):
        self.syscom.new_struct('SBeamformingCtrlParams', name)
        self.syscom.u32('sectorBeamformingMode')
        self.syscom.array('4', 'SSectorBfWeightforAntenna', 'sectorBfWeightforAntenna')
        self.syscom.u32('bfCqiThUp')
        self.syscom.u32('bfCqiThDown')
        self.syscom.u32('bfRankThUp')
        self.syscom.u32('bfRankThDown')
        self.syscom.u32('timeChInfoValid')
        self.syscom.u32('actBfFallback')
        self.syscom.u32('mimoBfdlCqiComp')
        self.syscom.u32('mimoBfCqiAvg')
        self.syscom.u32('mimoBfdlRiAvg')
        self.syscom.u32('deploymentInformation')
        self.syscom.u32('mimoBfslCqiThU')
        self.syscom.u32('mimoBfslCqiThD')
        self.syscom.u32('sectorBeamAggrGain')
        self.syscom.end_struct()

    def SBearerGroupPacketStats(self, name):
        self.syscom.new_struct('SBearerGroupPacketStats', name)
        self.syscom.u64('bytesSent')
        self.syscom.u64('bytesReceived')
        self.syscom.u64('bytesReceivedFromForwarding')
        self.syscom.u32('packageCount')
        self.syscom.u32('packetsSent')
        self.syscom.u32('sendingPeriod')
        self.syscom.u32('receivingPeriod')
        self.syscom.u32('payloadFailures')
        self.syscom.u32('packetsReceivedFromForwarding')
        self.syscom.u32('endMarkersReceived')
        self.syscom.u32('avgDealayInMicrosecs')
        self.syscom.u32('maxDelayInMicroSecs')
        self.syscom.u32('minDelayInMicroSecs')
        self.syscom.end_struct()

    def SBearerGroupStats(self, name):
        self.syscom.new_struct('SBearerGroupStats', name)
        self.SBearerGroupPacketStats('dlPackets')
        self.SBearerGroupPacketStats('ulPackets')
        self.syscom.end_struct()

    def SBearerIds(self, name):
        self.syscom.new_struct('SBearerIds', name)
        self.syscom.u8('drbId')
        self.syscom.u8('lcgId')
        self.syscom.u16('rcvdData')
        self.syscom.end_struct()

    def SBearerInfo(self, name):
        self.syscom.new_struct('SBearerInfo', name)
        self.syscom.u32('sgwTeid')
        self.syscom.u32('enbTeid')
        self.syscom.u32('ueId')
        self.syscom.u32('drbId')
        self.syscom.u32('sutDspIpOrSicad')
        self.syscom.array('2', 'u32', 'uesimDspIpOrSicad')
        self.syscom.u32('e')
        self.syscom.end_struct()

    def SBearerList(self, name):
        self.syscom.new_struct('SBearerList', name)
        self.syscom.u32('drbId')
        self.syscom.u32('packetId')
        self.syscom.end_struct()

    def SBitRateParams(self, name):
        self.syscom.new_struct('SBitRateParams', name)
        self.syscom.u32('minBitrateUl')
        self.syscom.u32('minBitrateDl')
        self.syscom.u32('hasMaxBitrateUl')
        self.syscom.u32('maxBitrateUl')
        self.syscom.u32('hasMaxBitrateDl')
        self.syscom.u32('maxBitrateDl')
        self.syscom.end_struct()

    def SBrowserObject(self, name):
        self.syscom.new_struct('SBrowserObject', name)
        self.syscom.u32('name')
        self.syscom.u32('id')
        self.syscom.u32('index')
        self.syscom.end_struct()

    def SBrowserObjectData(self, name):
        self.syscom.new_struct('SBrowserObjectData', name)
        self.syscom.u32('discriminator')
        self.UInnerSBrowserObjectData('u')
        self.syscom.end_struct()

    def SBrowserObjectPath(self, name):
        self.syscom.new_struct('SBrowserObjectPath', name)
        self.syscom.u32('hasParent')
        self.SBrowserObject('parent')
        self.SBrowserObject('object')
        self.syscom.end_struct()

    def SBrowserRequestor(self, name):
        self.syscom.new_struct('SBrowserRequestor', name)
        self.syscom.u8('board')
        self.syscom.u8('cpu')
        self.syscom.u16('task')
        self.syscom.end_struct()

    def SBufferDiscardParams(self, name):
        self.syscom.new_struct('SBufferDiscardParams', name)
        self.syscom.u32('thOverflowDiscard')
        self.syscom.u32('flagOverflowDiscard')
        self.syscom.u32('discBuffThrAct')
        self.syscom.u32('discBuffHighThr')
        self.syscom.end_struct()

    def SCCAddresses(self, name):
        self.syscom.new_struct('SCCAddresses', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('respDAddress')
        self.syscom.u32('cqiRespDAddress')
        self.syscom.end_struct()

    def SCHSTUB_UeSimInstanceInfo(self, name):
        self.syscom.new_struct('SCHSTUB_UeSimInstanceInfo', name)
        self.syscom.u32('uesimInstance')
        self.syscom.array('3', 'u32', 'phyStubInstances')
        self.syscom.end_struct()

    def SCaCeInfo(self, name):
        self.syscom.new_struct('SCaCeInfo', name)
        self.syscom.u8('caCeAvail')
        self.syscom.u8('caCeValue')
        self.syscom.u16('unused')
        self.syscom.end_struct()

    def SCaCqiParams(self, name):
        self.syscom.new_struct('SCaCqiParams', name)
        self.SCqiParams('cqiParams')
        self.SCqiParamsWmp('cqiParamsWmp')
        self.syscom.end_struct()

    def SCaDcmSCellContainer(self, name):
        self.syscom.new_struct('SCaDcmSCellContainer', name)
        self.syscom.u32('sCellDeactivationTimer')
        self.syscom.u32('sCellDeactivationTimerEnb')
        self.syscom.u16('sCellAddKeepFlag')
        self.syscom.u16('sCellAddKeepFlagOriginal')
        self.syscom.u16('sCellInitialActiveDeactiveStatus')
        self.syscom.u16('thSCellRemove')
        self.syscom.u16('lcpForCqiOffsetAdjSCell')
        self.syscom.u16('padding')
        self.syscom.u32('initialSCellInactivityTimerR')
        self.syscom.end_struct()

    def SCaRbInfo(self, name):
        self.syscom.new_struct('SCaRbInfo', name)
        self.syscom.u32('drbId')
        self.SRlcAmParameters('rlcAmParameters')
        self.syscom.end_struct()

    def SCaSplitRbData(self, name):
        self.syscom.new_struct('SCaSplitRbData', name)
        self.syscom.u16('ueIndexDataSCell')
        self.syscom.u16('ueIndexDataPCell')
        self.syscom.u16('nonGbrDataSplit')
        self.syscom.u16('maxTransferRatePerTti')
        self.syscom.end_struct()

    def SCaWmpSCellContainer(self, name):
        self.syscom.new_struct('SCaWmpSCellContainer', name)
        self.syscom.u32('harqMaxTrDlSCell')
        self.syscom.u32('sCellResourceGroupId')
        self.syscom.u32('interbandCaScell')
        self.syscom.u32('hasCqiParamsScellWmp')
        self.SCqiParamsScellWmp('cqiParamsScellWmp')
        self.syscom.u32('poolIdDataScell')
        self.syscom.u16('ueIndexDataScell')
        self.syscom.u16('paddingUeIndexDataScell')
        self.syscom.end_struct()

    def SCaWmpUlSCellContainer(self, name):
        self.syscom.new_struct('SCaWmpUlSCellContainer', name)
        self.SUplinkPowerControlCommonSCell('uplinkPowerControlCommonSCell')
        self.SUlPCUeParams('uplinkPowerControlDedicatedSCell')
        self.syscom.u32('hasSoundingRsUlConfigDedicatedSCell')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicatedSCell')
        self.syscom.u32('reserved1')
        self.syscom.end_struct()

    def SCarrierAggrParams(self, name):
        self.syscom.new_struct('SCarrierAggrParams', name)
        self.syscom.u32('caSchedFairFact')
        self.syscom.u32('sCellActivationCyclePeriod')
        self.syscom.u32('sCellActivationMethod')
        self.syscom.u32('sCellpCellHARQFdbkUsage')
        self.syscom.u32('caCellIndex')
        self.syscom.u32('numOfCaCells')
        self.syscom.u32('scellActivationLevel')
        self.syscom.u32('numTxWithHighNonGbr')
        self.syscom.u32('dataDivisionThrXCC')
        self.syscom.u32('hasDlCarrierAggrParamsPCell')
        self.SDlCarrierAggrParamsPCell('dlCarrierAggrParamsPCell')
        self.syscom.u32('hasDlCarrierAggrParamsSCell')
        self.SDlCarrierAggrParamsSCell('dlCarrierAggrParamsSCell')
        self.syscom.u32('actULCAggr')
        self.syscom.u32('hasUlCaPathlossThr')
        self.syscom.u32('ulCaPathlossThr')
        self.syscom.end_struct()

    def SCchInformationDlDcm(self, name):
        self.syscom.new_struct('SCchInformationDlDcm', name)
        self.syscom.array('16', 'u16', 'sirCommonDbchTable')
        self.syscom.u16('sirCommonPch')
        self.syscom.u16('sirCommonRachResp')
        self.syscom.u16('flagSSDbch')
        self.syscom.u16('flagSSRachResp')
        self.syscom.u16('offsetRBnumSS')
        self.syscom.end_struct()

    def SCchInformationUlDcm(self, name):
        self.syscom.new_struct('SCchInformationUlDcm', name)
        self.syscom.u16('maxNumOfMsg3')
        self.syscom.u16('nRach')
        self.syscom.u16('flagPRACHposition')
        self.syscom.u16('rbRachM3start0')
        self.syscom.u16('rbRachM3start1')
        self.syscom.u16('sizeRachM3RA')
        self.syscom.u16('sizeRachM3D')
        self.syscom.u16('numOfRbsRachM3RA')
        self.syscom.u16('numOfRbsRachM3D')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SCellCarrierInfo(self, name):
        self.syscom.new_struct('SCellCarrierInfo', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('dlChBw')
        self.syscom.u32('ulChBw')
        self.syscom.end_struct()

    def SCellSlotConf(self, name):
        self.syscom.new_struct('SCellSlotConf', name)
        self.syscom.u32('amountOfSlots')
        self.syscom.u32('lowestSlot')
        self.syscom.end_struct()

    def SCellSpecificReports(self, name):
        self.syscom.new_struct('SCellSpecificReports', name)
        self.syscom.u32('cellId')
        self.syscom.u32('numberOfReports')
        self.syscom.end_struct()

    def SCoeffParamsLCGDcm(self, name):
        self.syscom.new_struct('SCoeffParamsLCGDcm', name)
        self.syscom.array('32', 'SSIULSpecificParamsDcm', 'siulSpecificParamsTable')
        self.syscom.u16('nonAllocTimeLowTh')
        self.syscom.u16('nonAllocTimeHighTh')
        self.syscom.u16('weightCoeffNonAllocTime')
        self.syscom.u16('weightCoeffUlADR')
        self.syscom.u16('forgettingFactorConvAdrUl')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SCoeffParamsLCPDcm(self, name):
        self.syscom.new_struct('SCoeffParamsLCPDcm', name)
        self.SCoeffReTxInfoDcm('prioHarqDl')
        self.syscom.array('32', 'SSIDLSpecificParamsDcm', 'sidlSpecificParamsTable')
        self.syscom.u16('buffTimeLowTh')
        self.syscom.u16('buffTimeHighTh')
        self.syscom.u16('weightCoeffNumReTx')
        self.syscom.u16('weightCoeffBuffTime')
        self.syscom.u16('weightCoeffDlADR')
        self.syscom.u16('forgettingFactorConvAdrDl')
        self.syscom.end_struct()

    def SCoeffReTxInfoDcm(self, name):
        self.syscom.new_struct('SCoeffReTxInfoDcm', name)
        self.syscom.u16('coeffNumReTx0')
        self.syscom.u16('coeffNumReTx1')
        self.syscom.u16('coeffNumReTx2to3')
        self.syscom.u16('coeffNumReTx4to15')
        self.syscom.end_struct()

    def SCommonCellNbrConfig(self, name):
        self.syscom.new_struct('SCommonCellNbrConfig', name)
        self.syscom.u32('nbrCongHandling')
        self.syscom.u32('maxNbrTrafficLimit')
        self.syscom.u32('maxPrbsPerNbrUe')
        self.syscom.end_struct()

    def SCommonCellParams(self, name):
        self.syscom.new_struct('SCommonCellParams', name)
        self.syscom.u32('lCelId')
        self.syscom.u32('dlChBw')
        self.syscom.u32('ulChBw')
        self.syscom.i32('pMax')
        self.syscom.u32('dlPhyDataAddress')
        self.syscom.u32('ulPhyDataAddress')
        self.syscom.u32('maxNrSymPdcch')
        self.syscom.u32('taTimer')
        self.syscom.u32('taMaxOffset')
        self.syscom.u32('dlMimoMode')
        self.syscom.u32('cycPrefixDl')
        self.syscom.u32('cycPreFixUl')
        self.syscom.u32('testModelActive')
        self.syscom.u32('hasFrameConfTdd')
        self.SFrameConfTdd('frameConfTdd')
        self.syscom.u32('latencyIndAddress')
        self.syscom.u32('hasDlMimoModeRTX')
        self.syscom.u32('dlMimoModeRTX')
        self.syscom.end_struct()

    def SCommonCellParamsWmp(self, name):
        self.syscom.new_struct('SCommonCellParamsWmp', name)
        self.syscom.u32('iniPrbsUl')
        self.syscom.u32('maxNumPrbSr')
        self.syscom.u32('dlsTputAvgT')
        self.syscom.u32('ulsTputAvgT')
        self.syscom.u32('maxNumUeDl')
        self.syscom.u32('maxNumUeUl')
        self.syscom.i32('psd0')
        self.syscom.i32('psdMimo')
        self.syscom.u32('dl64QamEnable')
        self.syscom.u32('enableDl16Qam')
        self.syscom.u32('dlsUsePartPrb')
        self.syscom.u32('ilMinDatvolUl')
        self.syscom.u32('ilReacTimerUl')
        self.syscom.u32('enablePhichCtrlUl')
        self.syscom.u32('taOffsetSchedMgn')
        self.syscom.u32('taCmdMaxRetry')
        self.syscom.u32('taTimerMargin')
        self.syscom.u32('nCqiDtx')
        self.syscom.u32('nCqiRec')
        self.syscom.u32('redBwEnDl')
        self.SOaMRedBwMaxRbDl('redBwMaxRbDl')
        self.syscom.u32('redBwRpaEnUl')
        self.SRadioLinkFailureParams('radioLinkFailureParams')
        self.SRateCappingParams('rateCappingParams')
        self.SUlPCCellParams('ulPCCellParams')
        self.syscom.u32('dlsFdPfSchAvgC')
        self.syscom.u32('qciWeightAlignDl')
        self.syscom.u32('ulsFdPrbAssignAlg')
        self.syscom.u32('qciWeightAlignUl')
        self.syscom.u32('actModulationSchemeUL')
        self.syscom.u32('ulsSchedMethod')
        self.syscom.u32('ulsInterferenceCst')
        self.syscom.u32('ulsNumSchedAreaUl')
        self.syscom.u32('ulsTxPowDenConst')
        self.SExtendedDrxParameters('extendedDrxParameters')
        self.SPlmnId('primaryPLMNId')
        self.STtiBundlingParameters('ttiBundlingParameters')
        self.syscom.u32('actCsiDroppingSolution')
        self.SArrayOfOaMUlsPuschMask('ulsPuschMask')
        self.syscom.u32('hasRedBwRbUlConfig')
        self.SOaMRedBwRbUlConfig('redBwRbUlConfig')
        self.syscom.u32('actNbrForNonGbrBearers')
        self.syscom.u32('hasCommonCellNbrConfig')
        self.SCommonCellNbrConfig('commonCellNbrConfig')
        self.syscom.u32('amountBlankedRes')
        self.syscom.u32('hasActDlIsh')
        self.syscom.u32('actDlIsh')
        self.syscom.u32('cellType')
        self.syscom.u32('hasInterferenceShaping')
        self.SInterferenceShaping('interferenceShaping')
        self.syscom.u32('l1InstanceSize')
        self.syscom.u32('expectedCellSize')
        self.syscom.u32('actTaHistCounters')
        self.syscom.u32('actProactSchedBySrb')
        self.syscom.u32('actFlexScellSelect')
        self.syscom.u32('eutraCelId')
        self.syscom.u32('actUlMultiCluster')
        self.syscom.u32('actSrb1Robustness')
        self.SOaMDlSrbCqiOffset('dlSrbCqiOffset')
        self.syscom.u32('actUlpcRachPwrCtrl')
        self.syscom.u32('numOfPlmnIdList')
        self.syscom.array('5', 'SPlmnId', 'plmnIdList')
        self.syscom.u32('hasUlSrbRobustOffset')
        self.syscom.i32('ulSrbRobustOffset')
        self.syscom.u32('hasCommonCellParamsWmpTdd')
        self.SCommonCellParamsWmpTdd('commonCellParamsWmpTdd')
        self.syscom.end_struct()

    def SCommonCellParamsWmpTdd(self, name):
        self.syscom.new_struct('SCommonCellParamsWmpTdd', name)
        self.syscom.u32('maxNumUeDlDwPTS')
        self.syscom.u32('nSrsDtx')
        self.syscom.u32('nSrsRec')
        self.syscom.u32('dlsSchedType')
        self.syscom.u32('ulsSrelFilterCst')
        self.syscom.u32('dlsNgap')
        self.syscom.u32('dlsDciCch')
        self.SPuschHoppingInformation('puschHoppingInformation')
        self.syscom.u32('dlsFdAlg')
        self.SOaMAntBearingForAoaCalc('antBearingForAoa')
        self.syscom.u32('earfcnUL')
        self.SUlSpsParameters('ulSpsParameters')
        self.SOaMUciOnlyMaxCodeRate('uciOnlyMaxCodeRate')
        self.SOaMAntElementSpacing('antElementSpacing')
        self.syscom.u32('actFallback2Ssf5')
        self.syscom.u32('hasDelayOfAbsoluteDist')
        self.syscom.u32('delayOfAbsoluteDist')
        self.syscom.u32('hasUlMuMimoParameters')
        self.SUlMuMimoParameters('ulMuMimoParameters')
        self.syscom.end_struct()

    def SConfigurableUsageAddresses(self, name):
        self.syscom.new_struct('SConfigurableUsageAddresses', name)
        self.syscom.u32('numOfConfigurableUsageAddresses')
        self.syscom.array('6', 'SAddressInfo', 'configurableUsageAddresses')
        self.syscom.end_struct()

    def SConfiguredCsiRs(self, name):
        self.syscom.new_struct('SConfiguredCsiRs', name)
        self.syscom.u32('csiRsResourceConf')
        self.syscom.u32('csiRsSubfrConf')
        self.syscom.i32('csiRsPwrOffset')
        self.syscom.end_struct()

    def SContainerOfOaMSuperCellParSet(self, name):
        self.syscom.new_struct('SContainerOfOaMSuperCellParSet', name)
        self.syscom.u32('hasSuperCellParSet')
        self.SOaMSuperCellParSet('superCellParSet')
        self.syscom.end_struct()

    def SContentionResInd(self, name):
        self.syscom.new_struct('SContentionResInd', name)
        self.syscom.u16('cellId')
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u8('raEvent')
        self.syscom.u8('paddingRaEvent')
        self.syscom.u64('ueContentionResolutionId')
        self.syscom.end_struct()

    def SContextInfo(self, name):
        self.syscom.new_struct('SContextInfo', name)
        self.syscom.u16('lnCelId')
        self.syscom.u16('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('contextType')
        self.syscom.u32('numGtpTeIds')
        self.syscom.array('8', 'u32', 'gtpTeIdList')
        self.syscom.end_struct()

    def SConvVoiceParams(self, name):
        self.syscom.new_struct('SConvVoiceParams', name)
        self.syscom.u32('actConvVoice')
        self.syscom.u32('actDlsVoicePacketAgg')
        self.syscom.u32('actDlsOldtc')
        self.SOaMDlsOldtcTarget('dlsOldtcTarget')
        self.syscom.u32('dlsOldtcStepUp')
        self.syscom.u32('ulsMaxPacketAgg')
        self.syscom.u32('ulsVoipOverhead')
        self.syscom.u32('actVoLteCallSteering')
        self.syscom.end_struct()

    def SCplaParamsDlDcm(self, name):
        self.syscom.new_struct('SCplaParamsDlDcm', name)
        self.SPdcchTpcParamsDlDcm('pdcchTpcParamsDl')
        self.SPhichTpcParamsDlDcm('phichTpcParamsDl')
        self.syscom.u16('txPowerOfPcfich')
        self.syscom.u16('cqiAvgForgetFactorCpla')
        self.syscom.end_struct()

    def SCpuLoadMeasurementConfig(self, name):
        self.syscom.new_struct('SCpuLoadMeasurementConfig', name)
        self.syscom.u32('sicad')
        self.syscom.u32('measGroupId')
        self.syscom.u8('reset')
        self.syscom.u8('getIdleMeasurements')
        self.syscom.u8('recordIdleMeasurementsForIntervalOnly')
        self.syscom.u8('padding')
        self.syscom.u16('startDelayMs')
        self.syscom.u16('intervalMs')
        self.syscom.end_struct()

    def SCpuLoads(self, name):
        self.syscom.new_struct('SCpuLoads', name)
        self.syscom.u16('min')
        self.syscom.u16('max')
        self.syscom.u16('average')
        self.syscom.end_struct()

    def SCpuMeasLoads(self, name):
        self.syscom.new_struct('SCpuMeasLoads', name)
        self.syscom.u16('min')
        self.syscom.u16('max')
        self.syscom.u16('average')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SCqiParams(self, name):
        self.syscom.new_struct('SCqiParams', name)
        self.syscom.u32('cqiAperMode')
        self.syscom.u32('cqiPerEnable')
        self.syscom.u32('numOfCqiPmi')
        self.syscom.array('2', 'u32', 'iCqiPmi')
        self.syscom.u32('resourceIndexCqi')
        self.syscom.u32('cqiPerMode')
        self.syscom.u32('riEnable')
        self.syscom.u32('numOfRi')
        self.syscom.array('2', 'u32', 'iRi')
        self.syscom.u32('cqiPerSimulAck')
        self.syscom.u32('cqiPerSbCycK')
        self.syscom.u32('hasCqiPerSbPeriodFactor')
        self.syscom.u32('cqiPerSbPeriodFactor')
        self.syscom.end_struct()

    def SCqiParamsLCPDcm(self, name):
        self.syscom.new_struct('SCqiParamsLCPDcm', name)
        self.syscom.u16('deltaCqiAdjDl')
        self.syscom.u16('targetBlerDl')
        self.syscom.u16('powerOffsetCqiDl')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SCqiParamsScell(self, name):
        self.syscom.new_struct('SCqiParamsScell', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('enbId')
        self.syscom.u32('cqiAperMode')
        self.syscom.u32('cqiPerEnable')
        self.syscom.u32('iCqiPmi')
        self.syscom.u32('resourceIndexCqiR10')
        self.syscom.u32('cqiPerMode')
        self.syscom.u32('riEnable')
        self.syscom.u32('iRi')
        self.syscom.u32('cqiPerSimulAck')
        self.syscom.u32('cqiPerSbCycK')
        self.syscom.u32('cqiPerSbPeriodicityFactorR10')
        self.syscom.end_struct()

    def SCqiParamsScellWmp(self, name):
        self.syscom.new_struct('SCqiParamsScellWmp', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('cqiAperPollT')
        self.syscom.u32('cqiAperEnable')
        self.syscom.end_struct()

    def SCqiParamsWmp(self, name):
        self.syscom.new_struct('SCqiParamsWmp', name)
        self.syscom.u32('cqiAperPollT')
        self.syscom.u32('cqiAperEnable')
        self.syscom.u32('cqiPerSimulAckPucchf3')
        self.syscom.end_struct()

    def SCrossReferenceTable(self, name):
        self.syscom.new_struct('SCrossReferenceTable', name)
        self.syscom.u32('nodeaddress')
        self.syscom.array('3', 'SNmapAddress', 'nmapAddress')
        self.syscom.end_struct()

    def SCsBIANeighborCellParameters(self, name):
        self.syscom.new_struct('SCsBIANeighborCellParameters', name)
        self.syscom.u32('lnCelId')
        self.SOaMAntBearingForAoaCalc('antBearingForAoa')
        self.SOaMAntElementSpacing('antElementSpacing')
        self.syscom.end_struct()

    def SCsBIAParameters(self, name):
        self.syscom.new_struct('SCsBIAParameters', name)
        self.syscom.u32('bwRatioCsBIA')
        self.syscom.u32('pCellA3Reuse')
        self.syscom.u32('mutingPatternCheckPeriod')
        self.syscom.u32('csBIAThreshold')
        self.syscom.u32('hasLeftNeighborCellParameters')
        self.SCsBIANeighborCellParameters('leftNeighborCellParameters')
        self.syscom.u32('hasRightNeighborCellParameters')
        self.SCsBIANeighborCellParameters('rightNeighborCellParameters')
        self.syscom.end_struct()

    def SCsiRsConfiguration(self, name):
        self.syscom.new_struct('SCsiRsConfiguration', name)
        self.syscom.u32('numOfCsiRsAntennaPorts')
        self.syscom.u32('numOfConfiguredCsiRs')
        self.syscom.array('3', 'SConfiguredCsiRs', 'configuredCsiRs')
        self.syscom.u32('actCsiRsSubFNonTM9Sch')
        self.syscom.u32('zeroTxPowerResourceConfigList')
        self.syscom.u32('zeroTxPowerSubframeConfig')
        self.syscom.end_struct()

    def SDCIParamsDcm(self, name):
        self.syscom.new_struct('SDCIParamsDcm', name)
        self.syscom.u32('dCIFlagPch')
        self.syscom.u32('dCIFlagDbch')
        self.syscom.u32('dCIFlagRachres')
        self.syscom.u32('flagDistributed')
        self.syscom.u32('nGap')
        self.syscom.end_struct()

    def SDLPersistentParamsDlDcm(self, name):
        self.syscom.new_struct('SDLPersistentParamsDlDcm', name)
        self.syscom.array('8', 'SSpsTfDlDcm', 'persistentTfDlTable')
        self.syscom.array('7', 'u16', 'persistentDlTfrUpTable')
        self.syscom.array('7', 'u16', 'persistentDlTfrDownTable')
        self.syscom.array('7', 'u16', 'persistentTfrInitDlTable')
        self.syscom.array('8', 'u16', 'mcsIndexDl')
        self.syscom.array('8', 'u16', 'numRbDl')
        self.syscom.u16('padding1')
        self.syscom.u32('cqiAverForgetFactor')
        self.syscom.u32('silentPeriodTimerTh')
        self.syscom.u32('persistentTttDlTh')
        self.syscom.u32('persistentReconfigDlTimerTh')
        self.syscom.u16('dlTalkSpurtUpperDataTh')
        self.syscom.u16('dlTalkSpurtLowerDataSIDTh')
        self.syscom.u16('powerAdjStepCqiPersistentDl')
        self.syscom.u16('targetBlerPersistentDl')
        self.syscom.u16('numOfNackTh')
        self.syscom.u16('weightDBCH')
        self.syscom.u16('weightPch')
        self.syscom.u16('averTimePchRbUsage')
        self.syscom.u16('averTimeDbchRbUsage')
        self.syscom.u16('weightRachRes')
        self.syscom.u16('rbMbms')
        self.syscom.u16('weightMbms')
        self.syscom.u16('weightPersistentDl')
        self.syscom.u16('averTimeRachResRbUsage')
        self.syscom.u16('averTimePersistentDlRbUsage')
        self.syscom.u16('cqiAdjustPersistent')
        self.syscom.end_struct()

    def SDRbList(self, name):
        self.syscom.new_struct('SDRbList', name)
        self.syscom.u32('drbId')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def SDataReceived(self, name):
        self.syscom.new_struct('SDataReceived', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.end_struct()

    def SDcchGroup(self, name):
        self.syscom.new_struct('SDcchGroup', name)
        self.syscom.u32('dctG6M22')
        self.syscom.end_struct()

    def SDcchGroup2(self, name):
        self.syscom.new_struct('SDcchGroup2', name)
        self.syscom.u32('dctG3M15')
        self.syscom.end_struct()

    def SDciInfo(self, name):
        self.syscom.new_struct('SDciInfo', name)
        self.syscom.i16('txPower')
        self.syscom.u16('crnti')
        self.syscom.u8('numOfCce')
        self.syscom.u8('cceStartIndex')
        self.syscom.u8('tbSize')
        self.syscom.u8('dciFormat')
        self.syscom.array('8', 'u8', 'data')
        self.syscom.end_struct()

    def SDcmCellContainerDcm(self, name):
        self.syscom.new_struct('SDcmCellContainerDcm', name)
        self.SDlDcmMacPsContainerCSDcm('dlDcmMacPsContainerCS')
        self.SUlDcmMacPsContainerCSDcm('ulDcmMacPsContainerCS')
        self.syscom.end_struct()

    def SDcmCellPoolContainer(self, name):
        self.syscom.new_struct('SDcmCellPoolContainer', name)
        self.syscom.u16('thSCellCqiState')
        self.syscom.u16('thPduSizePaddingTA')
        self.syscom.u32('thSCellActivationDl1')
        self.syscom.u32('thSCellActivationDl2')
        self.syscom.u32('thSCellActivationUl1')
        self.syscom.u32('thSCellActivationUl2')
        self.syscom.u32('timerProhibitActivationCommand')
        self.syscom.u32('timerSCellCqiCheck')
        self.syscom.u32('fdEstimationUsage')
        self.syscom.u32('dlChBw')
        self.syscom.u32('sCellType')
        self.syscom.u16('cqiRef')
        self.syscom.u16('padding')
        self.syscom.array('4', 'SFlagSCellSchedulingUlTable', 'flagSCellSchedulingUlTable')
        self.syscom.array('16', 'SFlagSCellSchedulingDlTable', 'flagSCellSchedulingDlTable')
        self.SMacPsL2Addresses('l2Addresses')
        self.syscom.u32('numOfaddress')
        self.syscom.array('256', 'u32', 'macPsAddresses')
        self.syscom.u32('hasFrameConfTdd')
        self.SFrameConfTdd('frameConfTdd')
        self.syscom.u16('flagSSCheck')
        self.syscom.u16('freqCell')
        self.syscom.end_struct()

    def SDcmCellReconfigurationContainerDcm(self, name):
        self.syscom.new_struct('SDcmCellReconfigurationContainerDcm', name)
        self.STxPowersDlDcm('txPowers')
        self.syscom.end_struct()

    def SDcmDedicRaParams(self, name):
        self.syscom.new_struct('SDcmDedicRaParams', name)
        self.syscom.u32('dedicRaPreExpT')
        self.syscom.u32('dedicRaPreIHoT')
        self.syscom.end_struct()

    def SDcmLCGInfoCSDcm(self, name):
        self.syscom.new_struct('SDcmLCGInfoCSDcm', name)
        self.SCoeffParamsLCGDcm('coeffParamsLCG')
        self.SSirParamsLCGDcm('sirParamsLCG')
        self.syscom.u16('nTmpUlBuffer')
        self.syscom.u16('nTmpUlBuffer2')
        self.syscom.u16('nTmpUlBuffer3')
        self.syscom.u16('reserved1')
        self.syscom.end_struct()

    def SDcmLCPInfoCSDcm(self, name):
        self.syscom.new_struct('SDcmLCPInfoCSDcm', name)
        self.SCoeffParamsLCPDcm('coeffParamsLCP')
        self.SCqiParamsLCPDcm('cqiParamsLCP')
        self.syscom.u32('dlTargetDataRateMeas')
        self.syscom.u16('maxNumHarqRetransmissionsDl')
        self.syscom.u16('flagOrderingLowClass')
        self.syscom.end_struct()

    def SDcmRbContainerDcm(self, name):
        self.syscom.new_struct('SDcmRbContainerDcm', name)
        self.SDlDcmMacPsContainerRbSDcm('dlDcmMacPsContaineRbS')
        self.SUlDcmMacPsContainerRbSDcm('ulDcmMacPsContainerRbS')
        self.syscom.end_struct()

    def SDcmUlResCtrlParamContainerDcm(self, name):
        self.syscom.new_struct('SDcmUlResCtrlParamContainerDcm', name)
        self.STpcPdcchForPucchParamsDlDcm('tpcPdcchForPucchTpcParamsDl')
        self.STpcPdcchForPuschParamsUlDcm('tpcPdcchForPuschTpcParamsUl')
        self.syscom.end_struct()

    def SDcmUlTfrParamContainerDcm(self, name):
        self.syscom.new_struct('SDcmUlTfrParamContainerDcm', name)
        self.syscom.u32('srsBandwidth')
        self.syscom.u16('pSrsOffset')
        self.syscom.u16('flagTtiBundling')
        self.syscom.end_struct()

    def SDcmUserContainerDcm(self, name):
        self.syscom.new_struct('SDcmUserContainerDcm', name)
        self.SDlDcmMacPsContainerUSDcm('dlDcmMacPsContainerUS')
        self.SUlDcmMacPsContainerUSDcm('ulDcmMacPsContainerUS')
        self.syscom.end_struct()

    def SDctDlPdcpSduHdbde(self, name):
        self.syscom.new_struct('SDctDlPdcpSduHdbde', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('numOfDctDlPdcpSduResultsHdbde')
        self.syscom.array('10', 'SDctDlPdcpSduResultHdbde', 'dctDlPdcpSduResultsHdbde')
        self.syscom.end_struct()

    def SDctDlPdcpSduResultHdbde(self, name):
        self.syscom.new_struct('SDctDlPdcpSduResultHdbde', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG11M1')
        self.syscom.u32('dctG11M2')
        self.syscom.u32('dctG11M3')
        self.syscom.u32('dctG11M4')
        self.syscom.u32('dctG11M5')
        self.syscom.u32('dctG11M6')
        self.syscom.u32('dctG11M7')
        self.syscom.u32('dctG11M8')
        self.syscom.u32('dctG11M9')
        self.syscom.u32('dctG11M10')
        self.syscom.u32('dctG11M11')
        self.syscom.end_struct()

    def SDctDlRlcAmPduResult(self, name):
        self.syscom.new_struct('SDctDlRlcAmPduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG9M1')
        self.syscom.u32('dctG9M2')
        self.syscom.u32('dctG9M3')
        self.syscom.end_struct()

    def SDctDlRlcSdu(self, name):
        self.syscom.new_struct('SDctDlRlcSdu', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('numOfDctDlRlcSduResults')
        self.syscom.array('10', 'SDctDlRlcSduResult', 'dctDlRlcSduResults')
        self.syscom.end_struct()

    def SDctDlRlcSduResult(self, name):
        self.syscom.new_struct('SDctDlRlcSduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG15M1')
        self.syscom.u32('dctG15M2')
        self.syscom.end_struct()

    def SDctDlRlcUmPduResult(self, name):
        self.syscom.new_struct('SDctDlRlcUmPduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG9M5')
        self.syscom.end_struct()

    def SDctDlSchData2TmReport(self, name):
        self.syscom.new_struct('SDctDlSchData2TmReport', name)
        self.syscom.u32('numOfDctDlSchData2TmResults')
        self.syscom.u32('cumulativeG6M29_NoTx')
        self.syscom.u32('cumulativeG6M29_Nack')
        self.syscom.u32('cumulativeG6M29_Ack')
        self.syscom.u32('cumulativeG6M29_Dtx')
        self.syscom.u32('cumulativeG6M29_invalid')
        self.syscom.end_struct()

    def SDctDlschData1(self, name):
        self.syscom.new_struct('SDctDlschData1', name)
        self.syscom.u32('cellId')
        self.syscom.u32('sfn')
        self.syscom.u32('subFrameCounter')
        self.syscom.u32('numberOfPdus')
        self.syscom.array('32', 'SDctDlschData1Result', 'dctDlschData1Result')
        self.syscom.end_struct()

    def SDctDlschData1Result(self, name):
        self.syscom.new_struct('SDctDlschData1Result', name)
        self.syscom.u8('transportBlockNumber')
        self.syscom.u8('paddingTransportBlockNumber1')
        self.syscom.u8('paddingTransportBlockNumber2')
        self.syscom.u8('paddingTransportBlockNumber3')
        self.syscom.u32('rnti')
        self.syscom.u32('ueId')
        self.syscom.u8('dctG6M28')
        self.syscom.u8('paddingDctG6M281')
        self.syscom.u8('paddingDctG6M282')
        self.syscom.u8('paddingDctG6M283')
        self.syscom.array('2', 'SDcchGroup', 'dcchGroup')
        self.syscom.array('8', 'SDtchGroup', 'dtchGroup')
        self.syscom.u32('dctG6m24')
        self.syscom.u32('dctG6m25')
        self.syscom.u32('dctG6m26')
        self.syscom.u32('dctG6m27')
        self.syscom.end_struct()

    def SDctG2M4(self, name):
        self.syscom.new_struct('SDctG2M4', name)
        self.syscom.u32('accumulatedData')
        self.syscom.u16('numberOfSubframes')
        self.syscom.u16('paddingNumberOfSubframes')
        self.syscom.end_struct()

    def SDctMeasurementGroupRespInformation(self, name):
        self.syscom.new_struct('SDctMeasurementGroupRespInformation', name)
        self.syscom.u32('groupId')
        self.syscom.u32('receivedForCell1')
        self.syscom.u32('receivedForCell2')
        self.syscom.array('10', 'u32', 'receivedForUe')
        self.syscom.end_struct()

    def SDctUlPdcpPdu(self, name):
        self.syscom.new_struct('SDctUlPdcpPdu', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('numOfDctUlPdcpPduResults')
        self.syscom.array('10', 'SDctUlPdcpPduResult', 'dctUlPdcpPduResults')
        self.syscom.end_struct()

    def SDctUlPdcpPduResult(self, name):
        self.syscom.new_struct('SDctUlPdcpPduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbId')
        self.syscom.u32('dctG10M1N')
        self.syscom.u32('dctG10M1A')
        self.syscom.end_struct()

    def SDctUlRlcAmPduResult(self, name):
        self.syscom.new_struct('SDctUlRlcAmPduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG9M4')
        self.syscom.end_struct()

    def SDctUlRlcUmPduResult(self, name):
        self.syscom.new_struct('SDctUlRlcUmPduResult', name)
        self.syscom.u32('isSrbId')
        self.syscom.u32('rbIdentifier')
        self.syscom.u32('dctG9M6')
        self.syscom.end_struct()

    def SDctUlSch1TmReport(self, name):
        self.syscom.new_struct('SDctUlSch1TmReport', name)
        self.syscom.u32('numOfDctUlsch1TmResults')
        self.syscom.u32('cumulativeDctG2M3')
        self.syscom.u32('cumulativeDctG2M5')
        self.syscom.u32('cumulativeDctG2M6')
        self.syscom.end_struct()

    def SDctUlSchData1TmReport(self, name):
        self.syscom.new_struct('SDctUlSchData1TmReport', name)
        self.syscom.u32('numOfDctUlSchData1Results')
        self.syscom.u32('cumulativeG3M22')
        self.syscom.end_struct()

    def SDctUlSchData2TmReport(self, name):
        self.syscom.new_struct('SDctUlSchData2TmReport', name)
        self.syscom.u32('numOfDctUlSchData2Results')
        self.syscom.u32('cumulativeG3M23')
        self.syscom.end_struct()

    def SDctUlsch1Result(self, name):
        self.syscom.new_struct('SDctUlsch1Result', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u32('dctG2M3')
        self.syscom.u32('dctG2M5')
        self.syscom.u32('dctG2M6')
        self.SDctG2M4('dctG2M4')
        self.syscom.end_struct()

    def SDctUlschData1(self, name):
        self.syscom.new_struct('SDctUlschData1', name)
        self.syscom.u32('cellId')
        self.syscom.u32('sfn')
        self.syscom.u32('subFrameCounter')
        self.syscom.u32('numOfDctUlschData1Results')
        self.syscom.array('32', 'SDctUlschData1Result', 'dctUlschData1Results')
        self.syscom.end_struct()

    def SDctUlschData1Result(self, name):
        self.syscom.new_struct('SDctUlschData1Result', name)
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u8('numberOfDcch')
        self.syscom.u8('paddingNumberOfDcch1')
        self.syscom.u8('paddingNumberOfDcch2')
        self.syscom.u8('paddingNumberOfDcch3')
        self.syscom.array('2', 'SDcchGroup2', 'dcchGroup')
        self.syscom.u8('numberOfDtch')
        self.syscom.u8('paddingNumberOfDtch1')
        self.syscom.u8('paddingNumberOfDtch2')
        self.syscom.u8('paddingNumberOfDtch3')
        self.syscom.array('8', 'SDtchGroup2', 'dtchGroup')
        self.syscom.u32('dctG3M17')
        self.syscom.u32('dctG3M18')
        self.syscom.u32('dctG3M19')
        self.syscom.u32('dctG3M20')
        self.syscom.u8('dctG3M21')
        self.syscom.u8('dctG3M22')
        self.syscom.u16('dctG3M222')
        self.syscom.u32('dctG3M44')
        self.syscom.u32('dctG3M45')
        self.syscom.u32('dctG3M46')
        self.syscom.u32('dctG3M47')
        self.syscom.u32('dctG3M48')
        self.syscom.u32('dctG3M49')
        self.syscom.end_struct()

    def SDctUserInfo(self, name):
        self.syscom.new_struct('SDctUserInfo', name)
        self.syscom.u32('cellId')
        self.syscom.u32('ueId')
        self.syscom.u32('crnti')
        self.syscom.end_struct()

    def SDelayPackedInfoDcm(self, name):
        self.syscom.new_struct('SDelayPackedInfoDcm', name)
        self.syscom.u32('thDelayPacked')
        self.syscom.u16('thDataSizePacked')
        self.syscom.u16('numTxCount')
        self.syscom.u16('numPdu')
        self.syscom.u16('tfMinDelayPacked')
        self.syscom.u16('rbMinDelayPacked')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('paddingReserved2')
        self.syscom.end_struct()

    def SDeployableUnit(self, name):
        self.syscom.new_struct('SDeployableUnit', name)
        self.syscom.u16('nodeAddr')
        self.syscom.u16('explicitPadding')
        self.syscom.u32('nodeType')
        self.syscom.end_struct()

    def SDlBfTbFormat(self, name):
        self.syscom.new_struct('SDlBfTbFormat', name)
        self.syscom.array('4', 'u32', 'bfWeight')
        self.syscom.u32('stBFWeight')
        self.syscom.u16('nSCID')
        self.syscom.u16('cbiValidity')
        self.syscom.u32('numMuPrbs')
        self.syscom.array('4', 'u32', 'muPrbMapSlot0')
        self.syscom.array('4', 'u32', 'muPrbMapSlot1')
        self.syscom.end_struct()

    def SDlBufferStatusInd(self, name):
        self.syscom.new_struct('SDlBufferStatusInd', name)
        self.syscom.u32('amountDataOctets')
        self.syscom.u32('amountOfRlcSduData')
        self.syscom.u16('amountCtrlOctets')
        self.syscom.u16('ueIndex')
        self.syscom.u8('rbId')
        self.syscom.u8('lcId')
        self.syscom.u16('xsfnTimeStamp')
        self.syscom.end_struct()

    def SDlCarrierAggrParamsPCell(self, name):
        self.syscom.new_struct('SDlCarrierAggrParamsPCell', name)
        self.syscom.u32('hasUplinkPcCommonR10')
        self.SUplinkPcCommonR10('uplinkPcCommonR10')
        self.syscom.u32('actULCAggr')
        self.syscom.u32('hasUlCaPathlossThr')
        self.syscom.u32('ulCaPathlossThr')
        self.syscom.u32('earfcn')
        self.syscom.u32('numOfSCellConfigParameters')
        self.syscom.array('12', 'SSCellConfigParameters', 'sCellConfigParameters')
        self.syscom.end_struct()

    def SDlCarrierAggrParamsSCell(self, name):
        self.syscom.new_struct('SDlCarrierAggrParamsSCell', name)
        self.syscom.u32('sCellDeactivationTimerEnb')
        self.syscom.u32('numOfPCellConfigParameters')
        self.syscom.array('12', 'SPCellConfigParameters', 'pCellConfigParameters')
        self.syscom.end_struct()

    def SDlDcmMacPsContainerCSDcm(self, name):
        self.syscom.new_struct('SDlDcmMacPsContainerCSDcm', name)
        self.STxPowersDlDcm('txPowers')
        self.SCchInformationDlDcm('cchInformationDl')
        self.syscom.u16('paddingCchInformationDl')
        self.SCplaParamsDlDcm('cplaParamsDl')
        self.SDrxParamsDlDcm('drxParams')
        self.syscom.array('2', 'STaParamsDlDcm', 'taParamsDl')
        self.SDLPersistentParamsDlDcm('dLPersistentParams')
        self.syscom.array('16', 'SDcmLCPInfoCSDcm', 'dcmLCPInfoTable')
        self.SPucchTpcParamsDlDcm('pucchTpcParamsDl')
        self.SDCIParamsDcm('dciParams')
        self.SSyncInfoDlDcm('syncInfoDl')
        self.SAperiodicCqiParamsDcm('aperiodicCqiParams')
        self.SRbRestrictionParamsDlDcm('rbRestrictionParamsDl')
        self.SDlVoLteParamsDcm('voLteDlParams')
        self.syscom.array('16', 'u16', 'rvInfoTable')
        self.syscom.array('10', 'u16', 'nCapabilityTable')
        self.syscom.u32('rMinDl')
        self.syscom.u32('dlAmbrPeriod')
        self.syscom.u32('thUeInactivityTimeHo')
        self.syscom.u32('thUeInactivityTimeReEst')
        self.syscom.u32('ueInactivityTimerIdleTh')
        self.syscom.u32('fdEstimationUsage')
        self.syscom.u16('maxNumOfEmergCallsDl')
        self.syscom.u16('prioDrx')
        self.syscom.u16('prioMacCe')
        self.syscom.u16('crTh')
        self.syscom.u16('nDlMax')
        self.syscom.u16('maxCqiOffsetDl')
        self.syscom.u16('minCqiOffsetDl')
        self.syscom.u16('cqiRef')
        self.SAssuredPucchInfoDl('assuredPucchInfoDl')
        self.syscom.u16('lteT1TimeTh')
        self.syscom.u16('nDlCandidateMax')
        self.syscom.u16('alphaDlPDCCH')
        self.syscom.u16('betaDlPDCCHCommon')
        self.syscom.u16('gammaDlPDCCH')
        self.syscom.u16('bCaPCell')
        self.syscom.u16('bCaSCell')
        self.syscom.array('4', 'u16', 'bCaTpc')
        self.syscom.u16('thSCellCqiState')
        self.syscom.u16('flagACqiCellSelection')
        self.syscom.u16('padding1')
        self.syscom.u32('thSCellActivationDl1')
        self.syscom.u32('thSCellActivationDl2')
        self.syscom.u32('timerProhibitActivationCommand')
        self.syscom.u32('timerSCellCqiCheck')
        self.syscom.u32('actDeactRetxTimer')
        self.syscom.u16('flagTaSCell')
        self.syscom.u16('padding2')
        self.syscom.u32('sCellType')
        self.syscom.array('4', 'u32', 'thPucchTpc')
        self.syscom.array('4', 'u16', 'nDlUELargeData')
        self.syscom.array('3', 'u16', 'thUELargeData')
        self.syscom.array('3', 'u16', 'flagOrdering')
        self.syscom.u16('nDlPRBRemain')
        self.syscom.u16('thCQIOrdering')
        self.syscom.u16('dlCsearch')
        self.syscom.u16('dlCdataSize')
        self.syscom.u16('thSumRBOrdering')
        self.syscom.u16('flagSSCheck')
        self.syscom.u16('maxTFSS')
        self.syscom.u16('offsetSIRSSData')
        self.syscom.u16('freqCell')
        self.syscom.array('4', 'u16', 'freqAggressor')
        self.syscom.array('4', 'u16', 'freqVictim')
        self.syscom.array('4', 'u16', 'thCQILow')
        self.syscom.array('4', 'u16', 'thCQIHigh')
        self.syscom.array('4', 'u16', 'thPowerLow')
        self.syscom.array('4', 'u16', 'thPowerMiddle')
        self.syscom.array('4', 'u16', 'thPowerHigh')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('reserved3')
        self.syscom.end_struct()

    def SDlDcmMacPsContainerRbSDcm(self, name):
        self.syscom.new_struct('SDlDcmMacPsContainerRbSDcm', name)
        self.syscom.u16('persistentDlEnable')
        self.syscom.u16('lcpDl')
        self.syscom.u16('sidl')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('reserved3')
        self.syscom.u16('reserved4')
        self.syscom.u16('reserved5')
        self.syscom.end_struct()

    def SDlDcmMacPsContainerUSDcm(self, name):
        self.syscom.new_struct('SDlDcmMacPsContainerUSDcm', name)
        self.syscom.u16('numSSCellsParams')
        self.syscom.array('2', 'SSCellsParams', 'sCellsParams')
        self.syscom.u16('padding')
        self.STpcPdcchForPucchParamsDlDcm('tpcPdcchForPucchTpcParams')
        self.syscom.u32('callTypeDl')
        self.syscom.u32('initialUEInactivityTimerValue')
        self.syscom.u32('maxPayloadSizeDlAmbr')
        self.syscom.u32('ueInactivityTimerIdleTh')
        self.syscom.u16('lcpForCqiOffsetAdj')
        self.syscom.u16('p0UePucch')
        self.syscom.u16('initialNumProhibitDelayPacked')
        self.syscom.u16('initialMinDelayPackedIndex')
        self.syscom.end_struct()

    def SDlHarqParameters(self, name):
        self.syscom.new_struct('SDlHarqParameters', name)
        self.syscom.u32('dlHarqTransmissionType')
        self.syscom.u16('subFrameHarqIndex')
        self.syscom.u16('harqId')
        self.syscom.u32('initialTxFrame')
        self.syscom.u32('initialTxSubFrame')
        self.syscom.end_struct()

    def SDlPhyDataAddressInfo(self, name):
        self.syscom.new_struct('SDlPhyDataAddressInfo', name)
        self.syscom.u32('PbchSendReqAddress')
        self.syscom.u32('pdcchSendReqAddress')
        self.syscom.u32('PhichSendReqAddress')
        self.syscom.u32('pdschEventQueueId')
        self.syscom.end_struct()

    def SDlRbsAmResult(self, name):
        self.syscom.new_struct('SDlRbsAmResult', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u8('numberOfRadioBearers')
        self.syscom.u8('paddingNumberOfRadioBearers1')
        self.syscom.u8('paddingNumberOfRadioBearers2')
        self.syscom.u8('paddingNumberOfRadioBearers3')
        self.syscom.array('10', 'SDctDlRlcAmPduResult', 'dctDlRlcAmPduResults')
        self.syscom.end_struct()

    def SDlRbsUmResult(self, name):
        self.syscom.new_struct('SDlRbsUmResult', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u8('numberOfRadioBearers')
        self.syscom.u8('paddingNumberOfRadioBearers1')
        self.syscom.u8('paddingNumberOfRadioBearers2')
        self.syscom.u8('paddingNumberOfRadioBearers3')
        self.syscom.array('10', 'SDctDlRlcUmPduResult', 'dctDlRlcUmPduResults')
        self.syscom.end_struct()

    def SDlSchPduMuxAmountOctets(self, name):
        self.syscom.new_struct('SDlSchPduMuxAmountOctets', name)
        self.syscom.u16('logicalChannelId')
        self.syscom.u16('sessionId')
        self.syscom.u16('ctrl')
        self.syscom.u16('data')
        self.syscom.end_struct()

    def SDlSchPduMuxCwAttributes(self, name):
        self.syscom.new_struct('SDlSchPduMuxCwAttributes', name)
        self.syscom.u32('tbSize')
        self.syscom.u8('drxCommEnable')
        self.syscom.u8('ueTaCeAvail')
        self.syscom.u16('ueTaCeValue')
        self.SCaCeInfo('ueCaCeInfo')
        self.syscom.u8('tfi')
        self.syscom.u8('modulation')
        self.syscom.u8('newDataIndicator')
        self.syscom.u8('redundancyVersion')
        self.syscom.u8('codeWordIndex')
        self.syscom.u8('harqIdCw')
        self.syscom.u8('trnumCw')
        self.syscom.u8('amountRbs')
        self.syscom.array('10', 'SDlSchPduMuxAmountOctets', 'amountRbOctets')
        self.SDlHarqParameters('dlHarqParameters')
        self.syscom.end_struct()

    def SDlSchedulingRules(self, name):
        self.syscom.new_struct('SDlSchedulingRules', name)
        self.syscom.u32('index')
        self.syscom.u32('modulo')
        self.syscom.end_struct()

    def SDlVoLteParamsDcm(self, name):
        self.syscom.new_struct('SDlVoLteParamsDcm', name)
        self.syscom.array('4', 'SDelayPackedInfoDcm', 'delayPackedIndexRefTable')
        self.syscom.array('3', 'u16', 'yDelayPacked')
        self.syscom.u16('paddingYDelayPacked')
        self.syscom.u32('delayPackedTimer')
        self.syscom.u16('cqiDelayPackedDiff')
        self.syscom.u16('alphaDelayPacked')
        self.syscom.u16('delayPackedInitIndex')
        self.syscom.u16('numProhibitDelayPacked')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.end_struct()

    def SDlsch1TmResult(self, name):
        self.syscom.new_struct('SDlsch1TmResult', name)
        self.syscom.u32('numOfDlsch1TmResults')
        self.syscom.u32('cumulativeDctG5M6')
        self.syscom.end_struct()

    def SDrxParameters(self, name):
        self.syscom.new_struct('SDrxParameters', name)
        self.syscom.u32('drxCommEnable')
        self.syscom.u32('drxLongEnable')
        self.syscom.u32('drxStartOffset')
        self.syscom.u32('drxOnDuratT')
        self.syscom.u32('drxInactivityT')
        self.syscom.u32('drxRetransT')
        self.syscom.u32('drxLongCycle')
        self.syscom.u32('drxShortEnable')
        self.syscom.u32('drxShortCycle')
        self.syscom.u32('drxShortCycleTimer')
        self.syscom.u32('smartStInactFactor')
        self.syscom.u32('drxProfileIndex')
        self.syscom.u32('hasDrxConfigType')
        self.syscom.u32('drxConfigType')
        self.syscom.u32('hasDrxConfigId')
        self.syscom.u32('drxConfigId')
        self.syscom.end_struct()

    def SDrxParamsDlDcm(self, name):
        self.syscom.new_struct('SDrxParamsDlDcm', name)
        self.syscom.u32('drxCommandTh')
        self.syscom.u16('flagSRNonDrx')
        self.syscom.u16('reserved1')
        self.syscom.end_struct()

    def SDtchGroup(self, name):
        self.syscom.new_struct('SDtchGroup', name)
        self.syscom.u32('dctG6M23')
        self.syscom.end_struct()

    def SDtchGroup2(self, name):
        self.syscom.new_struct('SDtchGroup2', name)
        self.syscom.u32('dctG3M16')
        self.syscom.end_struct()

    def SEcgi(self, name):
        self.syscom.new_struct('SEcgi', name)
        self.syscom.u32('eci')
        self.SPlmnId('plmnId')
        self.syscom.end_struct()

    def SEicicParameters(self, name):
        self.syscom.new_struct('SEicicParameters', name)
        self.syscom.u32('eIcicCreDelta')
        self.syscom.end_struct()

    def SExtendedDrxParameters(self, name):
        self.syscom.new_struct('SExtendedDrxParameters', name)
        self.syscom.u32('applyOutOfSyncState')
        self.syscom.u32('stInactFactor')
        self.syscom.end_struct()

    def SFastLoadBalanceConfig(self, name):
        self.syscom.new_struct('SFastLoadBalanceConfig', name)
        self.syscom.u32('prbUsageRatioHighThresh')
        self.syscom.u32('prbUsageRatioGapThresh')
        self.syscom.u32('fastLoadBalanceMcsThresh')
        self.syscom.end_struct()

    def SFaultFiltering(self, name):
        self.syscom.new_struct('SFaultFiltering', name)
        self.syscom.u32('faultId')
        self.syscom.u32('blocked')
        self.syscom.u32('faultDetectionWindow')
        self.syscom.u32('faultIndFrequency')
        self.syscom.u32('recoveryState')
        self.syscom.end_struct()

    def SFlagSCellSchedulingDlTable(self, name):
        self.syscom.new_struct('SFlagSCellSchedulingDlTable', name)
        self.syscom.array('2', 'u16', 'flagSCellSchedulingDl')
        self.syscom.end_struct()

    def SFlagSCellSchedulingUlTable(self, name):
        self.syscom.new_struct('SFlagSCellSchedulingUlTable', name)
        self.syscom.array('8', 'u16', 'flagSCellSchedulingUl')
        self.syscom.end_struct()

    def SFrameConfTdd(self, name):
        self.syscom.new_struct('SFrameConfTdd', name)
        self.syscom.u32('tddFrameConf')
        self.syscom.u32('tddSpecSubfConf')
        self.syscom.end_struct()

    def SFrequencyOffsetInfo(self, name):
        self.syscom.new_struct('SFrequencyOffsetInfo', name)
        self.syscom.u16('elapsedTimePusch')
        self.syscom.u16('elapsedTimePucchOrPrach')
        self.syscom.u32('frequencyOffsetPusch')
        self.syscom.u32('frequencyOffsetPucchOrPrach')
        self.syscom.end_struct()

    def SGbrCongestionParams(self, name):
        self.syscom.new_struct('SGbrCongestionParams', name)
        self.syscom.u32('gbrCongHandling')
        self.syscom.u32('maxGbrTrafficLimit')
        self.syscom.u32('addGbrTrafficRrHo')
        self.syscom.u32('addGbrTrafficTcHo')
        self.syscom.end_struct()

    def SGcadAddress(self, name):
        self.syscom.new_struct('SGcadAddress', name)
        self.syscom.u32('eqid')
        self.syscom.u32('ccid')
        self.syscom.end_struct()

    def SGcgi(self, name):
        self.syscom.new_struct('SGcgi', name)
        self.syscom.u16('lac')
        self.syscom.u16('ci')
        self.SPlmnId('plmnId')
        self.syscom.end_struct()

    def SGtpAddressesOfLteL2(self, name):
        self.syscom.new_struct('SGtpAddressesOfLteL2', name)
        self.syscom.array('16', 'u32', 'sicad')
        self.syscom.end_struct()

    def SGtpInfoBearerSetup(self, name):
        self.syscom.new_struct('SGtpInfoBearerSetup', name)
        self.syscom.u32('trswSicad')
        self.SGcadAddress('trswGcad')
        self.STransportLayerAddress('sGwTransportLayerAddress')
        self.STransportLayerAddress('enbTransportLayerAddress')
        self.syscom.u32('sGwTeid')
        self.syscom.u32('enbS1Teid')
        self.syscom.u32('dscp')
        self.syscom.u32('nullTermination')
        self.syscom.end_struct()

    def SGtpInfoDataForwardSetup(self, name):
        self.syscom.new_struct('SGtpInfoDataForwardSetup', name)
        self.syscom.u32('targetSicad')
        self.SGcadAddress('targetGcad')
        self.STransportLayerAddress('peerEntityTransportLayerAddress')
        self.syscom.u32('peerEntityTeid')
        self.syscom.u32('dscp')
        self.syscom.end_struct()

    def SGtpInfoPathSwitch(self, name):
        self.syscom.new_struct('SGtpInfoPathSwitch', name)
        self.STransportLayerAddress('sGwTransportLayerAddress')
        self.syscom.u32('sGwTeid')
        self.syscom.u32('trswSicad')
        self.SGcadAddress('trswGcad')
        self.syscom.end_struct()

    def SGtpInfoUserSetup(self, name):
        self.syscom.new_struct('SGtpInfoUserSetup', name)
        self.syscom.u32('trswSicad')
        self.SGcadAddress('trswGcad')
        self.STransportLayerAddress('sGwTransportLayerAddress')
        self.STransportLayerAddress('enbTransportLayerAddress')
        self.syscom.u32('sGwTeid')
        self.syscom.u32('enbS1Teid')
        self.syscom.u32('enbX2DlTeid')
        self.syscom.u32('enbX2UlTeid')
        self.syscom.u32('dscp')
        self.syscom.end_struct()

    def SGtpUser(self, name):
        self.syscom.new_struct('SGtpUser', name)
        self.syscom.u32('ueId')
        self.syscom.u16('ueGroup')
        self.syscom.u8('handoverType')
        self.syscom.u8('poolId')
        self.syscom.end_struct()

    def SGtpuPathDiagnosticsResult(self, name):
        self.syscom.new_struct('SGtpuPathDiagnosticsResult', name)
        self.syscom.u32('localChip')
        self.syscom.u32('pathStatus')
        self.syscom.end_struct()

    def SHarqReleaseInfo(self, name):
        self.syscom.new_struct('SHarqReleaseInfo', name)
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('paddingServingCellIndex')
        self.syscom.u16('ueIndex')
        self.syscom.u16('crnti')
        self.syscom.u8('harqId1')
        self.syscom.u8('harqId2')
        self.syscom.u8('validHarqId1')
        self.syscom.u8('validHarqId2')
        self.syscom.u8('ackReceivedHarqId1')
        self.syscom.u8('ackReceivedHarqId2')
        self.syscom.u32('lnCellIdServCell')
        self.syscom.end_struct()

    def SInterferenceShaping(self, name):
        self.syscom.new_struct('SInterferenceShaping', name)
        self.syscom.u32('blankingPosition')
        self.syscom.u32('prefAlignment')
        self.syscom.u32('actFastIncreaseGbr')
        self.syscom.u32('actFastIncreaseNonGbr')
        self.syscom.u32('activationThreshold')
        self.syscom.u32('updatePeriod')
        self.syscom.u32('prefResStepSize')
        self.syscom.u32('prefResIncreaseThreshold')
        self.syscom.u32('prefResDecreaseThreshold')
        self.syscom.u32('prefResLowerLimit')
        self.syscom.end_struct()

    def SIpSicAddr(self, name):
        self.syscom.new_struct('SIpSicAddr', name)
        self.UIpAddr('sgwIpAddress')
        self.syscom.u32('trswSicad')
        self.syscom.end_struct()

    def SIpV4(self, name):
        self.syscom.new_struct('SIpV4', name)
        self.syscom.u32('ip')
        self.syscom.end_struct()

    def SIpV6(self, name):
        self.syscom.new_struct('SIpV6', name)
        self.syscom.array('16', 'u8', 'ip')
        self.syscom.end_struct()

    def SL2CaParamsContainer(self, name):
        self.syscom.new_struct('SL2CaParamsContainer', name)
        self.syscom.u32('poolId')
        self.SConfigurableUsageAddresses('l2ConfigurableUsageAddresses')
        self.SL2PhyAddressess('l2PhyAddressess')
        self.SL2MacPsAddresses('l2MacPsAddresses')
        self.SL2L2Addresses('l2L2Addresses')
        self.syscom.u32('hasReserved1')
        self.syscom.u32('reserved1')
        self.syscom.u32('hasReserved2')
        self.syscom.u32('reserved2')
        self.syscom.u32('hasReserved3')
        self.syscom.u32('reserved3')
        self.syscom.u32('hasReserved4')
        self.syscom.u32('reserved4')
        self.syscom.end_struct()

    def SL2L2Addresses(self, name):
        self.syscom.new_struct('SL2L2Addresses', name)
        self.syscom.u32('numOfUeGroups')
        self.syscom.array('16', 'u32', 'dlGtpuSicad')
        self.syscom.array('16', 'SGcadAddress', 'dlL2Gcad')
        self.syscom.u32('dataMeasCounterClient')
        self.syscom.u32('dataUser')
        self.syscom.u32('dataUserLoadClient')
        self.syscom.u32('dataMeasInternalDCT')
        self.syscom.u32('dataMeasInternalAPI')
        self.syscom.end_struct()

    def SL2MacPsAddresses(self, name):
        self.syscom.new_struct('SL2MacPsAddresses', name)
        self.syscom.u32('psUserUl')
        self.syscom.u32('psUserDl')
        self.syscom.u32('psUserMgmt')
        self.syscom.u32('dataCtrlPdcchClient')
        self.syscom.u32('numOfUeGroups')
        self.syscom.array('16', 'u32', 'dataCtrlUlClient')
        self.syscom.array('16', 'u32', 'dataCtrlDlClient')
        self.syscom.end_struct()

    def SL2PhyAddressess(self, name):
        self.syscom.new_struct('SL2PhyAddressess', name)
        self.syscom.u32('pdschCw0SendReqAddress')
        self.syscom.u32('pdschCw1SendReqAddress')
        self.syscom.u32('srioType9Cos')
        self.syscom.u32('srioType9StreamId')
        self.syscom.u32('pdschEventQueueId')
        self.syscom.u32('puschReceiverAddress')
        self.syscom.end_struct()

    def SLcgIds(self, name):
        self.syscom.new_struct('SLcgIds', name)
        self.syscom.u32('ueBufferStatusReport')
        self.syscom.u32('receivedDataSize')
        self.syscom.end_struct()

    def SLinkAdaptConfParams(self, name):
        self.syscom.new_struct('SLinkAdaptConfParams', name)
        self.syscom.u32('dlamcEnable')
        self.syscom.u32('dlOlqcEnable')
        self.syscom.i32('dlOlqcDeltaCqiIni')
        self.syscom.u32('dlOlqcDeltaCqiMax')
        self.syscom.i32('dlOlqcDeltaCqiMin')
        self.syscom.u32('dlOlqcDeltaCqiStepUp')
        self.SOaMDlTargetBler('dlTargetBler')
        self.syscom.u32('dlamcCqiDef')
        self.syscom.u32('dlamcTHistCqi')
        self.syscom.i32('cqiCompSmRi1Ol')
        self.syscom.u32('cqiCompTdRi2Ol')
        self.syscom.i32('cqiCompSmRi1Cl')
        self.syscom.u32('cqiCompTdRi2Cl')
        self.syscom.u32('ulTargetBler')
        self.syscom.u32('ulamcUpdowngrF')
        self.syscom.u32('ulamcDeltaCmax')
        self.syscom.i32('ulamcDeltaCmin')
        self.syscom.i32('ulamcDeltaCini')
        self.syscom.u32('ulamcCStepUp')
        self.syscom.u32('ulamcAllTbEn')
        self.syscom.u32('ulamcHistMcsT')
        self.syscom.u32('ulamcInactT')
        self.syscom.u32('ulamcSwitchPer')
        self.syscom.u32('ulatbPhrAvgF')
        self.syscom.u32('ulatbEventPer')
        self.syscom.u32('actUlLnkAdp')
        self.SOaMEUlLaAtbPeriod('eUlLaAtbPeriod')
        self.SOaMEUlLaPrbIncDecFactor('eUlLaPrbIncDecFactor')
        self.SOaMEUlLaBlerAveWin('eUlLaBlerAveWin')
        self.SOaMEUlLaDeltaMcs('eUlLaDeltaMcs')
        self.SOaMEUlLaLowPrbThr('eUlLaLowPrbThr')
        self.SOaMEUlLaLowMcsThr('eUlLaLowMcsThr')
        self.syscom.u32('actOlLaPdcch')
        self.SOaMPdcchHarqTargetBler('pdcchHarqTargetBler')
        self.SOaMFUlLAAtbTrigThr('fUlLAAtbTrigThr')
        self.syscom.end_struct()

    def SLiquidCellConfiguration(self, name):
        self.syscom.new_struct('SLiquidCellConfiguration', name)
        self.syscom.u32('ulMeasThrJtCsiRs')
        self.syscom.u32('ulMeasThrSuMuCsiRs')
        self.syscom.u32('ulMeasHystJT')
        self.syscom.u32('ulMeasHystSuMu')
        self.syscom.u32('ulMeasN')
        self.syscom.u32('ulMeasAlphaBase')
        self.syscom.u32('liquidCellSuMuMode')
        self.syscom.end_struct()

    def SLnCellId(self, name):
        self.syscom.new_struct('SLnCellId', name)
        self.syscom.u32('cellId')
        self.SPlmnId('plmnId')
        self.syscom.end_struct()

    def SLocalCellResMapToAntennaBus(self, name):
        self.syscom.new_struct('SLocalCellResMapToAntennaBus', name)
        self.syscom.u32('localCellResourceId')
        self.syscom.u32('tCellAdjustment')
        self.syscom.u32('numOfTxAntennasInLocalCell')
        self.syscom.array('2', 'UAntennaBusParameters', 'txAntennasInLocalCell')
        self.syscom.u32('numOfRxAntennasInLocalCell')
        self.syscom.array('4', 'UAntennaBusParameters', 'rxAntennasInLocalCell')
        self.syscom.end_struct()

    def SMacMessageHeader(self, name):
        self.syscom.new_struct('SMacMessageHeader', name)
        self.syscom.u32('cellId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.u32('srioDioBufferAddr')
        self.syscom.u32('srioDioBufferSize')
        self.syscom.end_struct()

    def SMacPduDumpResults(self, name):
        self.syscom.new_struct('SMacPduDumpResults', name)
        self.syscom.u32('ueId')
        self.syscom.u32('sfnOfFirstReport')
        self.syscom.u32('subFrameCounterOfLastReport')
        self.syscom.u32('cellId')
        self.syscom.u32('totalNbrOfRetransmission')
        self.syscom.u32('sequenceNumberOfLastReport')
        self.syscom.u32('totalPduDataLengthInBytes')
        self.syscom.end_struct()

    def SMacPsL2Addresses(self, name):
        self.syscom.new_struct('SMacPsL2Addresses', name)
        self.syscom.u32('numOfUeGroupsPerPool')
        self.syscom.array('16', 'u32', 'dataCtrlDlData')
        self.syscom.array('16', 'u32', 'dataCtrlUl')
        self.syscom.array('16', 'u32', 'dataCtrlDiscard')
        self.syscom.array('16', 'u32', 'puschReceiveRespUAddress')
        self.syscom.u32('poolId')
        self.syscom.end_struct()

    def SMacPsMacPsAddresses(self, name):
        self.syscom.new_struct('SMacPsMacPsAddresses', name)
        self.syscom.u32('ulCell')
        self.syscom.u32('dlCell')
        self.syscom.u32('ulScheduler')
        self.syscom.u32('dlScheduler')
        self.syscom.u32('usedMacPsUeGroups')
        self.syscom.u32('psUserDlAddress')
        self.syscom.u32('psUserUlAddress')
        self.syscom.array('16', 'u32', 'psDataCtrlAddress')
        self.syscom.u32('psUserScellUlAddress')
        self.syscom.u32('psUserScellDlAddress')
        self.syscom.u32('psUserScellClientAddress')
        self.syscom.end_struct()

    def SMacSduRateReport(self, name):
        self.syscom.new_struct('SMacSduRateReport', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('measurementId')
        self.syscom.u32('status')
        self.syscom.array('16', 'SMacSduReportValue', 'macDlSduReportValueServingCell')
        self.syscom.array('16', 'SMacSduReportValue', 'macDlSduReportValueSCell')
        self.syscom.array('4', 'SMacSduReportValue', 'macUlSduReportValueServingCell')
        self.syscom.end_struct()

    def SMacSduReport(self, name):
        self.syscom.new_struct('SMacSduReport', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('status')
        self.syscom.array('16', 'SMacSduReportValue', 'macSduReportValue')
        self.syscom.end_struct()

    def SMacSduReportValue(self, name):
        self.syscom.new_struct('SMacSduReportValue', name)
        self.syscom.array('4', 'u32', 'macSduBitmap')
        self.syscom.u32('macSduDataAmount')
        self.syscom.end_struct()

    def SMacToPhyEvent(self, name):
        self.syscom.new_struct('SMacToPhyEvent', name)
        self.syscom.u16('crnti')
        self.syscom.u8('event')
        self.syscom.u8('type')
        self.syscom.end_struct()

    def SMacUpovlha(self, name):
        self.syscom.new_struct('SMacUpovlha', name)
        self.syscom.u32('enableSuspendSrs')
        self.syscom.u32('enableTxDivTransmission')
        self.syscom.end_struct()

    def SMbmsPduCtrlReq(self, name):
        self.syscom.new_struct('SMbmsPduCtrlReq', name)
        self.syscom.u16('mcchSn')
        self.syscom.u16('msiNum')
        self.SMcchMessage('mcchMessage')
        self.syscom.array('29', 'SMchScheduleInfo', 'mchScheduleInfo')
        self.syscom.end_struct()

    def SMcchMessage(self, name):
        self.syscom.new_struct('SMcchMessage', name)
        self.syscom.u32('size')
        self.syscom.array('256', 'u8', 'data')
        self.syscom.end_struct()

    def SMchScheduleInfo(self, name):
        self.syscom.new_struct('SMchScheduleInfo', name)
        self.syscom.u32('mtchId')
        self.syscom.u32('stopMtchCount')
        self.syscom.u16('sessionId')
        self.syscom.u16('paddingSessionId')
        self.syscom.end_struct()

    def SMcsParams(self, name):
        self.syscom.new_struct('SMcsParams', name)
        self.syscom.u32('raLargeMcsUl')
        self.syscom.u32('raLargeVolUl')
        self.syscom.u32('raSmallMcsUl')
        self.syscom.u32('raSmallVolUl')
        self.syscom.u32('maxCrSibDl')
        self.syscom.u32('maxCrPgDl')
        self.syscom.u32('maxCrRaDl')
        self.syscom.u32('maxCrRa4Dl')
        self.syscom.u32('iniMcsDl')
        self.syscom.u32('iniMcsUl')
        self.syscom.end_struct()

    def SMeasReportValue(self, name):
        self.syscom.new_struct('SMeasReportValue', name)
        self.syscom.u32('status')
        self.syscom.u32('measurementValue')
        self.syscom.end_struct()

    def SMeasurementA7or8(self, name):
        self.syscom.new_struct('SMeasurementA7or8', name)
        self.syscom.u32('enableTwoUserMeasurement')
        self.syscom.u32('stationaryUeResources')
        self.syscom.end_struct()

    def SMeasurementDcm5toDcm8(self, name):
        self.syscom.new_struct('SMeasurementDcm5toDcm8', name)
        self.syscom.u32('mcsIndex')
        self.syscom.end_struct()

    def SMemBuffer(self, name):
        self.syscom.new_struct('SMemBuffer', name)
        self.syscom.u32('addressPtr')
        self.syscom.u32('sizeInBytes')
        self.syscom.end_struct()

    def SMessageAddress(self, name):
        self.syscom.new_struct('SMessageAddress', name)
        self.syscom.u8('board')
        self.syscom.u8('cpu')
        self.syscom.u16('task')
        self.syscom.end_struct()

    def SMessageResult(self, name):
        self.syscom.new_struct('SMessageResult', name)
        self.syscom.u32('status')
        self.syscom.u32('cause')
        self.syscom.u32('specificCause')
        self.syscom.end_struct()

    def SMimoCtrlParams(self, name):
        self.syscom.new_struct('SMimoCtrlParams', name)
        self.syscom.u32('mimoOlCqiComp')
        self.syscom.u32('mimoOlCqiAvg')
        self.syscom.u32('mimoOlRiAvg')
        self.syscom.u32('mimoClCqiComp')
        self.syscom.u32('mimoClCqiAvg')
        self.syscom.u32('mimoClRiAvg')
        self.syscom.u32('hasMimoClConfig')
        self.SOaMMimoClConfig('mimoClConfig')
        self.syscom.u32('hasMimoOlConfig')
        self.SOaMMimoOlConfig('mimoOlConfig')
        self.syscom.end_struct()

    def SModNumOfLayers(self, name):
        self.syscom.new_struct('SModNumOfLayers', name)
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('maxLayersDeliveredToUe')
        self.syscom.u32('layersRestrictedToTwo')
        self.syscom.end_struct()

    def SMsg3DiscardData(self, name):
        self.syscom.new_struct('SMsg3DiscardData', name)
        self.syscom.u32('hasRaMsg3Thr')
        self.syscom.u32('raMsg3Thr')
        self.syscom.u32('hasRaMsg3ThrLowParameters')
        self.SRaMsg3ThrLowParameters('raMsg3ThrLowParameters')
        self.syscom.end_struct()

    def SMsg3Info(self, name):
        self.syscom.new_struct('SMsg3Info', name)
        self.syscom.u32('crnti')
        self.syscom.u32('size')
        self.syscom.array('6', 'u8', 'data')
        self.syscom.u16('paddingData')
        self.syscom.end_struct()

    def SMuMimoParameters(self, name):
        self.syscom.new_struct('SMuMimoParameters', name)
        self.syscom.u32('actDlMuMimo')
        self.syscom.u32('dlMuMimoCqiThd')
        self.syscom.u32('dlMuMimoCorrThd')
        self.syscom.u32('actDlMuGainMax')
        self.syscom.end_struct()

    def SMultiplexingtable(self, name):
        self.syscom.new_struct('SMultiplexingtable', name)
        self.syscom.u32('numOfLinksToBeCombined')
        self.syscom.array('4', 'u32', 'combinedLinkIndex')
        self.syscom.u32('numOfLinksToBeDecombined')
        self.syscom.array('4', 'u32', 'decombinedLinkIndex')
        self.syscom.u32('numOfLinksToBeRedirect')
        self.syscom.array('numOfLinksToBeRedirect', 'u32', 'redirectLinkIndex')
        self.syscom.end_struct()

    def SNbCellParams(self, name):
        self.syscom.new_struct('SNbCellParams', name)
        self.syscom.u32('hostLnCelId')
        self.syscom.array('3', 'u32', 'numberOfRepetition')
        self.syscom.array('3', 'u8', 'dlMcsPerCoverageType')
        self.syscom.array('3', 'u8', 'ulMcsPerCoverageType')
        self.syscom.u16('paddingUlMcsPerCoverageType')
        self.syscom.u32('dlPowerSetting')
        self.syscom.array('3', 'u32', 'extraParams')
        self.syscom.end_struct()

    def SNmapAddress(self, name):
        self.syscom.new_struct('SNmapAddress', name)
        self.syscom.u32('chip')
        self.syscom.u32('cpu')
        self.syscom.end_struct()

    def SNodeAddress(self, name):
        self.syscom.new_struct('SNodeAddress', name)
        self.syscom.u16('ulCellMac')
        self.syscom.u16('ulUeMac')
        self.syscom.u16('ulSchedulerMac')
        self.syscom.u16('dlCellMac')
        self.syscom.u16('dlUeMac')
        self.syscom.u16('dlSchedulerMac')
        self.syscom.u16('cellManager')
        self.syscom.end_struct()

    def SOaMActLteU(self, name):
        self.syscom.new_struct('SOaMActLteU', name)
        self.syscom.u32('hasActLteU')
        self.syscom.u32('actLteU')
        self.syscom.end_struct()

    def SOaMAllowFastActivation(self, name):
        self.syscom.new_struct('SOaMAllowFastActivation', name)
        self.syscom.u32('hasAllowFastActivation')
        self.syscom.u32('allowFastActivation')
        self.syscom.end_struct()

    def SOaMAntBearingForAoaCalc(self, name):
        self.syscom.new_struct('SOaMAntBearingForAoaCalc', name)
        self.syscom.u32('hasAntBearingForAoaCalc')
        self.syscom.u32('antBearingForAoaCalc')
        self.syscom.end_struct()

    def SOaMAntElementSpacing(self, name):
        self.syscom.new_struct('SOaMAntElementSpacing', name)
        self.syscom.u32('hasAntElementSpacing')
        self.syscom.u32('antElementSpacing')
        self.syscom.end_struct()

    def SOaMDlSrbCqiOffset(self, name):
        self.syscom.new_struct('SOaMDlSrbCqiOffset', name)
        self.syscom.u32('hasDlSrbCqiOffset')
        self.syscom.i32('dlSrbCqiOffset')
        self.syscom.end_struct()

    def SOaMDlTargetBler(self, name):
        self.syscom.new_struct('SOaMDlTargetBler', name)
        self.syscom.u32('hasDlTargetBler')
        self.syscom.u32('dlTargetBler')
        self.syscom.end_struct()

    def SOaMDlsOldtcTarget(self, name):
        self.syscom.new_struct('SOaMDlsOldtcTarget', name)
        self.syscom.u32('hasDlsOldtcTarget')
        self.syscom.u32('dlsOldtcTarget')
        self.syscom.end_struct()

    def SOaMEUlLaAtbPeriod(self, name):
        self.syscom.new_struct('SOaMEUlLaAtbPeriod', name)
        self.syscom.u32('hasEUlLaAtbPeriod')
        self.syscom.u32('eUlLaAtbPeriod')
        self.syscom.end_struct()

    def SOaMEUlLaBlerAveWin(self, name):
        self.syscom.new_struct('SOaMEUlLaBlerAveWin', name)
        self.syscom.u32('hasEUlLaBlerAveWin')
        self.syscom.u32('eUlLaBlerAveWin')
        self.syscom.end_struct()

    def SOaMEUlLaDeltaMcs(self, name):
        self.syscom.new_struct('SOaMEUlLaDeltaMcs', name)
        self.syscom.u32('hasEUlLaDeltaMcs')
        self.syscom.u32('eUlLaDeltaMcs')
        self.syscom.end_struct()

    def SOaMEUlLaLowMcsThr(self, name):
        self.syscom.new_struct('SOaMEUlLaLowMcsThr', name)
        self.syscom.u32('hasEUlLaLowMcsThr')
        self.syscom.u32('eUlLaLowMcsThr')
        self.syscom.end_struct()

    def SOaMEUlLaLowPrbThr(self, name):
        self.syscom.new_struct('SOaMEUlLaLowPrbThr', name)
        self.syscom.u32('hasEUlLaLowPrbThr')
        self.syscom.u32('eUlLaLowPrbThr')
        self.syscom.end_struct()

    def SOaMEUlLaPrbIncDecFactor(self, name):
        self.syscom.new_struct('SOaMEUlLaPrbIncDecFactor', name)
        self.syscom.u32('hasEUlLaPrbIncDecFactor')
        self.syscom.u32('eUlLaPrbIncDecFactor')
        self.syscom.end_struct()

    def SOaMFUlLAAtbTrigThr(self, name):
        self.syscom.new_struct('SOaMFUlLAAtbTrigThr', name)
        self.syscom.u32('hasFUlLAAtbTrigThr')
        self.syscom.i32('fUlLAAtbTrigThr')
        self.syscom.end_struct()

    def SOaMMimoClConfig(self, name):
        self.syscom.new_struct('SOaMMimoClConfig', name)
        self.syscom.u32('mimoClCqiThD')
        self.syscom.u32('mimoClCqiThU')
        self.syscom.u32('mimoClRiThD')
        self.syscom.u32('mimoClRiThU')
        self.syscom.end_struct()

    def SOaMMimoOlConfig(self, name):
        self.syscom.new_struct('SOaMMimoOlConfig', name)
        self.syscom.u32('mimoOlCqiThD')
        self.syscom.u32('mimoOlCqiThU')
        self.syscom.u32('mimoOlRiThD')
        self.syscom.u32('mimoOlRiThU')
        self.syscom.end_struct()

    def SOaMPdcchCqiShift(self, name):
        self.syscom.new_struct('SOaMPdcchCqiShift', name)
        self.syscom.u32('hasPdcchCqiShift')
        self.syscom.i32('pdcchCqiShift')
        self.syscom.end_struct()

    def SOaMPdcchHarqTargetBler(self, name):
        self.syscom.new_struct('SOaMPdcchHarqTargetBler', name)
        self.syscom.u32('hasPdcchHarqTargetBler')
        self.syscom.u32('pdcchHarqTargetBler')
        self.syscom.end_struct()

    def SOaMPdcchLoadLevel(self, name):
        self.syscom.new_struct('SOaMPdcchLoadLevel', name)
        self.syscom.u32('hasPdcchLoadLevel')
        self.syscom.u32('pdcchLoadLevel')
        self.syscom.end_struct()

    def SOaMPdcchLoadPsdOffset(self, name):
        self.syscom.new_struct('SOaMPdcchLoadPsdOffset', name)
        self.syscom.u32('hasPdcchLoadPsdOffset')
        self.syscom.i32('pdcchLoadPsdOffset')
        self.syscom.end_struct()

    def SOaMPrsConfigurationIndex(self, name):
        self.syscom.new_struct('SOaMPrsConfigurationIndex', name)
        self.syscom.u32('hasPrsConfigurationIndex')
        self.syscom.u32('prsConfigurationIndex')
        self.syscom.end_struct()

    def SOaMPrsNumDlFrames(self, name):
        self.syscom.new_struct('SOaMPrsNumDlFrames', name)
        self.syscom.u32('hasPrsNumDlFrames')
        self.syscom.u32('prsNumDlFrames')
        self.syscom.end_struct()

    def SOaMRcAmbrMgnDl(self, name):
        self.syscom.new_struct('SOaMRcAmbrMgnDl', name)
        self.syscom.u32('hasRcAmbrMgnDl')
        self.syscom.u32('rcAmbrMgnDl')
        self.syscom.end_struct()

    def SOaMRcAmbrMgnUl(self, name):
        self.syscom.new_struct('SOaMRcAmbrMgnUl', name)
        self.syscom.u32('hasRcAmbrMgnUl')
        self.syscom.u32('rcAmbrMgnUl')
        self.syscom.end_struct()

    def SOaMRedBwMaxRbDl(self, name):
        self.syscom.new_struct('SOaMRedBwMaxRbDl', name)
        self.syscom.u32('hasRedBwMaxRbDl')
        self.syscom.u32('redBwMaxRbDl')
        self.syscom.end_struct()

    def SOaMRedBwRbUlConfig(self, name):
        self.syscom.new_struct('SOaMRedBwRbUlConfig', name)
        self.syscom.u32('redBwMaxRbUl')
        self.syscom.u32('redBwMinRbUl')
        self.syscom.end_struct()

    def SOaMRipAlarmingConfig(self, name):
        self.syscom.new_struct('SOaMRipAlarmingConfig', name)
        self.syscom.u32('actRIPAlarming')
        self.syscom.u32('alarmThresholdCrossingTime')
        self.syscom.i32('alarmThresholdULSF')
        self.syscom.i32('alarmThresholdSpecialSFTdd')
        self.syscom.end_struct()

    def SOaMSrsPwrOffset(self, name):
        self.syscom.new_struct('SOaMSrsPwrOffset', name)
        self.syscom.u32('hasSrsPwrOffset')
        self.syscom.u32('srsPwrOffset')
        self.syscom.end_struct()

    def SOaMSuperCellParSet(self, name):
        self.syscom.new_struct('SOaMSuperCellParSet', name)
        self.syscom.u32('candSubCellUlSinrOffset')
        self.syscom.u32('remCandSubCellUlSinrHys')
        self.syscom.u32('repCandSubCellUlSinrHys')
        self.syscom.u32('subCellSwitchUlSinrHys')
        self.syscom.u32('subCellUlSinrAvgT')
        self.syscom.end_struct()

    def SOaMTmSwitchThresholdDef(self, name):
        self.syscom.new_struct('SOaMTmSwitchThresholdDef', name)
        self.syscom.u32('tm3to7CqiTh')
        self.syscom.u32('tm3to8CqiTh')
        self.syscom.u32('tm3to9CqiTh')
        self.syscom.u32('tm7to3CqiTh')
        self.syscom.u32('tm8to3CqiTh')
        self.syscom.u32('tm9to3CqiTh')
        self.syscom.end_struct()

    def SOaMTtiBundlingBlerTarget(self, name):
        self.syscom.new_struct('SOaMTtiBundlingBlerTarget', name)
        self.syscom.u32('hasTtiBundlingBlerTarget')
        self.syscom.u32('ttiBundlingBlerTarget')
        self.syscom.end_struct()

    def SOaMTtiBundlingBlerThreshold(self, name):
        self.syscom.new_struct('SOaMTtiBundlingBlerThreshold', name)
        self.syscom.u32('hasTtiBundlingBlerThreshold')
        self.syscom.u32('ttiBundlingBlerThreshold')
        self.syscom.end_struct()

    def SOaMTtiBundlingSinrThreshold(self, name):
        self.syscom.new_struct('SOaMTtiBundlingSinrThreshold', name)
        self.syscom.u32('hasTtiBundlingSinrThreshold')
        self.syscom.i32('ttiBundlingSinrThreshold')
        self.syscom.end_struct()

    def SOaMUciOnlyMaxCodeRate(self, name):
        self.syscom.new_struct('SOaMUciOnlyMaxCodeRate', name)
        self.syscom.u32('hasUciOnlyMaxCodeRate')
        self.syscom.u32('uciOnlyMaxCodeRate')
        self.syscom.end_struct()

    def SOaMUlMuMimoParaSet(self, name):
        self.syscom.new_struct('SOaMUlMuMimoParaSet', name)
        self.syscom.u32('ulMuMimoOrthThreshold')
        self.syscom.i32('ulMuMimoSinrThreshold')
        self.syscom.end_struct()

    def SOaMUlpcPucchConfig(self, name):
        self.syscom.new_struct('SOaMUlpcPucchConfig', name)
        self.syscom.i32('ulpcLowlevCch')
        self.syscom.i32('ulpcLowqualCch')
        self.syscom.i32('ulpcUplevCch')
        self.syscom.i32('ulpcUpqualCch')
        self.syscom.end_struct()

    def SOaMUlpcPuschConfig(self, name):
        self.syscom.new_struct('SOaMUlpcPuschConfig', name)
        self.syscom.i32('ulpcLowlevSch')
        self.syscom.i32('ulpcLowqualSch')
        self.syscom.i32('ulpcUplevSch')
        self.syscom.i32('ulpcUpqualSch')
        self.syscom.end_struct()

    def SOaMUlpcReadPeriod(self, name):
        self.syscom.new_struct('SOaMUlpcReadPeriod', name)
        self.syscom.u32('hasUlpcReadPeriod')
        self.syscom.u32('ulpcReadPeriod')
        self.syscom.end_struct()

    def SOaMUlpcRssiMaxIAw(self, name):
        self.syscom.new_struct('SOaMUlpcRssiMaxIAw', name)
        self.syscom.u32('hasUlpcRssiMaxIAw')
        self.syscom.i32('ulpcRssiMaxIAw')
        self.syscom.end_struct()

    def SOaMUlsPuschMask(self, name):
        self.syscom.new_struct('SOaMUlsPuschMask', name)
        self.syscom.u32('ulsPuschMaskLength')
        self.syscom.u32('ulsPuschMaskStart')
        self.syscom.end_struct()

    def SOtherSCellUeParams(self, name):
        self.syscom.new_struct('SOtherSCellUeParams', name)
        self.syscom.u32('numOfOtherScells')
        self.syscom.array('3', 'SOtherScellData', 'otherScellData')
        self.syscom.end_struct()

    def SOtherScellData(self, name):
        self.syscom.new_struct('SOtherScellData', name)
        self.syscom.u32('sCellId')
        self.syscom.u32('sCellEnbId')
        self.syscom.u32('hasCsiParamsScell')
        self.SCaCqiParams('csiParamsScell')
        self.syscom.u16('ueIndexInServingCell')
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('isUlCaSupported')
        self.syscom.u32('sCellTransmMode')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.end_struct()

    def SP0PrachInfoDcm(self, name):
        self.syscom.new_struct('SP0PrachInfoDcm', name)
        self.syscom.u16('p0Prach')
        self.syscom.u16('interferencePrachUp')
        self.syscom.u16('interferencePrachDown')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SP0PucchInfoDcm(self, name):
        self.syscom.new_struct('SP0PucchInfoDcm', name)
        self.syscom.u16('p0PucchRef')
        self.syscom.u16('tInterferenceUp')
        self.syscom.u16('tInterferenceDown')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SP0PuschInfoDcm(self, name):
        self.syscom.new_struct('SP0PuschInfoDcm', name)
        self.syscom.u16('p0PuschRef')
        self.syscom.u16('tInterferenceUp')
        self.syscom.u16('tInterferenceDown')
        self.syscom.end_struct()

    def SPCellConfigParameters(self, name):
        self.syscom.new_struct('SPCellConfigParameters', name)
        self.syscom.u32('lnCellIdPcell')
        self.syscom.u32('enbId')
        self.syscom.u32('ulChBw')
        self.syscom.u32('dlChBw')
        self.syscom.u8('disableSCellPDCCHOlLa')
        self.syscom.u8('isPcellTddTechnology')
        self.syscom.u16('reserved')
        self.syscom.array('4', 'u32', 'sharePerResourceGroup')
        self.syscom.u32('numOfOtherSCellConfigParameters')
        self.syscom.array('11', 'SSCellConfigParameters', 'otherSCellConfigParameters')
        self.syscom.u32('enableSRS')
        self.syscom.u32('srsSubfrConf')
        self.syscom.u32('anSrsSimulTx')
        self.syscom.u32('nPucchF3Prbs')
        self.syscom.u32('beamformingInScell')
        self.syscom.end_struct()

    def SPCellParams(self, name):
        self.syscom.new_struct('SPCellParams', name)
        self.syscom.u32('pCellId')
        self.syscom.u32('pCellEnbId')
        self.syscom.end_struct()

    def SPCellUeParams(self, name):
        self.syscom.new_struct('SPCellUeParams', name)
        self.syscom.u16('ueIndexPcell')
        self.syscom.u16('paddingUeIndexPcell')
        self.syscom.u32('uecAddress')
        self.syscom.u32('cookie')
        self.syscom.u32('hasSrsEnable')
        self.syscom.u32('srsEnable')
        self.syscom.u32('hasSoundingRsUlConfigDedicated')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.SCaCqiParams('csiParamsPcell')
        self.syscom.u32('transmModePcell')
        self.SPuschControlOffsets('controlOffsets')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.end_struct()

    def SPMQAPProfile(self, name):
        self.syscom.new_struct('SPMQAPProfile', name)
        self.syscom.u32('cfgQCI')
        self.syscom.u32('hasCfgARP')
        self.syscom.u32('cfgARP')
        self.syscom.u32('pmQAPId')
        self.syscom.end_struct()

    def SPMQAPProfiles(self, name):
        self.syscom.new_struct('SPMQAPProfiles', name)
        self.syscom.u32('numOfPmqapProfiles')
        self.syscom.array('20', 'SPMQAPProfile', 'pmqapProfiles')
        self.syscom.end_struct()

    def SPRSInfoParams(self, name):
        self.syscom.new_struct('SPRSInfoParams', name)
        self.syscom.u32('actOtdoa')
        self.SOaMPrsConfigurationIndex('prsConfigurationIndex')
        self.SOaMPrsNumDlFrames('prsNumDlFrames')
        self.syscom.end_struct()

    def SPSrsOffsetInfoDcm(self, name):
        self.syscom.new_struct('SPSrsOffsetInfoDcm', name)
        self.syscom.u32('srsBandwidth')
        self.syscom.u16('pSrsOffsetRef')
        self.syscom.u16('tSirSoundingRef')
        self.syscom.u16('pathlossUp')
        self.syscom.u16('pathlossDown')
        self.syscom.end_struct()

    def SPacketSendingMode(self, name):
        self.syscom.new_struct('SPacketSendingMode', name)
        self.syscom.u32('continuous')
        self.syscom.u32('numberOfPackets')
        self.syscom.u32('duration')
        self.syscom.u32('sendMode')
        self.syscom.end_struct()

    def SPcellSwapParameters(self, name):
        self.syscom.new_struct('SPcellSwapParameters', name)
        self.syscom.i32('ulSinrLowThreshold')
        self.syscom.u32('scellStateForPcellSwap')
        self.syscom.u32('enableVoLteUePcellSwap')
        self.syscom.end_struct()

    def SPdcchParams(self, name):
        self.syscom.new_struct('SPdcchParams', name)
        self.syscom.u32('pdcchAggSib')
        self.syscom.u32('pdcchAggRaresp')
        self.syscom.u32('pdcchAggPaging')
        self.syscom.u32('pdcchAggPreamb')
        self.syscom.u32('pdcchAggMsg4')
        self.syscom.u32('enableAmcPdcch')
        self.syscom.u32('pdcchAggDefUe')
        self.syscom.u32('pdcchCqiAvg')
        self.SOaMPdcchCqiShift('pdcchCqiShift')
        self.syscom.u32('pdcchOlComp')
        self.syscom.u32('pdcchClComp')
        self.syscom.u32('pdcchCqiHist')
        self.syscom.u32('enableLowAgg')
        self.syscom.u32('pdcchLowAggTh')
        self.syscom.u32('pdcchAlpha')
        self.syscom.u32('pdcchUlDlBal')
        self.syscom.array('20', 'u32', 'pdcchUlDlPrio')
        self.syscom.u32('enablePcPdcch')
        self.syscom.u32('pdcchPcBoost')
        self.syscom.u32('pdcchPcRed')
        self.syscom.u32('pdcchPcReloc')
        self.syscom.u32('actLdPdcch')
        self.syscom.u32('hasActPdcchLoadGen')
        self.syscom.u32('actPdcchLoadGen')
        self.SOaMPdcchLoadLevel('pdcchLoadLevel')
        self.SOaMPdcchLoadPsdOffset('pdcchLoadPsdOffset')
        self.syscom.end_struct()

    def SPdcchSendReqBuffer(self, name):
        self.syscom.new_struct('SPdcchSendReqBuffer', name)
        self.syscom.i16('txPowerPcfich')
        self.syscom.array('4', 'i16', 'pdcchSymPowerCorr')
        self.syscom.u8('cfiAndFlags')
        self.syscom.u8('numOfDci')
        self.syscom.array('1', 'SDciInfo', 'dciInfo')
        self.syscom.end_struct()

    def SPdcchTpcParamsDlDcm(self, name):
        self.syscom.new_struct('SPdcchTpcParamsDlDcm', name)
        self.syscom.array('10', 'u16', 'txPowerPdcchRef0')
        self.syscom.array('10', 'u16', 'txPowerPdcchRef1')
        self.syscom.array('10', 'u16', 'txPowerPdcchRef2')
        self.syscom.array('10', 'u16', 'txPowerPdcchRef3')
        self.syscom.array('10', 'u16', 'cqiDefaultPdcch0')
        self.syscom.array('10', 'u16', 'cqiDefaultPdcch1')
        self.syscom.array('10', 'u16', 'cqiDefaultPdcch2')
        self.syscom.array('10', 'u16', 'cqiDefaultPdcch3')
        self.syscom.array('10', 'u16', 'pdcchFormat0ThTable')
        self.syscom.array('10', 'u16', 'pdcchFormat1ThTable')
        self.syscom.array('10', 'u16', 'pdcchFormat2ThTable')
        self.syscom.u32('txPowerAdjUlEnable')
        self.syscom.u32('numOfOfdmaSymbolsMode')
        self.syscom.u16('txPowerOfRachRespPdcch')
        self.syscom.u16('txPowerOfPchPdcch')
        self.syscom.u16('txPowerOfDbchPdcch')
        self.syscom.u16('maxTxPowerOfPdcch')
        self.syscom.u16('minTxPowerOfPdcch')
        self.syscom.u16('txPowerAdjStepSize')
        self.syscom.u16('dlSchPdcchTargetBler')
        self.syscom.u16('ulSchPdcchTargetBler')
        self.syscom.u16('txPowerAdjDlEnable')
        self.syscom.u16('numOfOfdmaSymbolsDbchOffset')
        self.syscom.u16('numOfOfdmaSymbolsPchOffset')
        self.syscom.u16('numOfOfdmaSymbolsRachRespOffset')
        self.syscom.u16('pdcchFormatDbch')
        self.syscom.u16('pdcchFormatPch')
        self.syscom.u16('pdcchFormatTpcPucch')
        self.syscom.u16('pdcchFormatTpcPusch')
        self.syscom.u16('pdcchFormatRachResp')
        self.syscom.u16('offsetPdcchMax')
        self.syscom.u16('offsetPdcchMin')
        self.syscom.u16('thCfi1to2')
        self.syscom.u16('thCfi2to3')
        self.syscom.u16('pdcchFormatMch')
        self.syscom.u16('txPowerOfMchPdcch')
        self.syscom.u16('txPowerOfTpcPucchPdcch')
        self.syscom.u16('txPowerOfTpcPuschPdcch')
        self.syscom.u16('pdcchResourceAmount')
        self.syscom.end_struct()

    def SPdcpRbInfoBearerSetup(self, name):
        self.syscom.new_struct('SPdcpRbInfoBearerSetup', name)
        self.syscom.u32('tDiscard')
        self.syscom.u32('pdcpSnLength')
        self.syscom.u32('rohcEnable')
        self.syscom.array('3', 'u32', 'rohcProfileList')
        self.syscom.u32('rohcMaxCidDl')
        self.syscom.u32('rohcMaxCidUl')
        self.syscom.end_struct()

    def SPdcpRbInfoUserSetup(self, name):
        self.syscom.new_struct('SPdcpRbInfoUserSetup', name)
        self.syscom.u32('tDiscard')
        self.syscom.u32('pdcpSnLength')
        self.syscom.u32('statusReportReq')
        self.syscom.u32('rohcEnable')
        self.syscom.array('3', 'u32', 'rohcProfileList')
        self.syscom.u32('rohcMaxCidDl')
        self.syscom.u32('rohcMaxCidUl')
        self.syscom.end_struct()

    def SPdschResources(self, name):
        self.syscom.new_struct('SPdschResources', name)
        self.syscom.u32('numPrbs')
        self.syscom.array('4', 'u32', 'prbMap0')
        self.syscom.array('4', 'u32', 'prbMap1')
        self.syscom.end_struct()

    def SPduMuxDataReq(self, name):
        self.syscom.new_struct('SPduMuxDataReq', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('macId')
        self.syscom.i32('txPower')
        self.syscom.u8('spatialMode')
        self.syscom.u8('numOfLayers')
        self.syscom.u8('codebookIndex')
        self.syscom.u8('paddingCodebookIndex')
        self.syscom.u32('nIr')
        self.SPdschResources('resources')
        self.syscom.u8('mimoIndicator')
        self.syscom.u8('servingCellIndex')
        self.syscom.u16('paddingServingCellIndex')
        self.syscom.u32('lnCellIdServCell')
        self.syscom.u32('enbIdServCell')
        self.syscom.u8('reqType')
        self.syscom.u8('hasDlBfTbFormat')
        self.syscom.u16('paddingHasDlBfTbFormat')
        self.SDlBfTbFormat('dlBfTbFormat')
        self.syscom.u32('tbFlags')
        self.syscom.array('2', 'SDlSchPduMuxCwAttributes', 'cwAttributes')
        self.syscom.end_struct()

    def SPduMuxDataResultEntry(self, name):
        self.syscom.new_struct('SPduMuxDataResultEntry', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u32('cw0')
        self.syscom.u32('cw1')
        self.syscom.array('2', 'u8', 'harqIds')
        self.syscom.u16('paddingHarqIds')
        self.syscom.u32('tbSizeCW0')
        self.syscom.u32('tbSizeCW1')
        self.syscom.end_struct()

    def SPeriodicGrantInfoDcm(self, name):
        self.syscom.new_struct('SPeriodicGrantInfoDcm', name)
        self.syscom.u32('periodicGrantTimer')
        self.syscom.u16('sizePeriodicGrant')
        self.syscom.u16('flagTbPeriodicGrant')
        self.syscom.u16('numTxCountUl')
        self.syscom.u16('numPduUl')
        self.syscom.u16('rbPeriodicGrant')
        self.syscom.u16('tfPeriodicGrant')
        self.syscom.u16('rbPeriodicGrantTb')
        self.syscom.u16('tfPeriodicGrantTb')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.end_struct()

    def SPhichInfo(self, name):
        self.syscom.new_struct('SPhichInfo', name)
        self.syscom.u8('harqAckIndicatorAndPhichIndex')
        self.syscom.u8('groupIndex')
        self.syscom.i16('txPower')
        self.syscom.end_struct()

    def SPhichParams(self, name):
        self.syscom.new_struct('SPhichParams', name)
        self.syscom.u32('phichRes')
        self.syscom.u32('phichDur')
        self.syscom.end_struct()

    def SPhichSendReqBuffer(self, name):
        self.syscom.new_struct('SPhichSendReqBuffer', name)
        self.syscom.u32('numOfPhichInfo')
        self.syscom.array('numOfPhichInfo', 'SPhichInfo', 'phichInfo')
        self.syscom.end_struct()

    def SPhichTpcParamsDlDcm(self, name):
        self.syscom.new_struct('SPhichTpcParamsDlDcm', name)
        self.syscom.u32('txPowerAdjPhichEnable')
        self.syscom.u16('refTxPowerOfPhichNormal')
        self.syscom.u16('cqiDefaultPhichNormal')
        self.syscom.u16('refTxPowerOfPhichExtended')
        self.syscom.u16('cqiDefaultPhichExtended')
        self.syscom.u16('offsetPhich0')
        self.syscom.u16('offsetPhich1')
        self.syscom.u16('offsetPhich2')
        self.syscom.u16('cqiAdjustPhich')
        self.syscom.end_struct()

    def SPhyDataHeader(self, name):
        self.syscom.new_struct('SPhyDataHeader', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('frameNumber')
        self.syscom.u32('subFrameNumber')
        self.syscom.end_struct()

    def SPlmnId(self, name):
        self.syscom.new_struct('SPlmnId', name)
        self.syscom.u32('mncLength')
        self.syscom.u32('mnc')
        self.syscom.u32('mcc')
        self.syscom.end_struct()

    def SPmCounter(self, name):
        self.syscom.new_struct('SPmCounter', name)
        self.syscom.u32('counterId')
        self.syscom.u32('counterValue')
        self.syscom.end_struct()

    def SPmGeneralObject(self, name):
        self.syscom.new_struct('SPmGeneralObject', name)
        self.syscom.u32('objectClass')
        self.SBrowserObjectData('objectData')
        self.syscom.u32('moHasChild')
        self.syscom.u32('nbrOfMeasTypes')
        self.syscom.array('nbrOfMeasTypes', 'SStatisticalMeasurementType', 'measTypes')
        self.syscom.end_struct()

    def SPoolConf(self, name):
        self.syscom.new_struct('SPoolConf', name)
        self.syscom.u32('poolId')
        self.syscom.u32('poolLayer')
        self.syscom.u32('poolType')
        self.syscom.u32('numOfDeployableUnits')
        self.syscom.array('16', 'SDeployableUnit', 'deployableUnits')
        self.syscom.end_struct()

    def SPrachPreamble(self, name):
        self.syscom.new_struct('SPrachPreamble', name)
        self.syscom.u32('prachIndex')
        self.syscom.real32('signalPower')
        self.syscom.u32('frequencyOffsetPrach')
        self.syscom.u16('absoluteTimingAdvance')
        self.syscom.u16('timingAdvanceStrongestPath')
        self.syscom.end_struct()

    def SPrachTpcParamsUlDcm(self, name):
        self.syscom.new_struct('SPrachTpcParamsUlDcm', name)
        self.syscom.array('8', 'SP0PrachInfoDcm', 'p0PrachInfoDcm')
        self.syscom.u32('averTimePrachI')
        self.syscom.u16('tttP0PrachTh')
        self.syscom.u16('deltaMsg2')
        self.syscom.u16('deltaPowerRamping')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SProtocolStackProfile(self, name):
        self.syscom.new_struct('SProtocolStackProfile', name)
        self.syscom.u32('model')
        self.syscom.end_struct()

    def SPucchConfiguration(self, name):
        self.syscom.new_struct('SPucchConfiguration', name)
        self.syscom.u32('deltaPucchShift')
        self.syscom.u32('pucchNAnCs')
        self.syscom.u32('nCqiRb')
        self.syscom.u32('n1PucchAn')
        self.syscom.u32('firstPucchF3Prb')
        self.syscom.u32('nPucchF3Prbs')
        self.syscom.u32('blankedPucch')
        self.syscom.u32('nPucchPrbs')
        self.syscom.end_struct()

    def SPucchTpcParamsDlDcm(self, name):
        self.syscom.new_struct('SPucchTpcParamsDlDcm', name)
        self.syscom.array('8', 'SP0PucchInfoDcm', 'p0PucchInfoTable')
        self.syscom.u32('averTimePucchAvgTpcS')
        self.syscom.u32('averTimePucchAvgTpcI')
        self.syscom.u32('averTimePucchInstTpcI')
        self.syscom.u32('averTimePucchI')
        self.syscom.u16('tSirPucchInst')
        self.syscom.u16('tSirPucchAver')
        self.syscom.u16('pucchTpcOffset')
        self.syscom.u16('tttP0PucchTh')
        self.syscom.u16('flagPucchTpcCommandReset')
        self.syscom.u16('nNoCqiRb')
        self.syscom.end_struct()

    def SPuschControlOffsets(self, name):
        self.syscom.new_struct('SPuschControlOffsets', name)
        self.syscom.u32('puschAckOffI')
        self.syscom.u32('puschRiOffI')
        self.syscom.u32('puschCqiOffI')
        self.syscom.end_struct()

    def SPuschFreqHoppingInformationDcm(self, name):
        self.syscom.new_struct('SPuschFreqHoppingInformationDcm', name)
        self.syscom.u32('hoppingModeRachMsg3')
        self.syscom.u32('hoppingPatternRachMsg3')
        self.syscom.u32('hoppingModeUlSchDynamicHighFd')
        self.syscom.u32('hoppingModeUlSchDynamicLowFd')
        self.syscom.u32('hoppingPatternUlSchDynamic')
        self.syscom.u32('hoppingModeUlSchSPS0')
        self.syscom.u32('hoppingModeUlSchSPS1')
        self.syscom.u32('hoppingPatternUlSchSPS0')
        self.syscom.u32('hoppingPatternUlSchSPS1')
        self.syscom.u16('puschHoppingOffset')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SPuschHoppingInformation(self, name):
        self.syscom.new_struct('SPuschHoppingInformation', name)
        self.syscom.u32('hopBwPusch')
        self.syscom.u32('hopModePusch')
        self.syscom.u32('hopTypePusch')
        self.syscom.u32('TPuschHoppingEnable')
        self.syscom.u32('puschHopOffset')
        self.syscom.end_struct()

    def SPuschReceiveMeasResp(self, name):
        self.syscom.new_struct('SPuschReceiveMeasResp', name)
        self.syscom.u32('numOfSubcell1Rssi')
        self.syscom.u32('numOfUePuschResp')
        self.syscom.array('numOfUePuschResp', 'SPuschUeReceiveMeasResp', 'uePuschResp')
        self.syscom.end_struct()

    def SPuschReceiveReq(self, name):
        self.syscom.new_struct('SPuschReceiveReq', name)
        self.syscom.u32('rfLoopFlag')
        self.syscom.u32('numOfDelayedUe')
        self.syscom.array('32', 'u16', 'delayedUe')
        self.syscom.u32('numOfCCAddresses')
        self.syscom.array('13', 'SCCAddresses', 'ccAddresses')
        self.syscom.u32('numOfUeReq')
        self.syscom.array('numOfUeReq', 'SPuschUeReceiveReq', 'ueReq')
        self.syscom.end_struct()

    def SPuschResources(self, name):
        self.syscom.new_struct('SPuschResources', name)
        self.syscom.array('2', 'u8', 'firstPrb')
        self.syscom.array('2', 'u8', 'numPrbs')
        self.syscom.u8('simultanousSrs')
        self.syscom.u8('initialNumPrbs')
        self.syscom.u8('initialSimultanousSrs')
        self.syscom.u8('firstPrbIn2ndSlot')
        self.syscom.u8('ueContextFlags')
        self.syscom.u8('explicitPadding2')
        self.syscom.u16('explicitPadding3')
        self.syscom.end_struct()

    def SPuschTpcParamsUlDcm(self, name):
        self.syscom.new_struct('SPuschTpcParamsUlDcm', name)
        self.syscom.array('8', 'SP0PuschInfoDcm', 'p0PuschInfoTable')
        self.syscom.u32('averTimePuschI')
        self.syscom.u32('averTimeItpcRefI')
        self.syscom.u16('tttP0PuschTh')
        self.syscom.u16('flagPuschTpcCommandReset')
        self.syscom.u16('tTPCProhibitPlus')
        self.syscom.u16('tTPCProhibitMinus')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('reserved3')
        self.syscom.u16('reserved4')
        self.syscom.end_struct()

    def SPuschUeReceiveMeasResp(self, name):
        self.syscom.new_struct('SPuschUeReceiveMeasResp', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u32('status')
        self.syscom.u32('specificCause')
        self.syscom.real32('rssi')
        self.syscom.real32('interferencePower')
        self.syscom.u32('frequencyOffsetPusch')
        self.syscom.i32('phiReal')
        self.syscom.i32('phiImag')
        self.syscom.i16('postCombSinr')
        self.syscom.u8('ulCompUsage')
        self.syscom.u8('ulReliabilty')
        self.syscom.u8('subCellId')
        self.syscom.u8('explicitPadding1')
        self.syscom.u16('explicitPadding2')
        self.syscom.end_struct()

    def SPuschUeReceiveReq(self, name):
        self.syscom.new_struct('SPuschUeReceiveReq', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u32('paramNdmrs')
        self.syscom.u8('harqAckType')
        self.syscom.u8('ulCaPuschRespForwardingFlag')
        self.syscom.u16('ueContextCrnti')
        self.syscom.u8('servingSubCellId')
        self.syscom.u8('candidateSubCellId')
        self.syscom.u8('bundlingMode')
        self.syscom.u8('bundleIndex')
        self.SPuschResources('resources')
        self.SPuschControlOffsets('controlOffsets')
        self.SUlTbFormat('tbFormat')
        self.syscom.u32('tbSize')
        self.syscom.u32('tbPointer')
        self.SFrequencyOffsetInfo('frequencyOffsetInfo')
        self.SFrequencyOffsetInfo('frequencyOffsetInfoCandiSubCell')
        self.syscom.u8('numOfDlCcs')
        self.syscom.u8('riCqiIndicator')
        self.syscom.array('4', 'u8', 'harqProcessesInfoPacked')
        self.syscom.array('4', 'u8', 'addrIndexAn')
        self.syscom.array('4', 'u16', 'ueIndexAn')
        self.syscom.u16('harqAckSize')
        self.syscom.u16('tbSchedInfo')
        self.syscom.u8('numOfCsis')
        self.syscom.array('4', 'inner_list', 'cqiSize', '3', 'u8')
        self.syscom.array('3', 'u8', 'cqiRepType')
        self.syscom.array('3', 'u8', 'riSize')
        self.syscom.u8('spsTransmission')
        self.syscom.array('3', 'u16', 'ueIndexCqi')
        self.syscom.array('3', 'u8', 'addrIndexCqi')
        self.syscom.u8('isSpsExplicitReleaseTransientPhase')
        self.syscom.u16('padding3')
        self.syscom.u16('pairedUeIndex')
        self.syscom.u8('mimoLayer')
        self.syscom.u8('softBitCoMpUe')
        self.syscom.u16('ueIndexL2')
        self.syscom.u32('puschReceiveRespUAddress')
        self.syscom.u32('numOfDlHarqSubframesPacked')
        self.syscom.end_struct()

    def SPuschUeResp(self, name):
        self.syscom.new_struct('SPuschUeResp', name)
        self.syscom.u32('lnCelId')
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u8('harqProcessNumber')
        self.syscom.u8('crcResult')
        self.syscom.u8('ulReliability')
        self.syscom.u8('numOfAllocPrbs')
        self.syscom.u32('tbSize')
        self.syscom.u32('tbPointer')
        self.syscom.u8('ueContextFlags')
        self.syscom.u8('txCount')
        self.syscom.u16('ueContextCrnti')
        self.syscom.u8('ulCaPuschRespForwardingFlag')
        self.syscom.u8('padding1')
        self.syscom.u16('padding2')
        self.syscom.real32('rssi')
        self.syscom.end_struct()

    def SR10n1PucchAnCsElement(self, name):
        self.syscom.new_struct('SR10n1PucchAnCsElement', name)
        self.syscom.array('4', 'u32', 'pucchResourceIndex')
        self.syscom.end_struct()

    def SR10n3PucchElement(self, name):
        self.syscom.new_struct('SR10n3PucchElement', name)
        self.syscom.array('4', 'u32', 'pucchResourceIndex')
        self.syscom.end_struct()

    def SRaMsg3ThrCntParameters(self, name):
        self.syscom.new_struct('SRaMsg3ThrCntParameters', name)
        self.syscom.u32('discardingCellGroupId')
        self.syscom.u32('raMsg3ThrCnt')
        self.syscom.end_struct()

    def SRaMsg3ThrLowParameters(self, name):
        self.syscom.new_struct('SRaMsg3ThrLowParameters', name)
        self.syscom.u32('raMsg3ThrLow')
        self.syscom.u32('raMsg3ThrLowCnt')
        self.syscom.u32('flagCcchPriority')
        self.syscom.end_struct()

    def SRaPreambleList(self, name):
        self.syscom.new_struct('SRaPreambleList', name)
        self.syscom.u32('RAPreamble')
        self.syscom.end_struct()

    def SRaPreambleResList(self, name):
        self.syscom.new_struct('SRaPreambleResList', name)
        self.syscom.u32('RAPreamble')
        self.syscom.u32('crnti')
        self.syscom.u32('status')
        self.syscom.end_struct()

    def SRachParams(self, name):
        self.syscom.new_struct('SRachParams', name)
        self.syscom.u32('prachFreqOff')
        self.syscom.u32('prachConfIndex')
        self.syscom.u32('raNondedPreamb')
        self.syscom.u32('raPreambGrASize')
        self.syscom.u32('raRespWinSize')
        self.UCrntiParams('crntiParams')
        self.syscom.u32('raContResoT')
        self.syscom.u32('prachCS')
        self.syscom.u32('timerRaComp')
        self.syscom.u32('hasRaMsg3Thr')
        self.syscom.u32('raMsg3Thr')
        self.syscom.u32('hasRaMsg3ThrLowParameters')
        self.SRaMsg3ThrLowParameters('raMsg3ThrLowParameters')
        self.syscom.u32('hasRaMsg3ThrCntParameters')
        self.SRaMsg3ThrCntParameters('raMsg3ThrCntParameters')
        self.syscom.u32('hasPrachHsFlag')
        self.syscom.u32('prachHsFlag')
        self.syscom.end_struct()

    def SRadioLinkFailureParams(self, name):
        self.syscom.new_struct('SRadioLinkFailureParams', name)
        self.syscom.u32('rlpDetMaxTimeDl')
        self.syscom.u32('rlpDetMaxNoDl')
        self.syscom.u32('rlpDetEndNoDl')
        self.syscom.u32('rlpDetMaxNUl')
        self.syscom.u32('rlpDetEndNUl')
        self.syscom.end_struct()

    def SRateCappingParams(self, name):
        self.syscom.new_struct('SRateCappingParams', name)
        self.syscom.u32('rcEnableDl')
        self.SOaMRcAmbrMgnDl('rcAmbrMgnDl')
        self.syscom.u32('rcAvCstDl')
        self.syscom.u32('rcEnableUl')
        self.SOaMRcAmbrMgnUl('rcAmbrMgnUl')
        self.syscom.u32('rcAvCstUl')
        self.syscom.end_struct()

    def SRbGbrDlConfig(self, name):
        self.syscom.new_struct('SRbGbrDlConfig', name)
        self.syscom.array('2', 'u32', 'dlsGbrRlc')
        self.syscom.array('2', 'u32', 'dlsGbrMac')
        self.syscom.end_struct()

    def SRbGbrUlConfig(self, name):
        self.syscom.new_struct('SRbGbrUlConfig', name)
        self.syscom.array('2', 'u32', 'ulsGbrRlc')
        self.syscom.array('2', 'u32', 'ulsGbrMac')
        self.syscom.end_struct()

    def SRbInfo(self, name):
        self.syscom.new_struct('SRbInfo', name)
        self.syscom.u32('drbId')
        self.syscom.u32('drbType')
        self.syscom.u32('logicalChannelId')
        self.syscom.u32('logicalChannelGrId')
        self.syscom.u32('logicalChannelIndex')
        self.syscom.u32('rlcMode')
        self.SRlcUmParameters('rlcUmParameters')
        self.SRlcAmParameters('rlcAmParameters')
        self.UWmpDcmRbContainer('container')
        self.syscom.end_struct()

    def SRbInfoSCell(self, name):
        self.syscom.new_struct('SRbInfoSCell', name)
        self.syscom.u32('drbId')
        self.syscom.u32('logicalChannelId')
        self.syscom.end_struct()

    def SRbModifyInfo(self, name):
        self.syscom.new_struct('SRbModifyInfo', name)
        self.syscom.u32('drbId')
        self.syscom.u32('hasCongestionWeight')
        self.syscom.u32('congestionWeight')
        self.syscom.u32('hasQciInfo')
        self.SRbModifyQciInfo('qciInfo')
        self.syscom.u32('hasArp')
        self.syscom.u32('arp')
        self.syscom.end_struct()

    def SRbModifyQciInfo(self, name):
        self.syscom.new_struct('SRbModifyQciInfo', name)
        self.syscom.u32('schedulWeight')
        self.syscom.u32('qci')
        self.syscom.u32('hasRbNbrDlConfig')
        self.SRbNbrDlConfig('rbNbrDlConfig')
        self.syscom.u32('hasRbNbrUlConfig')
        self.SRbNbrUlConfig('rbNbrUlConfig')
        self.syscom.u32('hasRbGbrDlConfig')
        self.SRbGbrDlConfig('rbGbrDlConfig')
        self.syscom.u32('hasRbGbrUlConfig')
        self.SRbGbrUlConfig('rbGbrUlConfig')
        self.syscom.end_struct()

    def SRbNbrDlConfig(self, name):
        self.syscom.new_struct('SRbNbrDlConfig', name)
        self.syscom.u32('nbrDl')
        self.syscom.u32('dlSchedulingPriority')
        self.syscom.u32('dlsBucketSizeDuration')
        self.syscom.end_struct()

    def SRbNbrUlConfig(self, name):
        self.syscom.new_struct('SRbNbrUlConfig', name)
        self.syscom.u32('nbrUl')
        self.syscom.u32('ulSchedulingPriority')
        self.syscom.u32('ulsBucketSizeDuration')
        self.syscom.end_struct()

    def SRbRestrictionParamsDlDcm(self, name):
        self.syscom.new_struct('SRbRestrictionParamsDlDcm', name)
        self.syscom.u16('cchStartRb')
        self.syscom.u16('cchEndRb')
        self.syscom.u16('spsStartRb')
        self.syscom.u16('spsEndRb')
        self.syscom.u16('dynamicStartRb')
        self.syscom.u16('dynamicEndRb')
        self.syscom.end_struct()

    def SRbStopSchedulingInfo(self, name):
        self.syscom.new_struct('SRbStopSchedulingInfo', name)
        self.syscom.u32('drbId')
        self.syscom.u32('dataForwardingType')
        self.syscom.end_struct()

    def SRbgOffsetControlInfoDcm(self, name):
        self.syscom.new_struct('SRbgOffsetControlInfoDcm', name)
        self.syscom.array('16', 'u16', 'rbgOffsetInfoA')
        self.syscom.array('16', 'u16', 'rbgOffsetInfoB')
        self.syscom.u16('rbgOffsetHighTh')
        self.syscom.u16('rbgOffsetLowTh')
        self.syscom.end_struct()

    def SReservedAreaForCellContainer(self, name):
        self.syscom.new_struct('SReservedAreaForCellContainer', name)
        self.syscom.array('3350', 'u32', 'reservedArea')
        self.syscom.end_struct()

    def SResultCounters(self, name):
        self.syscom.new_struct('SResultCounters', name)
        self.syscom.u64('numberOfReceivedBits')
        self.syscom.u64('numberOfDefectiveBits')
        self.syscom.u64('numberOfReceivedTransmissionBlocks')
        self.syscom.u64('numberOfUnreceivedTransmissionBlocks')
        self.syscom.end_struct()

    def SRlcAmParameters(self, name):
        self.syscom.new_struct('SRlcAmParameters', name)
        self.syscom.u32('amRlcPollPdu')
        self.syscom.u32('amPollBytes')
        self.syscom.u32('amRlcTimerPollReTransmit')
        self.syscom.u32('amRlcTimerReordering')
        self.syscom.u32('amRlcTimerStatusProhibit')
        self.syscom.u32('maxRlcReTrans')
        self.syscom.end_struct()

    def SRlcLcpInfo(self, name):
        self.syscom.new_struct('SRlcLcpInfo', name)
        self.syscom.u32('umReorderingBufferSize')
        self.syscom.u32('umTransmitBufferSize')
        self.syscom.u32('bufferingTimeTh')
        self.syscom.u32('rlcDiscardTh')
        self.syscom.end_struct()

    def SRlcUmParameters(self, name):
        self.syscom.new_struct('SRlcUmParameters', name)
        self.syscom.u32('umRlcSnFieldLengthDownlink')
        self.syscom.u32('umRlcSnFieldLengthUplink')
        self.syscom.u32('umTimerReordering')
        self.syscom.end_struct()

    def SRmodSfp(self, name):
        self.syscom.new_struct('SRmodSfp', name)
        self.syscom.u16('rmod')
        self.syscom.u16('sfp')
        self.syscom.end_struct()

    def SRohcCellParameters(self, name):
        self.syscom.new_struct('SRohcCellParameters', name)
        self.syscom.u32('rohcFullHdCount')
        self.syscom.u32('rohcHdRefreshPeriod')
        self.syscom.u32('rohcK1')
        self.syscom.u32('rohcN1')
        self.syscom.u32('rohcK2')
        self.syscom.u32('rohcN2')
        self.syscom.u32('rohcHdDecomOmodeEnable')
        self.syscom.end_struct()

    def SRouteDef(self, name):
        self.syscom.new_struct('SRouteDef', name)
        self.syscom.u16('dlProcessCpid')
        self.syscom.u16('padding')
        self.syscom.u32('dspIpOrSicad')
        self.syscom.u32('macDataSimSicad')
        self.syscom.u32('fsm2Port')
        self.syscom.end_struct()

    def SRp3Link(self, name):
        self.syscom.new_struct('SRp3Link', name)
        self.syscom.u32('linkOrderNumber')
        self.syscom.u32('linkRate')
        self.syscom.u32('pi')
        self.syscom.u32('delta')
        self.SMultiplexingtable('multiplexingTable')
        self.SSchedulingTable('schedulingTable')
        self.syscom.end_struct()

    def SSCellConfigParameters(self, name):
        self.syscom.new_struct('SSCellConfigParameters', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('enbId')
        self.syscom.u32('ulChBw')
        self.syscom.u32('dlChBw')
        self.syscom.u32('dlMimoMode')
        self.syscom.u32('hasRcAmbrMgnDl')
        self.syscom.u32('rcAmbrMgnDl')
        self.syscom.array('4', 'u32', 'sharePerResourceGroup')
        self.syscom.u32('disableSCellPDCCHOlLa')
        self.syscom.u32('hasFrameConfTdd')
        self.SFrameConfTdd('frameConfTdd')
        self.SOaMAllowFastActivation('allowFastActivation')
        self.syscom.u32('earfcn')
        self.syscom.end_struct()

    def SSCellResultsParameters(self, name):
        self.syscom.new_struct('SSCellResultsParameters', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('enbId')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def SSCellUeCaParams(self, name):
        self.syscom.new_struct('SSCellUeCaParams', name)
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('paddingServingCellIndex1')
        self.syscom.u8('paddingServingCellIndex2')
        self.syscom.u8('paddingServingCellIndex3')
        self.syscom.u32('interbandCaScell')
        self.syscom.u32('numOfR10n1PucchAnCsList')
        self.syscom.array('2', 'SR10n1PucchAnCsElement', 'r10n1PucchAnCsList')
        self.syscom.u32('numOfR10n3PucchList')
        self.syscom.array('1', 'SR10n3PucchElement', 'r10n3PucchList')
        self.SAperiodicCsiTriggerParams('aperiodicCsiTriggerParams')
        self.syscom.u32('hasCaWmpDcmUlSCellContainer')
        self.UCaWmpDcmUlSCellContainer('caWmpDcmUlSCellContainer')
        self.syscom.end_struct()

    def SSCellUeParams(self, name):
        self.syscom.new_struct('SSCellUeParams', name)
        self.syscom.u32('hasCqiParamsScell')
        self.SCqiParams('cqiParamsScell')
        self.SUeParams('ueParams')
        self.SWmpUserContainer('wmpUserContainer')
        self.SSCellUeCaParams('sCellUeCaParams')
        self.syscom.end_struct()

    def SSCellsConfiguration(self, name):
        self.syscom.new_struct('SSCellsConfiguration', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('sCellServCellIndex')
        self.syscom.u32('enbId')
        self.syscom.u32('transmModeScell')
        self.syscom.u32('sCellConfig')
        self.syscom.u32('maxLayersDeliveredToUeSCell')
        self.syscom.u32('layersRestrictedToTwoSCell')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('hasMaxNumOfLayersSCell')
        self.syscom.u32('maxNumOfLayersSCell')
        self.syscom.u32('hasCqiParamsScell')
        self.SCqiParamsScell('cqiParamsScell')
        self.UCaWmpDcmSCellContainer('container')
        self.syscom.u32('hasUlScellContainer')
        self.UCaWmpDcmUlSCellContainer('ulScellContainer')
        self.syscom.end_struct()

    def SSCellsParams(self, name):
        self.syscom.new_struct('SSCellsParams', name)
        self.syscom.u16('lnCellIdScell')
        self.syscom.u16('lcpForCqiOffsetAdjSCell')
        self.syscom.end_struct()

    def SSCellsRemove(self, name):
        self.syscom.new_struct('SSCellsRemove', name)
        self.syscom.u32('lnCellIdScell')
        self.syscom.u32('enbId')
        self.syscom.end_struct()

    def SSIDLSpecificParamsDcm(self, name):
        self.syscom.new_struct('SSIDLSpecificParamsDcm', name)
        self.syscom.u32('schedPriorityGroupIndexDl')
        self.syscom.u16('prioLcp')
        self.syscom.u16('dlTargetDataRate')
        self.syscom.u16('dlFlagAMBR')
        self.syscom.u16('flagSCellSchedulingDl')
        self.syscom.end_struct()

    def SSIULSpecificParamsDcm(self, name):
        self.syscom.new_struct('SSIULSpecificParamsDcm', name)
        self.syscom.u32('schedPriorityGroupIndexUl')
        self.syscom.u32('ulTargetDataRateMeas')
        self.syscom.u16('prioLcg')
        self.syscom.u16('ulTargetDataRate')
        self.syscom.u16('ulFlagAMBR')
        self.syscom.u16('flagSCellSchedulingUl')
        self.syscom.end_struct()

    def SSRSTriggerParams(self, name):
        self.syscom.new_struct('SSRSTriggerParams', name)
        self.syscom.u32('ulsNumConsecutivePhr')
        self.syscom.u32('hasSrsConfiguration')
        self.syscom.u32('srsConfiguration')
        self.syscom.end_struct()

    def SSRbList(self, name):
        self.syscom.new_struct('SSRbList', name)
        self.syscom.u32('srbId')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def SScellDataTransferData(self, name):
        self.syscom.new_struct('SScellDataTransferData', name)
        self.SCaSplitRbData('caSplitRbData')
        self.SDlBufferStatusInd('dlBsr')
        self.syscom.end_struct()

    def SSchStubInstanceConfig(self, name):
        self.syscom.new_struct('SSchStubInstanceConfig', name)
        self.syscom.u32('mode')
        self.syscom.u32('sicad')
        self.syscom.u32('cellCount')
        self.syscom.array('12', 'u32', 'cellIds')
        self.syscom.end_struct()

    def SSchedulingTable(self, name):
        self.syscom.new_struct('SSchedulingTable', name)
        self.syscom.u32('numOfDlSchedulingRules')
        self.syscom.array('16', 'SDlSchedulingRules', 'dlSchedulingRules')
        self.syscom.u32('numOfDlControlRules')
        self.syscom.array('4', 'SDlSchedulingRules', 'dlControlRules')
        self.syscom.u32('numOfControlRules')
        self.syscom.array('4', 'SDlSchedulingRules', 'controlRules')
        self.syscom.u32('numOfLoopbackRules')
        self.syscom.array('4', 'SDlSchedulingRules', 'loopbackRules')
        self.syscom.u32('numOfPsRules')
        self.syscom.array('numOfPsRules', 'SDlSchedulingRules', 'psRules')
        self.syscom.end_struct()

    def SSchedulingWeightParams(self, name):
        self.syscom.new_struct('SSchedulingWeightParams', name)
        self.syscom.u32('prioHarqDl')
        self.syscom.u32('prioSrbDl')
        self.syscom.u32('prioHarqUl')
        self.syscom.u32('prioSrUl')
        self.syscom.u32('prioSrbUl')
        self.syscom.u32('prioUciOnlyUl')
        self.syscom.end_struct()

    def SSectorBfWeightforAntenna(self, name):
        self.syscom.new_struct('SSectorBfWeightforAntenna', name)
        self.syscom.i16('bfWeigthImag')
        self.syscom.i16('bfWeightReal')
        self.syscom.end_struct()

    def SServiceInfo(self, name):
        self.syscom.new_struct('SServiceInfo', name)
        self.syscom.u32('serviceType')
        self.syscom.u32('serviceAddr')
        self.syscom.end_struct()

    def SServingCellConfiguration(self, name):
        self.syscom.new_struct('SServingCellConfiguration', name)
        self.SSCellsConfiguration('sCellConfiguration')
        self.syscom.u16('ueIndexSCell')
        self.syscom.u16('paddingUeIndexSCell')
        self.syscom.end_struct()

    def SSharedCellId(self, name):
        self.syscom.new_struct('SSharedCellId', name)
        self.syscom.u32('cellId')
        self.SPlmnId('plmnId')
        self.SPlmnId('coreNetworkPlmnId')
        self.syscom.end_struct()

    def SSirParamsLCGDcm(self, name):
        self.syscom.new_struct('SSirParamsLCGDcm', name)
        self.syscom.u16('deltaSirAdjUl')
        self.syscom.u16('targetBlerUl')
        self.syscom.u16('powerOffsetSirUl')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SSmodSfp(self, name):
        self.syscom.new_struct('SSmodSfp', name)
        self.syscom.u16('smod')
        self.syscom.u16('sfp')
        self.syscom.end_struct()

    def SSoundingRsUlConfigCommon(self, name):
        self.syscom.new_struct('SSoundingRsUlConfigCommon', name)
        self.syscom.u32('enableSRS')
        self.syscom.u32('srsBwConf')
        self.syscom.u32('srsSubfrConf')
        self.syscom.u32('anSrsSimulTx')
        self.syscom.u32('hasSrsMaxUpPts')
        self.syscom.u32('srsMaxUpPts')
        self.syscom.end_struct()

    def SSoundingRsUlConfigDedicated(self, name):
        self.syscom.new_struct('SSoundingRsUlConfigDedicated', name)
        self.syscom.u32('enableSRS')
        self.syscom.u32('srsBandwidth')
        self.syscom.u32('srsHoppingBw')
        self.syscom.u32('freqDomPos')
        self.syscom.u32('srsDuration')
        self.syscom.u32('srsConfIndex')
        self.syscom.u32('transComb')
        self.syscom.u32('cyclicShift')
        self.syscom.end_struct()

    def SSpsTfDlDcm(self, name):
        self.syscom.new_struct('SSpsTfDlDcm', name)
        self.syscom.u32('modulation')
        self.syscom.u32('payloadSize')
        self.syscom.u16('numOfRbs')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SSpsTfUlDcm(self, name):
        self.syscom.new_struct('SSpsTfUlDcm', name)
        self.syscom.u32('modulation')
        self.syscom.u32('persistentUlBundling')
        self.syscom.u32('payloadSize')
        self.syscom.u16('numOfRbs')
        self.syscom.u16('persistentTargetSir')
        self.syscom.end_struct()

    def SSrbInfo(self, name):
        self.syscom.new_struct('SSrbInfo', name)
        self.syscom.u32('srbId')
        self.syscom.u32('logicalChannelId')
        self.syscom.u32('logicalChannelGrId')
        self.syscom.u32('logicalChannelIndex')
        self.syscom.u32('rlcMode')
        self.SRlcAmParameters('rlcAmParameters')
        self.UWmpDcmSrbContainer('container')
        self.syscom.end_struct()

    def SSrioBoardPresenceConfig(self, name):
        self.syscom.new_struct('SSrioBoardPresenceConfig', name)
        self.syscom.u32('useBoardPresenceConfig')
        self.syscom.u32('firstFspWspInUseFlag')
        self.syscom.u32('secondFspWspInUseFlag')
        self.syscom.u32('thirdFspWspInUseFlag')
        self.syscom.end_struct()

    def SSrioDaisyChainConfig(self, name):
        self.syscom.new_struct('SSrioDaisyChainConfig', name)
        self.syscom.u32('daisyChain')
        self.syscom.u32('daisyChainModel')
        self.syscom.u32('noOfUsedDaisyChainEntries')
        self.syscom.array('4', 'SSrioDaisyChainParam', 'daisyChainConfig')
        self.syscom.end_struct()

    def SSrioDaisyChainParam(self, name):
        self.syscom.new_struct('SSrioDaisyChainParam', name)
        self.syscom.u32('upperBound16bit')
        self.syscom.u32('lowerBound16bit')
        self.syscom.u32('upperBound8bit')
        self.syscom.u32('lowerBound8bit')
        self.syscom.u32('srioPortId')
        self.syscom.end_struct()

    def SSrioMultiCastConfig(self, name):
        self.syscom.new_struct('SSrioMultiCastConfig', name)
        self.syscom.u32('multicast')
        self.syscom.u32('noOf16BitMulticastEntries')
        self.syscom.u32('multicastId1_16Bit')
        self.syscom.u32('multicastId2_16Bit')
        self.syscom.u32('multicastId3_16Bit')
        self.syscom.u32('noOf8BitMulticastEntries')
        self.syscom.u32('multicastId1_8Bit')
        self.syscom.u32('multicastId2_8Bit')
        self.syscom.u32('multicastId3_8Bit')
        self.syscom.end_struct()

    def SSrioPhysicalPara(self, name):
        self.syscom.new_struct('SSrioPhysicalPara', name)
        self.syscom.u32('linkspeed')
        self.syscom.u32('loopBack')
        self.syscom.u32('clockrate')
        self.syscom.u32('deviceId16Bit')
        self.syscom.u32('deviceId8Bit')
        self.syscom.u32('portEn')
        self.syscom.array('2', 'u32', 'serdesCfgRxCntl')
        self.syscom.array('2', 'u32', 'serdesCfgTxCntl')
        self.syscom.end_struct()

    def SSrioSysComRegRxConfig(self, name):
        self.syscom.new_struct('SSrioSysComRegRxConfig', name)
        self.syscom.u32('rxPoolUseL2Cache')
        self.syscom.u32('rxFirstStageMsgBufferPoolId')
        self.syscom.u32('rxSecondStageMsgBufferPoolId')
        self.syscom.u32('rxReassembleMsgBufferPoolId')
        self.syscom.u32('rxNoOfMultiSegmentQueue')
        self.syscom.u32('rxNoOfBdPerMultiSegmentQueue')
        self.syscom.u32('rxNoOfBdPerSingleSegmentQueue')
        self.syscom.end_struct()

    def SSrioSysComRegTxConfig(self, name):
        self.syscom.new_struct('SSrioSysComRegTxConfig', name)
        self.syscom.array('10', 'u32', 'hopSicad')
        self.syscom.array('10', 'u32', 'hopMetric')
        self.syscom.u32('txMsgFragmentBufferPoolId')
        self.syscom.end_struct()

    def SSrsBandwidthControlInfoDcm(self, name):
        self.syscom.new_struct('SSrsBandwidthControlInfoDcm', name)
        self.syscom.array('4', 'SSrsRefTableDcm', 'srsRefTable')
        self.syscom.u16('tttSrsTh')
        self.syscom.u16('tttSrsRenewalCycle')
        self.syscom.u16('indexSrsInitIndex')
        self.syscom.u16('tttRefTableThUp')
        self.syscom.u16('tttRefTableThDown')
        self.syscom.u16('refTableInitIndex')
        self.syscom.end_struct()

    def SSrsIndexRestrictionInfoDcm(self, name):
        self.syscom.new_struct('SSrsIndexRestrictionInfoDcm', name)
        self.syscom.array('4', 'u16', 'thTARestrict')
        self.syscom.array('4', 'u16', 'indexMinRestrictInit')
        self.syscom.array('4', 'u16', 'indexMinRestrictLowPL')
        self.syscom.array('4', 'u16', 'indexMinRestrictMiddlePL')
        self.syscom.array('4', 'u16', 'indexMinRestrictHighPL')
        self.syscom.array('4', 'u16', 'thPLRestrictLow')
        self.syscom.array('4', 'u16', 'thPLRestrictHigh')
        self.syscom.array('4', 'u16', 'rbMaxRestrictInit')
        self.syscom.array('4', 'u16', 'rbMaxRestrictLowPL')
        self.syscom.array('4', 'u16', 'rbMaxRestrictMiddlePL')
        self.syscom.array('4', 'u16', 'rbMaxRestrictHighPL')
        self.syscom.end_struct()

    def SSrsParamsScellWmp(self, name):
        self.syscom.new_struct('SSrsParamsScellWmp', name)
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('paddingServingCellIndex1')
        self.syscom.u8('paddingServingCellIndex2')
        self.syscom.u8('paddingServingCellIndex3')
        self.SSoundingRsUlConfigDedicated('soundingRsUlConfigDedicated')
        self.syscom.end_struct()

    def SSrsReceiveReq(self, name):
        self.syscom.new_struct('SSrsReceiveReq', name)
        self.syscom.u32('numOfUeReq')
        self.syscom.array('numOfUeReq', 'SSrsUeReceiveReq', 'ueReq')
        self.syscom.end_struct()

    def SSrsReceiveRespU(self, name):
        self.syscom.new_struct('SSrsReceiveRespU', name)
        self.syscom.u32('numOfSrsMeas')
        self.syscom.u32('numOfUeResp')
        self.syscom.array('numOfUeResp', 'SSrsUeReceiveRespU', 'ueResp')
        self.syscom.end_struct()

    def SSrsRefTableDcm(self, name):
        self.syscom.new_struct('SSrsRefTableDcm', name)
        self.syscom.array('8', 'SPSrsOffsetInfoDcm', 'pSrsOffsetRefTable')
        self.syscom.u16('interferenceTableUp')
        self.syscom.u16('interferenceTableDown')
        self.syscom.end_struct()

    def SSrsUeReceiveReq(self, name):
        self.syscom.new_struct('SSrsUeReceiveReq', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u8('cyclicShift')
        self.syscom.u8('srsBandWidth')
        self.syscom.u8('startPosition')
        self.syscom.u8('transComb')
        self.syscom.u8('bfMeasurement')
        self.syscom.u8('explicitPadding')
        self.syscom.u16('explicitPadding2')
        self.syscom.end_struct()

    def SSrsUeReceiveRespU(self, name):
        self.syscom.new_struct('SSrsUeReceiveRespU', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.u8('srsQualityResult')
        self.syscom.u8('srsBandWidth')
        self.syscom.u8('startPosition')
        self.syscom.u8('subCellId')
        self.syscom.u16('payloadOffset')
        self.syscom.u16('explicitPadding')
        self.syscom.end_struct()

    def SStatisticalMeasurementType(self, name):
        self.syscom.new_struct('SStatisticalMeasurementType', name)
        self.syscom.u32('measurementType')
        self.syscom.u32('nbrOfCounters')
        self.syscom.array('nbrOfCounters', 'SPmCounter', 'counters')
        self.syscom.end_struct()

    def SSubCellMeasurement(self, name):
        self.syscom.new_struct('SSubCellMeasurement', name)
        self.syscom.u8('subCellId')
        self.syscom.u8('numOfSubCellPreamble')
        self.syscom.u16('explicitPadding')
        self.syscom.real32('interferencePower')
        self.syscom.end_struct()

    def SSuperCellParameters(self, name):
        self.syscom.new_struct('SSuperCellParameters', name)
        self.syscom.u32('actSuperCell')
        self.SContainerOfOaMSuperCellParSet('superCellParSet')
        self.syscom.u32('numOfSubCells')
        self.syscom.end_struct()

    def SSyncInfoDlDcm(self, name):
        self.syscom.new_struct('SSyncInfoDlDcm', name)
        self.syscom.u16('syncInitialTimer')
        self.syscom.u16('nSyncReqMax')
        self.syscom.u16('syncTimerR')
        self.syscom.u16('syncTimerD')
        self.syscom.u16('maxNumOfSyncReqs')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def STaParamsDlDcm(self, name):
        self.syscom.new_struct('STaParamsDlDcm', name)
        self.syscom.u32('periodicityTa')
        self.syscom.u32('timeAlignmentTimerDedicated')
        self.syscom.u16('periodicTaEnable')
        self.syscom.u16('eventTriggeredTaEnable')
        self.syscom.u16('thStopPeriodicTaTh')
        self.syscom.u16('thTatRestartTA')
        self.syscom.u16('tProhibitRestartTA')
        self.syscom.u16('thStopRestartTA')
        self.syscom.u16('tProhibitPaddingTA')
        self.syscom.u16('thPduSizePaddingTA')
        self.syscom.u16('thTatPaddingTA')
        self.syscom.u16('padding')
        self.syscom.u32('offsetTrafficIAT')
        self.syscom.end_struct()

    def STargetBLER(self, name):
        self.syscom.new_struct('STargetBLER', name)
        self.syscom.u32('hasTargetBlerDl')
        self.syscom.u32('targetBlerDl')
        self.syscom.u32('targetBlerUl')
        self.syscom.end_struct()

    def SThroughputThresholdMonitoring(self, name):
        self.syscom.new_struct('SThroughputThresholdMonitoring', name)
        self.syscom.u32('enableThroughputThresholdMonitoring')
        self.syscom.u32('dlThroughputThreshold')
        self.syscom.u32('ulThroughputThreshold')
        self.syscom.end_struct()

    def STmSwitch(self, name):
        self.syscom.new_struct('STmSwitch', name)
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u32('newTransmMode')
        self.syscom.end_struct()

    def STpcPdcchConfigParams(self, name):
        self.syscom.new_struct('STpcPdcchConfigParams', name)
        self.syscom.u32('tpcPucchRnti')
        self.syscom.u32('tpcPucchIndexOfFormat3')
        self.syscom.u32('tpcPuschRnti')
        self.syscom.u32('tpcPuschIndexOfFormat3')
        self.syscom.end_struct()

    def STpcPdcchForPucchParamsDlDcm(self, name):
        self.syscom.new_struct('STpcPdcchForPucchParamsDlDcm', name)
        self.syscom.u16('startOffsetForTpcPdcchForPucch')
        self.syscom.u16('padding')
        self.syscom.u32('periodicityForTpcPdcchForPucch')
        self.syscom.end_struct()

    def STpcPdcchForPuschParamsUlDcm(self, name):
        self.syscom.new_struct('STpcPdcchForPuschParamsUlDcm', name)
        self.syscom.u16('startOffsetForTpcPdcchForPusch')
        self.syscom.u16('padding')
        self.syscom.u32('periodicityForTpcPdcchForPusch')
        self.syscom.end_struct()

    def STransmModeParams(self, name):
        self.syscom.new_struct('STransmModeParams', name)
        self.syscom.u32('actTmSwitch')
        self.syscom.u32('prohibitTimerTmSwitch')
        self.SOaMTmSwitchThresholdDef('tmSwitchThresholdDef')
        self.syscom.end_struct()

    def STransportLayerAddress(self, name):
        self.syscom.new_struct('STransportLayerAddress', name)
        self.syscom.u32('addressLength')
        self.syscom.array('16', 'u8', 'address')
        self.syscom.end_struct()

    def STtiBundlingParameters(self, name):
        self.syscom.new_struct('STtiBundlingParameters', name)
        self.SOaMTtiBundlingBlerThreshold('ttiBundlingBlerThreshold')
        self.SOaMTtiBundlingSinrThreshold('ttiBundlingSinrThreshold')
        self.SOaMTtiBundlingBlerTarget('ttiBundlingBlerTarget')
        self.syscom.u32('ttiBundlingCStepUp')
        self.syscom.i32('ttiBundlingDeltaCini')
        self.syscom.i32('ttiBundlingDeltaCmin')
        self.syscom.u32('ttiBundlingDeltaCmax')
        self.syscom.u32('ttibOperMode')
        self.syscom.i32('ttibSinrThresholdIn')
        self.syscom.i32('ttibSinrThresholdOut')
        self.syscom.end_struct()

    def STupDiscardParameters(self, name):
        self.syscom.new_struct('STupDiscardParameters', name)
        self.syscom.u32('thOverflowDiscard')
        self.syscom.u32('flagOverflowDiscard')
        self.syscom.u32('discBuffThrAct')
        self.syscom.u32('discBuffHighThr')
        self.syscom.array('10', 'u32', 'discBuffHighThrList')
        self.syscom.u32('chBw')
        self.syscom.u32('thresholdOverflowDiscard2')
        self.syscom.u32('outflowAverageRLCinitial')
        self.syscom.u32('outflowRateRLCmin')
        self.syscom.u32('tDiscardComponentBased')
        self.syscom.u32('forgettingFactorL2BufferAmount')
        self.syscom.u32('forgettingFactorRLCoutflow')
        self.syscom.end_struct()

    def STupPdcpSrbInfo(self, name):
        self.syscom.new_struct('STupPdcpSrbInfo', name)
        self.syscom.u32('pdcpSnLength')
        self.syscom.end_struct()

    def STupRbInfoBearerModify(self, name):
        self.syscom.new_struct('STupRbInfoBearerModify', name)
        self.syscom.u32('drbId')
        self.syscom.u32('hasDscp')
        self.syscom.u32('dscp')
        self.syscom.u32('hasQci')
        self.syscom.u32('qci')
        self.syscom.u32('hasQciCounterGroup')
        self.syscom.u32('qciCounterGroup')
        self.syscom.u32('logicalChannelIndex')
        self.syscom.end_struct()

    def STupRbInfoBearerSetup(self, name):
        self.syscom.new_struct('STupRbInfoBearerSetup', name)
        self.syscom.u32('drbId')
        self.syscom.u32('rlcMode')
        self.SGtpInfoBearerSetup('gtpInfo')
        self.SPdcpRbInfoBearerSetup('pdcpInfo')
        self.syscom.u32('qci')
        self.syscom.u32('qciCounterGroup')
        self.syscom.u32('logicalChannelIndex')
        self.syscom.end_struct()

    def STupRbInfoDataForwardSetup(self, name):
        self.syscom.new_struct('STupRbInfoDataForwardSetup', name)
        self.syscom.u32('drbId')
        self.syscom.u32('dataForwardingType')
        self.SGtpInfoDataForwardSetup('gtpInfoDl')
        self.SGtpInfoDataForwardSetup('gtpInfoUl')
        self.syscom.u32('index')
        self.syscom.end_struct()

    def STupRbInfoDataForwardSetupResp(self, name):
        self.syscom.new_struct('STupRbInfoDataForwardSetupResp', name)
        self.syscom.u32('drbId')
        self.syscom.u32('numOfRxStatusOfUlPdcpSdus')
        self.syscom.array('512', 'u8', 'rxStatusOfUlPdcpSdus')
        self.syscom.u32('ulHfnValue')
        self.syscom.u32('ulPdcpSnValue')
        self.syscom.u32('dlHfnValue')
        self.syscom.u32('dlPdcpSnValue')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def STupRbInfoPathSwitch(self, name):
        self.syscom.new_struct('STupRbInfoPathSwitch', name)
        self.syscom.u32('drbId')
        self.SGtpInfoPathSwitch('gtpInfo')
        self.syscom.u32('uplinkMute')
        self.syscom.end_struct()

    def STupRbInfoPdcpEnable(self, name):
        self.syscom.new_struct('STupRbInfoPdcpEnable', name)
        self.syscom.u32('drbId')
        self.syscom.u32('tS1DataRetard')
        self.syscom.u32('numOfRxStatusOfUlPdcpSdus')
        self.syscom.array('512', 'u8', 'rxStatusOfUlPdcpSdus')
        self.syscom.u32('ulHfnValue')
        self.syscom.u32('ulPdcpSnValue')
        self.syscom.u32('dlHfnValue')
        self.syscom.u32('dlPdcpSnValue')
        self.syscom.end_struct()

    def STupRbInfoResp(self, name):
        self.syscom.new_struct('STupRbInfoResp', name)
        self.syscom.u32('drbId')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def STupRbInfoUserSetup(self, name):
        self.syscom.new_struct('STupRbInfoUserSetup', name)
        self.syscom.u32('drbId')
        self.syscom.u32('rlcMode')
        self.syscom.u32('dataForwardingType')
        self.SGtpInfoUserSetup('gtpInfo')
        self.SPdcpRbInfoUserSetup('pdcpInfo')
        self.syscom.u32('qci')
        self.syscom.u32('qciCounterGroup')
        self.syscom.u32('logicalChannelIndex')
        self.syscom.end_struct()

    def STupSecurityInformation(self, name):
        self.syscom.new_struct('STupSecurityInformation', name)
        self.syscom.chars('16', 'kRrcInt')
        self.syscom.chars('16', 'kRrcEnc')
        self.syscom.chars('16', 'kUpEnc')
        self.syscom.u32('intAlgorithm')
        self.syscom.u32('encAlgorithm')
        self.syscom.u32('keyRefreshMargin')
        self.syscom.end_struct()

    def STupSrbInfo(self, name):
        self.syscom.new_struct('STupSrbInfo', name)
        self.syscom.u32('srbId')
        self.syscom.u32('rlcMode')
        self.STupPdcpSrbInfo('pdcpInfo')
        self.syscom.end_struct()

    def STupSrbInfoResp(self, name):
        self.syscom.new_struct('STupSrbInfoResp', name)
        self.syscom.u32('srbId')
        self.SMessageResult('messageResult')
        self.syscom.end_struct()

    def STupUserAddress(self, name):
        self.syscom.new_struct('STupUserAddress', name)
        self.syscom.u32('dlTupUserAddress')
        self.syscom.end_struct()

    def STxPowersDlDcm(self, name):
        self.syscom.new_struct('STxPowersDlDcm', name)
        self.syscom.u16('referenceSignalPower')
        self.syscom.u16('pASch')
        self.syscom.u16('pAPbch')
        self.syscom.u16('pBPbch')
        self.syscom.u16('pAPdsch')
        self.syscom.u16('pBPdsch')
        self.syscom.end_struct()

    def SUciOnlyGrantConfiguration(self, name):
        self.syscom.new_struct('SUciOnlyGrantConfiguration', name)
        self.syscom.u32('actUciOnlyGrants')
        self.syscom.u32('multUciGrant')
        self.syscom.u32('multNumUeHighPrioUciGrant')
        self.syscom.u32('maxPrbHighPrioUciGrant')
        self.syscom.end_struct()

    def SUeBufferStatus(self, name):
        self.syscom.new_struct('SUeBufferStatus', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('crnti')
        self.syscom.u8('usefulDataReceived')
        self.syscom.u8('numBearerIdList')
        self.syscom.u8('dtchMacSduReceived')
        self.syscom.u8('harqProcessNumber')
        self.syscom.array('4', 'SLcgIds', 'lcgIdList')
        self.syscom.array('8', 'SBearerIds', 'bearerIdList')
        self.syscom.end_struct()

    def SUeHoParams(self, name):
        self.syscom.new_struct('SUeHoParams', name)
        self.syscom.u32('ueCategory')
        self.syscom.u32('ueCategoryR10')
        self.syscom.u32('ueCategoryR11')
        self.syscom.u32('ueCategoryR11a0')
        self.syscom.u32('ueCategoryDlR12')
        self.syscom.u32('ueCategoryUlR12')
        self.syscom.u32('ul64QAMCapable')
        self.syscom.u32('hasAmbrParams')
        self.SAmbrParams('ambrParams')
        self.syscom.u32('hasBitRateParams')
        self.SBitRateParams('bitRateParams')
        self.syscom.u32('hasDrxParameters')
        self.SDrxParameters('drxParameters')
        self.syscom.end_struct()

    def SUeInfo(self, name):
        self.syscom.new_struct('SUeInfo', name)
        self.syscom.u16('crnti')
        self.syscom.u16('ueIndex')
        self.syscom.end_struct()

    def SUeList(self, name):
        self.syscom.new_struct('SUeList', name)
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.array('4', 'u8', 'drbIdList')
        self.syscom.u16('paddingDrbIdList')
        self.syscom.u32('bearerReleaseIndCause')
        self.syscom.end_struct()

    def SUeParams(self, name):
        self.syscom.new_struct('SUeParams', name)
        self.syscom.u32('transmMode')
        self.syscom.u32('accessStratumRelease')
        self.syscom.u32('ueCreAttributes')
        self.syscom.u32('hasUeHoParams')
        self.SUeHoParams('ueHoParams')
        self.syscom.end_struct()

    def SUePhr(self, name):
        self.syscom.new_struct('SUePhr', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('crnti')
        self.syscom.u8('powerLevel')
        self.syscom.u8('servCellIndex')
        self.syscom.u8('pcMax')
        self.syscom.u8('ePhrBitFields')
        self.syscom.end_struct()

    def SUeSetupParams(self, name):
        self.syscom.new_struct('SUeSetupParams', name)
        self.syscom.u32('srEnable')
        self.syscom.u32('pucchResourceIndex')
        self.syscom.u32('srPeriod')
        self.syscom.u32('srOffset')
        self.syscom.u32('hasUeSetupParamsConfigId')
        self.syscom.u32('ueSetupParamsConfigId')
        self.syscom.end_struct()

    def SUlAddrGroupInSubPool(self, name):
        self.syscom.new_struct('SUlAddrGroupInSubPool', name)
        self.syscom.u32('puschReceiverAddress')
        self.syscom.u32('pucchReceiverAddress')
        self.syscom.u32('srsReceiverAddress')
        self.syscom.end_struct()

    def SUlBufStatusIndPayload(self, name):
        self.syscom.new_struct('SUlBufStatusIndPayload', name)
        self.syscom.u32('numberOfUes')
        self.syscom.array('20', 'SUeBufferStatus', 'ueIdInfo')
        self.syscom.end_struct()

    def SUlCtrlChannelMeasCounters(self, name):
        self.syscom.new_struct('SUlCtrlChannelMeasCounters', name)
        self.syscom.u32('detectedCounter')
        self.syscom.u32('missedCounter')
        self.syscom.u32('falseCounter')
        self.syscom.u32('idlePeriodCounter')
        self.syscom.end_struct()

    def SUlCtrlChannelMeasCountersMissedPrach(self, name):
        self.syscom.new_struct('SUlCtrlChannelMeasCountersMissedPrach', name)
        self.syscom.u32('noPaCounter')
        self.syscom.u32('wrongPaCounter')
        self.syscom.u32('wrongTimingCounter')
        self.syscom.end_struct()

    def SUlCtrlChannelPrachParams(self, name):
        self.syscom.new_struct('SUlCtrlChannelPrachParams', name)
        self.syscom.u32('prachConfIndex')
        self.syscom.u32('preambleIndex')
        self.syscom.u32('acceptedTimingError')
        self.syscom.u32('constantOffset')
        self.syscom.u32('delayPatternSingleStepDuration')
        self.syscom.end_struct()

    def SUlCtrlChannelPucchAckParams(self, name):
        self.syscom.new_struct('SUlCtrlChannelPucchAckParams', name)
        self.syscom.u32('pucchResourceIndexAn')
        self.syscom.u32('pucchResourceIndexSecond')
        self.syscom.u32('pucchResourceIndexThird')
        self.syscom.u32('pucchResourceIndexFourth')
        self.syscom.u32('pucchResourceIndexFifth')
        self.syscom.end_struct()

    def SUlCtrlChannelPucchCqiParams(self, name):
        self.syscom.new_struct('SUlCtrlChannelPucchCqiParams', name)
        self.syscom.u32('pucchResourceIndexCqi')
        self.syscom.u32('pucchResourceIndexSecond')
        self.syscom.u32('pucchResourceIndexThird')
        self.syscom.u32('pucchResourceIndexFourth')
        self.syscom.end_struct()

    def SUlCtrlChannelPuschHarqAckParams(self, name):
        self.syscom.new_struct('SUlCtrlChannelPuschHarqAckParams', name)
        self.syscom.u32('referenceChannelNumber')
        self.syscom.u32('resourceBlockOffset')
        self.syscom.end_struct()

    def SUlDcmMacPsContainerCSDcm(self, name):
        self.syscom.new_struct('SUlDcmMacPsContainerCSDcm', name)
        self.SPrachTpcParamsUlDcm('prachTpcParamsUl')
        self.SPuschFreqHoppingInformationDcm('puschFreqHoppingInformation')
        self.SSrsBandwidthControlInfoDcm('srsBandwidthControlInfo')
        self.SRbgOffsetControlInfoDcm('rbgOffsetControlInfo')
        self.SPuschTpcParamsUlDcm('puschTpcParamsUl')
        self.SCchInformationUlDcm('cchInformationUl')
        self.SUlPersistentParamsUlDcm('ulPersistentParamsUl')
        self.syscom.array('4', 'SDcmLCGInfoCSDcm', 'dcmLCGInfoTable')
        self.SBackoffIndicatorInfoDcm('backoffIndicatorInfo')
        self.SUlVoLteParamsDcm('voLteUlParams')
        self.syscom.u32('averTimeSRSI')
        self.syscom.u32('averTimeSRSS')
        self.syscom.u32('modulationSchemeMsg3')
        self.syscom.u32('rMinUl')
        self.syscom.u32('ulRbAllocationMode')
        self.syscom.u32('coeffKs')
        self.syscom.u32('averTimeDMRSS')
        self.syscom.u32('ueInactivityTimerIdleTh')
        self.syscom.u32('fdEstimationUsage')
        self.syscom.u16('guardRbLow')
        self.syscom.u16('guardRbHigh')
        self.syscom.u16('maxNumEmergCallsUl')
        self.syscom.u16('prioSr')
        self.syscom.u16('numUlHighPl')
        self.syscom.u16('numUlLowPl')
        self.syscom.u16('pathlossUlTh')
        self.syscom.u16('ulTxTypeMode')
        self.syscom.u16('pathlossUlPhichTh')
        self.syscom.u16('coeffPathloss')
        self.syscom.u16('coeffTFRS')
        self.syscom.u16('coefAdjust')
        self.syscom.u16('nRBUlBufferMin')
        self.syscom.u16('pathlossDlTh')
        self.syscom.u16('nUlMax')
        self.syscom.u16('refPathloss')
        self.syscom.u16('maxSirOffsetUl')
        self.syscom.u16('minSirOffsetUl')
        self.syscom.u16('plAperCQINotTriggered')
        self.syscom.u16('pathlossUlThNoSRS')
        self.syscom.u16('minAperiodicCqiMCS')
        self.syscom.u16('ttiBundlingSirOffset')
        self.SAssuredPucchInfoUl('assuredPucchInfoUl')
        self.SSrsIndexRestrictionInfoDcm('srsIndexRestrictionInfoDcm')
        self.syscom.u32('ulAmbrPeriod')
        self.syscom.u16('deltaPreambleMsg3')
        self.syscom.u16('minCostAMBR')
        self.syscom.u16('maxTbsAMBR')
        self.syscom.u16('flagRBReduction')
        self.syscom.u16('flagPhichHopping')
        self.syscom.u16('nUlCandidateMax')
        self.syscom.u16('alphaUlPDCCH')
        self.syscom.u16('betaUlPDCCHCommon')
        self.syscom.u16('gammaUlPDCCH')
        self.syscom.u16('minPuschSir')
        self.syscom.u32('thSCellActivationUl1')
        self.syscom.u32('thSCellActivationUl2')
        self.syscom.u16('flagRBGReconcate')
        self.syscom.u16('flagTFRSorting')
        self.syscom.u16('flagRBGSelect')
        self.syscom.u16('flagUlbufferControl')
        self.syscom.u16('nTmpUlbufferSR')
        self.syscom.u16('reserved1')
        self.syscom.array('11', 'u16', 'rbAn')
        self.syscom.array('11', 'u16', 'tfIndexAn')
        self.syscom.u16('freqCell')
        self.syscom.array('4', 'u16', 'freqAggressor')
        self.syscom.array('4', 'u16', 'freqVictim')
        self.syscom.array('4', 'u16', 'thCQILow')
        self.syscom.array('4', 'u16', 'thCQIHigh')
        self.syscom.array('4', 'u16', 'thPowerLow')
        self.syscom.array('4', 'u16', 'thPowerMiddle')
        self.syscom.array('4', 'u16', 'thPowerHigh')
        self.syscom.array('4', 'u16', 'InterferenceRBStart')
        self.syscom.array('4', 'u16', 'InterferenceRBEnd')
        self.syscom.array('4', 'u16', 'ulRestrict')
        self.syscom.array('4', 'u16', 'interferenceMaxRB')
        self.syscom.u16('tmpPUSCHRB')
        self.syscom.end_struct()

    def SUlDcmMacPsContainerRbSDcm(self, name):
        self.syscom.new_struct('SUlDcmMacPsContainerRbSDcm', name)
        self.syscom.u16('persistentUlEnable')
        self.syscom.u16('siul')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('reserved3')
        self.syscom.u16('reserved4')
        self.syscom.u16('reserved5')
        self.syscom.u16('padding')
        self.syscom.end_struct()

    def SUlDcmMacPsContainerUSDcm(self, name):
        self.syscom.new_struct('SUlDcmMacPsContainerUSDcm', name)
        self.STpcPdcchForPuschParamsUlDcm('tpcPdcchForPuschTpcParamsUl')
        self.syscom.u32('callTypeUl')
        self.syscom.u32('initialUEInactivityTimerValue')
        self.syscom.u32('maxPayloadSizeUlAmbr')
        self.syscom.u32('ueInactivityTimerIdleTh')
        self.syscom.u16('lcgForSIROffsetAdj')
        self.syscom.u16('ueMaxTxPower')
        self.syscom.u16('tMaxNumHarqRetransmissionsUlSch')
        self.syscom.u16('p0UePusch')
        self.syscom.u16('flagFirstBearerSetup')
        self.syscom.u16('initialPathloss')
        self.syscom.u16('initialPeriodicGrantIndexandStatus')
        self.syscom.u16('initialNumProhibitPeriodicGrant')
        self.syscom.u16('initialMinPeriodicGrantIndex')
        self.syscom.u16('initialDmrsSirForPeriodicGrant')
        self.syscom.u16('initialProhibitTbReconfig')
        self.syscom.u16('reserved4')
        self.syscom.end_struct()

    def SUlMuMimoParameters(self, name):
        self.syscom.new_struct('SUlMuMimoParameters', name)
        self.syscom.u32('actUlMuMimo')
        self.syscom.u32('hasUlMuMimoParaSet')
        self.SOaMUlMuMimoParaSet('ulMuMimoParaSet')
        self.syscom.end_struct()

    def SUlPCCellParams(self, name):
        self.syscom.new_struct('SUlPCCellParams', name)
        self.syscom.i32('ulpcRarespTpc')
        self.syscom.u32('dFpucchF1')
        self.syscom.u32('dFpucchF1b')
        self.syscom.u32('dFpucchF2')
        self.syscom.u32('dFpucchF2a')
        self.syscom.u32('dFpucchF2b')
        self.syscom.i32('ulpcRssiMin')
        self.syscom.i32('ulpcRssiMax')
        self.syscom.i32('ulpcSinrMin')
        self.syscom.i32('ulpcSinrMax')
        self.syscom.u32('ulpcWfPucchcell')
        self.syscom.u32('ulpcWfPucchUe')
        self.syscom.u32('ulpcWfPuschcell')
        self.syscom.u32('ulpcWfPuschUe')
        self.syscom.u32('ulpcWfSrscell')
        self.syscom.u32('ulpcWfSrsUe')
        self.syscom.i32('ulpcCumpucchmin')
        self.syscom.i32('ulpcCumpucchmax')
        self.syscom.i32('ulpcCumpuschmin')
        self.syscom.i32('ulpcCumpuschmax')
        self.SOaMUlpcReadPeriod('ulpcReadPeriod')
        self.syscom.u32('ulpcSchavgtcont')
        self.syscom.u32('ulpcSchavgtdisc')
        self.syscom.u32('ulpcCchavgtcont')
        self.syscom.u32('ulpcCchavgtdisc')
        self.syscom.u32('actUlpcMethod')
        self.syscom.i32('p0NominalPusch')
        self.syscom.i32('p0NomPucch')
        self.syscom.i32('deltaPreambleMsg3')
        self.syscom.u32('ulpcAlpha')
        self.syscom.u32('hasUlpcPucchConfig')
        self.SOaMUlpcPucchConfig('ulpcPucchConfig')
        self.syscom.u32('hasUlpcPuschConfig')
        self.SOaMUlpcPuschConfig('ulpcPuschConfig')
        self.syscom.u32('hasUlpcIawConfig')
        self.SUlpcIawConfig('ulpcIawConfig')
        self.syscom.u32('hasPMax')
        self.syscom.i32('pMax')
        self.syscom.end_struct()

    def SUlPCUeParams(self, name):
        self.syscom.new_struct('SUlPCUeParams', name)
        self.syscom.i32('p0UePusch')
        self.syscom.i32('p0UePucch')
        self.syscom.u32('deltaTfEnabled')
        self.syscom.u32('ulpcAccuEnable')
        self.SOaMSrsPwrOffset('srsPwrOffset')
        self.syscom.end_struct()

    def SUlPersistentParamsUlDcm(self, name):
        self.syscom.new_struct('SUlPersistentParamsUlDcm', name)
        self.syscom.array('4', 'SSpsTfUlDcm', 'persistentTfUlTable')
        self.syscom.array('3', 'u16', 'persistentUlTfrUpTable')
        self.syscom.array('3', 'u16', 'persistentUlTfrDownTable')
        self.syscom.array('3', 'u16', 'persistentTfrInitUlTable')
        self.syscom.array('4', 'u16', 'mcsIndexUl')
        self.syscom.array('4', 'u16', 'numRbUl')
        self.syscom.u16('padding')
        self.syscom.u32('persistentTttUlTh')
        self.syscom.u32('persistentReconfigUlTimerTh')
        self.syscom.u32('averTimePersistentSir')
        self.syscom.u16('ulTalkSpurtUpperDataTh')
        self.syscom.u16('ulTalkSpurtLowerDataTh')
        self.syscom.u16('rbPersistent0')
        self.syscom.u16('rbPersistent1')
        self.syscom.u16('numOfMaxTxTh')
        self.syscom.u16('weightRachMsg3')
        self.syscom.u16('weightPersistentUl')
        self.syscom.u16('averTimeRachMsg3RBUsage')
        self.syscom.u16('averTimePersistentUlRBUsage')
        self.syscom.u16('implicitReleaseAfter')
        self.syscom.end_struct()

    def SUlPhyDataAddressInfo(self, name):
        self.syscom.new_struct('SUlPhyDataAddressInfo', name)
        self.syscom.u32('puschReceiverAddress')
        self.syscom.u32('pucchReceiverAddress')
        self.syscom.u32('srsReceiverAddress')
        self.syscom.end_struct()

    def SUlRbsAmResult(self, name):
        self.syscom.new_struct('SUlRbsAmResult', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u8('numberOfRadioBearers')
        self.syscom.u8('paddingNumberOfRadioBearers1')
        self.syscom.u8('paddingNumberOfRadioBearers2')
        self.syscom.u8('paddingNumberOfRadioBearers3')
        self.syscom.array('10', 'SDctUlRlcAmPduResult', 'dctUlRlcAmPduResults')
        self.syscom.end_struct()

    def SUlRbsUmResult(self, name):
        self.syscom.new_struct('SUlRbsUmResult', name)
        self.syscom.u32('cellId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u8('numberOfRadioBearers')
        self.syscom.u8('paddingNumberOfRadioBearers1')
        self.syscom.u8('paddingNumberOfRadioBearers2')
        self.syscom.u8('paddingNumberOfRadioBearers3')
        self.syscom.array('10', 'SDctUlRlcUmPduResult', 'dctUlRlcUmPduResults')
        self.syscom.end_struct()

    def SUlSpsConfig(self, name):
        self.syscom.new_struct('SUlSpsConfig', name)
        self.syscom.u32('maxNumSpsUeUl')
        self.syscom.u32('ulSpsInterval')
        self.syscom.u32('ulSpsMaxNumPrb')
        self.syscom.u32('ulSpsMaxPrbPerUeNB')
        self.syscom.u32('ulSpsMaxPrbPerUeWB')
        self.syscom.u32('ulSpsMinVoicePktSize')
        self.syscom.u32('ulSpsTwoIntervalConfig')
        self.syscom.u32('ulSpsVoicePktTbsNB')
        self.syscom.u32('ulSpsVoicePktTbsWB')
        self.syscom.u32('ulTargetBlerSps')
        self.syscom.end_struct()

    def SUlSpsConfigDedicated(self, name):
        self.syscom.new_struct('SUlSpsConfigDedicated', name)
        self.syscom.u32('ulSpsNumEmptyTransmissions')
        self.syscom.i32('p0NomPuschSps')
        self.syscom.u32('amrWbNb')
        self.syscom.end_struct()

    def SUlSpsParaSet(self, name):
        self.syscom.new_struct('SUlSpsParaSet', name)
        self.syscom.u32('ulMaxSpsRetry')
        self.syscom.u32('nSpsDTX')
        self.syscom.u32('maxNumDSUeUl')
        self.syscom.i32('p0UePuschSps')
        self.syscom.u32('deltaSinrSpsInitialMcs')
        self.syscom.u32('deltaSinrPercentSpsMcsUpgrade')
        self.syscom.u32('ulSpsMaxExplicitReleaseRetry')
        self.syscom.u32('actUlSpsPrbSelection')
        self.syscom.u32('actUlSpsUESelectionCCEBase')
        self.SUlSpsConfig('ulSpsConfig')
        self.syscom.end_struct()

    def SUlSpsParameters(self, name):
        self.syscom.new_struct('SUlSpsParameters', name)
        self.syscom.u32('actUlSps')
        self.syscom.u32('hasUlSpsParaSet')
        self.SUlSpsParaSet('ulSpsParaSet')
        self.syscom.end_struct()

    def SUlTbFormat(self, name):
        self.syscom.new_struct('SUlTbFormat', name)
        self.syscom.u8('modulation')
        self.syscom.u8('newDataIndicator')
        self.syscom.u8('harqProcessNumber')
        self.syscom.u8('redundancyVersion')
        self.syscom.end_struct()

    def SUlTestModelConfig(self, name):
        self.syscom.new_struct('SUlTestModelConfig', name)
        self.syscom.u32('noOfHarqTransmissions')
        self.syscom.u32('hstConfig')
        self.syscom.u32('resourceIndexCqi')
        self.syscom.u32('iCqiPmi')
        self.syscom.end_struct()

    def SUlTestModelsDigitalOutputParams(self, name):
        self.syscom.new_struct('SUlTestModelsDigitalOutputParams', name)
        self.syscom.u32('digitalOutputType')
        self.syscom.u32('bitRate')
        self.syscom.u32('bBSelector')
        self.syscom.end_struct()

    def SUlUeBufferStatus(self, name):
        self.syscom.new_struct('SUlUeBufferStatus', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('crnti')
        self.syscom.u16('cellId')
        self.syscom.u16('servCellIndex')
        self.syscom.u8('usefulDataReceived')
        self.syscom.u8('numBearerIdList')
        self.syscom.u8('dtchMacSduReceived')
        self.syscom.u8('harqProcessNumber')
        self.syscom.array('4', 'SLcgIds', 'lcgIdList')
        self.syscom.array('8', 'SBearerIds', 'bearerIdList')
        self.syscom.end_struct()

    def SUlUePowerInfo(self, name):
        self.syscom.new_struct('SUlUePowerInfo', name)
        self.syscom.u32('crnti')
        self.syscom.real32('rssi')
        self.syscom.u8('numOfAllocPrbs')
        self.syscom.u8('paddingNumOfAllocPrbs')
        self.syscom.u16('powerLevel')
        self.syscom.end_struct()

    def SUlVoLteParamsDcm(self, name):
        self.syscom.new_struct('SUlVoLteParamsDcm', name)
        self.syscom.array('4', 'SPeriodicGrantInfoDcm', 'periodicGrantIndexRefTable')
        self.syscom.array('3', 'u16', 'yPeriodicGrantInit')
        self.syscom.array('3', 'u16', 'yPeriodicGrant')
        self.syscom.u32('periodicGrantAveDmrsSTimer')
        self.syscom.u32('periodicGrantControlTimer')
        self.syscom.u32('talkSpurtOffTimer')
        self.syscom.u16('periodicGrantSizeMax')
        self.syscom.u16('periodicGranttInitIndex')
        self.syscom.u16('numProhibitPeriodicGrant')
        self.syscom.u16('numProhibitTbReconfig')
        self.syscom.u16('sizeHeaderAssumed')
        self.syscom.u16('reserved1')
        self.syscom.u16('reserved2')
        self.syscom.u16('paddingReserved2')
        self.syscom.end_struct()

    def SUlpcIawConfig(self, name):
        self.syscom.new_struct('SUlpcIawConfig', name)
        self.syscom.u32('ulpcCEBalanceIAw')
        self.syscom.u32('ulpcMinWaitForPc')
        self.syscom.u32('ulpcMinQualIAw')
        self.syscom.i32('ulpcRefPwrIAw')
        self.SOaMUlpcRssiMaxIAw('ulpcRssiMaxIAw')
        self.syscom.end_struct()

    def SUplaneOvlHandlingParameters(self, name):
        self.syscom.new_struct('SUplaneOvlHandlingParameters', name)
        self.syscom.u16('actUplaneOvlHandling')
        self.syscom.u16('upovlCorUl')
        self.syscom.u16('upovlCorDl')
        self.syscom.u16('upovlAveFact')
        self.syscom.u16('upovlThreshold0')
        self.syscom.u16('upovlThreshold1')
        self.syscom.u16('upovlThreshold2')
        self.syscom.u16('upovlUeThreshold')
        self.SMacUpovlha('macUpovlha')
        self.syscom.end_struct()

    def SUplinkPcCommonR10(self, name):
        self.syscom.new_struct('SUplinkPcCommonR10', name)
        self.syscom.u32('deltaFPucchF3r10')
        self.syscom.u32('deltaFPucchF1bCSr10')
        self.syscom.end_struct()

    def SUplinkPowerControlCommonSCell(self, name):
        self.syscom.new_struct('SUplinkPowerControlCommonSCell', name)
        self.syscom.u32('hasPMax')
        self.syscom.i32('pMax')
        self.syscom.i32('p0NominalPusch')
        self.syscom.u32('ulpcAlpha')
        self.syscom.end_struct()

    def SUserInfoMac(self, name):
        self.syscom.new_struct('SUserInfoMac', name)
        self.UDedicRaPreParams('dedicRaPreParams')
        self.syscom.end_struct()

    def SUserResourcesPerCell(self, name):
        self.syscom.new_struct('SUserResourcesPerCell', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('numCrntis')
        self.syscom.array('4', 'SUserResourcesSummary', 'userResourcesSummaryList')
        self.syscom.end_struct()

    def SUserResourcesSummary(self, name):
        self.syscom.new_struct('SUserResourcesSummary', name)
        self.syscom.u32('contextType')
        self.syscom.u32('numContexts')
        self.syscom.u32('numDRbs')
        self.syscom.end_struct()

    def SVoLteThresholdParams(self, name):
        self.syscom.new_struct('SVoLteThresholdParams', name)
        self.syscom.u32('ulTalkSpurtUpperDataTh')
        self.syscom.u32('ulTalkSpurtLowerDataTh')
        self.syscom.end_struct()

    def SWcgi(self, name):
        self.syscom.new_struct('SWcgi', name)
        self.syscom.u32('hot')
        self.syscom.u32('tcId')
        self.SPlmnId('plmnId')
        self.syscom.end_struct()

    def SWmpCellContainer(self, name):
        self.syscom.new_struct('SWmpCellContainer', name)
        self.syscom.u32('enbId')
        self.syscom.u32('numOfCellsPerL1Instance')
        self.syscom.u32('dataCtrlMbmsService')
        self.SCommonCellParamsWmp('commonCellParamsWmp')
        self.SMcsParams('mcsParams')
        self.SPdcchParams('pdcchParams')
        self.SSchedulingWeightParams('schedulingWeightParams')
        self.SLinkAdaptConfParams('linkAdaptConfParams')
        self.SMimoCtrlParams('mimoCtrlParams')
        self.SConvVoiceParams('convVoiceParams')
        self.syscom.u32('enaDrxRepGra')
        self.syscom.u32('enaDrxWactUl')
        self.syscom.u32('enaDrxWactDl')
        self.syscom.u32('enaDrxWcqiDl')
        self.syscom.u32('actDrx')
        self.syscom.u32('drxMaxLongCycle')
        self.syscom.u32('actQci1RfDrx')
        self.syscom.u32('dlRsBoost')
        self.syscom.u32('dlPcfichBoost')
        self.syscom.u32('dlPhichBoost')
        self.syscom.u32('dlsSciCch')
        self.syscom.u32('ulsMinTbs')
        self.syscom.u32('ulsMinRbPerUe')
        self.syscom.u32('actEnhAcAndGbrServices')
        self.SGbrCongestionParams('gbrCongestionParams')
        self.SPRSInfoParams('prsInfoParams')
        self.syscom.u32('actDLCAggr')
        self.syscom.u32('actFastMimoSwitch')
        self.syscom.u32('cellResourceSharingMode')
        self.syscom.u32('crgSkipThreshold')
        self.syscom.array('4', 'u32', 'sharePerResourceGroup')
        self.syscom.u32('sdlEnable')
        self.syscom.u32('actUlCoMp')
        self.syscom.u32('ulCoMpMode')
        self.syscom.u32('actLiquidCell')
        self.syscom.u32('hasLiquidCellConfiguration')
        self.SLiquidCellConfiguration('liquidCellConfiguration')
        self.syscom.u32('actL1PM')
        self.syscom.u32('simUlSpsPf3')
        self.syscom.u32('actSdlc')
        self.syscom.u32('selectOuterPuschRegion')
        self.syscom.u32('ulsMinNumCoverageLimitationStateCheck')
        self.syscom.i32('ulsPhrQci1Low')
        self.syscom.u32('ulsPhrQci1Hyst')
        self.syscom.u32('actVoipCovBoost')
        self.syscom.u32('actMicroDtx')
        self.syscom.u32('mdtxPdcchSymb')
        self.syscom.u32('mdtxAggressiveness')
        self.syscom.u32('multScellReleaseTimer')
        self.syscom.u32('scellNotDetectableThr')
        self.syscom.u32('scellBadChQualThr')
        self.syscom.u32('scellGoodChQualThr')
        self.syscom.u32('longPeriodScellChEst')
        self.syscom.u32('shortPeriodScellChEst')
        self.syscom.u32('notDetectedChEstPer')
        self.syscom.u32('badChEstPer')
        self.syscom.u32('goodChEstPer')
        self.syscom.u32('actAdvScellMeas')
        self.syscom.u32('hasSrsTriggerParams')
        self.SSRSTriggerParams('srsTriggerParams')
        self.syscom.u32('hasBfCtrlParams')
        self.SBeamformingCtrlParams('bfCtrlParams')
        self.syscom.u32('hasTransmModeParams')
        self.STransmModeParams('transmModeParams')
        self.syscom.u32('hasEIcicParams')
        self.SEicicParameters('eIcicParams')
        self.syscom.u32('hasMuMimoParameters')
        self.SMuMimoParameters('muMimoParameters')
        self.syscom.u32('hasCarrierAggrParams')
        self.SCarrierAggrParams('carrierAggrParams')
        self.syscom.u32('hasCsiRsConfiguration')
        self.SCsiRsConfiguration('csiRsConfiguration')
        self.syscom.u32('hasSuperCellParameters')
        self.SSuperCellParameters('superCellParameters')
        self.syscom.u32('hasScellTmSettingWithBf')
        self.syscom.u32('scellTmSettingWithBf')
        self.syscom.u32('hasRipAlarmingParameters')
        self.SOaMRipAlarmingConfig('ripAlarmingParameters')
        self.syscom.u32('hasUplaneOvlHandlingParameters')
        self.SUplaneOvlHandlingParameters('uplaneOvlHandlingParameters')
        self.syscom.u32('actCsBIA')
        self.syscom.u32('hasCsBIAParameters')
        self.SCsBIAParameters('csBIAParameters')
        self.SOaMActLteU('actLteU')
        self.syscom.u32('actPcellSwap')
        self.syscom.u32('hasPCellSwapParams')
        self.SPcellSwapParameters('pCellSwapParams')
        self.syscom.u32('hasQci1DrxOffThreshold')
        self.syscom.u32('qci1DrxOffThreshold')
        self.syscom.u32('hasQci1DrxOnThreshold')
        self.syscom.u32('qci1DrxOnThreshold')
        self.SUciOnlyGrantConfiguration('uciOnlyGrantConfiguration')
        self.SPMQAPProfiles('pmqapProfiles')
        self.syscom.u32('hasNbCellParams')
        self.SNbCellParams('nbCellParams')
        self.syscom.u32('hasFastLoadBalanceConfig')
        self.SFastLoadBalanceConfig('fastLoadBalanceConfig')
        self.syscom.u32('reserved1')
        self.syscom.u32('reserved2')
        self.syscom.end_struct()

    def SWmpCellInfoContainer(self, name):
        self.syscom.new_struct('SWmpCellInfoContainer', name)
        self.SConfigurableUsageAddresses('macPsDelayCriticalAddresses')
        self.SConfigurableUsageAddresses('macPsNonDelayCriticalAddresses')
        self.SMacPsMacPsAddresses('macPsAddresses')
        self.SMacPsL2Addresses('l2Addresses')
        self.syscom.end_struct()

    def SWmpDcmCaParamsContainer(self, name):
        self.syscom.new_struct('SWmpDcmCaParamsContainer', name)
        self.syscom.u32('hasL2CaParamsContainer')
        self.UL2CaParamsContainer('l2CaParamsContainer')
        self.syscom.u32('hasMacPsCaParamsContainer')
        self.UWmpDcmCaParamsContainer('macPsCaParamsContainer')
        self.syscom.end_struct()

    def SWmpRbInfo(self, name):
        self.syscom.new_struct('SWmpRbInfo', name)
        self.syscom.u32('dlSchedulingPriority')
        self.syscom.u32('schedulWeight')
        self.syscom.u32('qci')
        self.syscom.u32('dlsBucketSizeDuration')
        self.syscom.array('2', 'u32', 'dlsGbrRlc')
        self.syscom.array('2', 'u32', 'dlsGbrMac')
        self.syscom.u32('dlsDelayTarget')
        self.syscom.u32('ulsBucketSizeDuration')
        self.syscom.array('2', 'u32', 'ulsGbrRlc')
        self.syscom.array('2', 'u32', 'ulsGbrMac')
        self.syscom.u32('ulsDelayTarget')
        self.syscom.u32('ulsSidVol')
        self.syscom.u32('congestionWeight')
        self.syscom.u32('ulSchedulingPriority')
        self.syscom.u32('hasNbrDl')
        self.syscom.u32('nbrDl')
        self.syscom.u32('hasNbrUl')
        self.syscom.u32('nbrUl')
        self.syscom.u32('reqPRBDL')
        self.syscom.u32('arp')
        self.syscom.u32('hasReserved1')
        self.syscom.u32('reserved1')
        self.syscom.end_struct()

    def SWmpSrbInfo(self, name):
        self.syscom.new_struct('SWmpSrbInfo', name)
        self.syscom.u32('dlSchedulingPriority')
        self.syscom.end_struct()

    def SWmpUlResCtrlParams(self, name):
        self.syscom.new_struct('SWmpUlResCtrlParams', name)
        self.SCqiParamsWmp('cqiParamsWmp')
        self.syscom.u32('numOfCqiParamsScellWmp')
        self.syscom.array('4', 'SCqiParamsScellWmp', 'cqiParamsScellWmp')
        self.syscom.u32('hasTmSwitch')
        self.STmSwitch('tmSwitch')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('numOfSrsParamsScellWmp')
        self.syscom.array('1', 'SSrsParamsScellWmp', 'srsParamsScellWmp')
        self.syscom.u32('measGapStopRequired')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('hasReserved1')
        self.syscom.u32('reserved1')
        self.syscom.u32('hasReserved2')
        self.syscom.u32('reserved2')
        self.syscom.end_struct()

    def SWmpUserContainer(self, name):
        self.syscom.new_struct('SWmpUserContainer', name)
        self.SCqiParamsWmp('cqiParamsWmp')
        self.syscom.u32('harqMaxTrDl')
        self.syscom.u32('harqMaxTrUl')
        self.syscom.u32('tmSupportIndicator')
        self.syscom.u32('ttiBmMeasActivate')
        self.syscom.u32('measGapStopRequired')
        self.syscom.u32('gapPattern')
        self.syscom.u32('measGapOffset')
        self.syscom.u32('hasUeInactivityTimer')
        self.syscom.u32('ueInactivityTimer')
        self.syscom.u32('anrUtraInactivityTimer')
        self.syscom.u32('tInactiveUtraAnrAction')
        self.syscom.u32('dedicRaPreExpT')
        self.syscom.u32('hasOldCrntiInTheSameCell')
        self.syscom.u32('oldCrntiInTheSameCell')
        self.syscom.u32('intentionalContentionbasedRaEnabled')
        self.syscom.u32('cellResourceGroupId')
        self.syscom.u32('hasMaxNumOfLayers')
        self.syscom.u32('maxNumOfLayers')
        self.syscom.u32('maxLayersDeliveredToUe')
        self.syscom.u32('layersRestrictedToTwo')
        self.syscom.u32('hasTargetBLER')
        self.STargetBLER('targetBLER')
        self.syscom.u32('hasThroughputThresholdMonitoring')
        self.SThroughputThresholdMonitoring('throughputThresholdMonitoring')
        self.syscom.u32('hasConfigId')
        self.syscom.u32('configId')
        self.syscom.u32('tddSsp9SupportFlag')
        self.syscom.u32('hasUlSpsConfigDedicated')
        self.SUlSpsConfigDedicated('ulSpsConfigDedicated')
        self.syscom.u32('cookie')
        self.SPlmnId('plmnId')
        self.syscom.u32('hasReserved1')
        self.syscom.u32('reserved1')
        self.syscom.u32('hasReserved2')
        self.syscom.u32('reserved2')
        self.syscom.end_struct()

    def TUP_BearerSetupReq(self, name):
        self.syscom.new_struct('TUP_BearerSetupReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSecurityInformation')
        self.STupSecurityInformation('securityInformation')
        self.syscom.u32('uecategory')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('1', 'STupSrbInfo', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoBearerSetup', 'rbList')
        self.syscom.end_struct()

    def TUP_DataForwardSetupReq(self, name):
        self.syscom.new_struct('TUP_DataForwardSetupReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('destinationUeId')
        self.syscom.u16('destinationUeIndex')
        self.syscom.u16('paddingDestinationUeIndex')
        self.syscom.u32('destinationCellId')
        self.syscom.u32('destinationPoolId')
        self.syscom.u32('transactionId')
        self.syscom.u32('handoverType')
        self.syscom.u32('dcmDlInterRatFoType')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoDataForwardSetup', 'rbList')
        self.syscom.end_struct()

    def TUP_SecurityActivationReq(self, name):
        self.syscom.new_struct('TUP_SecurityActivationReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.end_struct()

    def TUP_SecurityConfReq(self, name):
        self.syscom.new_struct('TUP_SecurityConfReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasSecurityInformation')
        self.STupSecurityInformation('securityInformation')
        self.syscom.end_struct()

    def TUP_SrbSendReq(self, name):
        self.syscom.new_struct('TUP_SrbSendReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('hasDrxConfigId')
        self.syscom.u32('drxConfigId')
        self.syscom.u32('srbId')
        self.syscom.u32('respFlag')
        self.syscom.u32('harqRespFlag')
        self.syscom.u32('mui')
        self.syscom.u32('integrityActivationPreFlag')
        self.syscom.u32('dlCipherActivationPostFlag')
        self.syscom.u32('numOfL3Payload')
        self.syscom.array('1', 'u8', 'l3Payload')
        self.syscom.end_struct()

    def TUP_UserDeleteReq(self, name):
        self.syscom.new_struct('TUP_UserDeleteReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.end_struct()

    def TUP_UserSetupReq(self, name):
        self.syscom.new_struct('TUP_UserSetupReq', name)
        self.syscom.u32('lnCelId')
        self.syscom.u32('crnti')
        self.syscom.u32('ueId')
        self.syscom.u16('ueIndex')
        self.syscom.u16('paddingUeIndex')
        self.syscom.u32('transactionId')
        self.syscom.u32('tupUserAddress')
        self.syscom.u32('tupSgnlSrbAddress')
        self.syscom.u32('macUserAddr')
        self.syscom.u32('handoverType')
        self.syscom.u32('sourceUeId')
        self.syscom.u32('sourceCellId')
        self.syscom.u32('suspendUlTx')
        self.syscom.u32('uecategory')
        self.syscom.u32('numOfSrbList')
        self.syscom.array('2', 'STupSrbInfo', 'srbList')
        self.syscom.u32('numOfRbList')
        self.syscom.array('numOfRbList', 'STupRbInfoUserSetup', 'rbList')
        self.syscom.end_struct()

    def TtiStats(self, name):
        self.syscom.new_struct('TtiStats', name)
        self.syscom.u32('numOfScheduledTtis')
        self.syscom.u32('numOfTtisMimoRequested')
        self.syscom.u32('numOfTtisMimoReqNotFulfilled')
        self.syscom.end_struct()

    def TupBearerSetupReq_UserCreateDeleteLooping(self, name):
        self.syscom.new_struct('TupBearerSetupReq_UserCreateDeleteLooping', name)
        self.STupRbInfoBearerSetup('drbInfo')
        self.syscom.end_struct()

    def TupUserSetupReq_UserCreateDeleteLooping(self, name):
        self.syscom.new_struct('TupUserSetupReq_UserCreateDeleteLooping', name)
        self.STupSrbInfo('srbInfo')
        self.syscom.end_struct()

    def Tup_Uesim_header(self, name):
        self.syscom.new_struct('Tup_Uesim_header', name)
        self.syscom.u32('NumberOfUsers')
        self.syscom.u32('numOfTupSrbSicads')
        self.syscom.array('2', 'u32', 'TupSgnlSicad')
        self.syscom.end_struct()

    def UAdditionalMeasurementParameters(self, name):
        self.syscom.new_struct('UAdditionalMeasurementParameters', name)
        self.syscom.u32('discriminator')
        self.UInnerUAdditionalMeasurementParameters('u')
        self.syscom.end_struct()

    def UAntennaBusParameters(self, name):
        self.syscom.new_union('UAntennaBusParameters', name)
        self.SAntennaBusParametersForRfBus('antennaBusParametersForRfBus')
        self.SAntennaBusParametersForRp3('antennaBusParametersForRp3')
        self.syscom.end_union()

    def UCaUserReconfigurationContainer(self, name):
        self.syscom.new_struct('UCaUserReconfigurationContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUCaUserReconfigurationContainer('u')
        self.syscom.end_struct()

    def UCaWmpDcmSCellContainer(self, name):
        self.syscom.new_struct('UCaWmpDcmSCellContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUCaWmpDcmSCellContainer('u')
        self.syscom.end_struct()

    def UCaWmpDcmUlSCellContainer(self, name):
        self.syscom.new_struct('UCaWmpDcmUlSCellContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUCaWmpDcmUlSCellContainer('u')
        self.syscom.end_struct()

    def UCrntiParams(self, name):
        self.syscom.new_struct('UCrntiParams', name)
        self.syscom.u32('discriminator')
        self.UInnerUCrntiParams('u')
        self.syscom.end_struct()

    def UDedicRaPreParams(self, name):
        self.syscom.new_struct('UDedicRaPreParams', name)
        self.syscom.u32('discriminator')
        self.UInnerUDedicRaPreParams('u')
        self.syscom.end_struct()

    def UInnerSBrowserObjectData(self, name):
        self.syscom.new_union('UInnerSBrowserObjectData', name)
        self.syscom.u32('objectId')
        self.SLnCellId('lnCellId')
        self.SEcgi('ecgi')
        self.SWcgi('wcgi')
        self.SGcgi('gcgi')
        self.SPlmnId('plmnId')
        self.syscom.u32('hbc')
        self.syscom.u16('hua')
        self.syscom.u16('lnAdj')
        self.syscom.u16('lnMme')
        self.syscom.u16('lnM3')
        self.syscom.u16('lnMce')
        self.syscom.u16('earfcn')
        self.SSmodSfp('smodsfp')
        self.SBbmodSfp('bbmodsfp')
        self.SRmodSfp('rmodsfp')
        self.SSharedCellId('sharedCellId')
        self.syscom.u16('apmod')
        self.syscom.u32('mrbtsId')
        self.syscom.u16('pmqap')
        self.syscom.end_union()

    def UInnerUAdditionalMeasurementParameters(self, name):
        self.syscom.new_union('UInnerUAdditionalMeasurementParameters', name)
        self.SMeasurementA7or8('measurementA7or8')
        self.SUlTestModelConfig('ulTestModelConfig')
        self.SMeasurementDcm5toDcm8('measurementDcm5toDcm8')
        self.syscom.end_union()

    def UInnerUCaUserReconfigurationContainer(self, name):
        self.syscom.new_union('UInnerUCaUserReconfigurationContainer', name)
        self.SCaCqiParams('caCqiParams')
        self.syscom.end_union()

    def UInnerUCaWmpDcmSCellContainer(self, name):
        self.syscom.new_union('UInnerUCaWmpDcmSCellContainer', name)
        self.SCaWmpSCellContainer('caWmpSCellContainer')
        self.SCaDcmSCellContainer('caDcmSCellContainer')
        self.syscom.end_union()

    def UInnerUCaWmpDcmUlSCellContainer(self, name):
        self.syscom.new_union('UInnerUCaWmpDcmUlSCellContainer', name)
        self.SCaWmpUlSCellContainer('caWmpUlSCellContainer')
        self.syscom.end_union()

    def UInnerUCrntiParams(self, name):
        self.syscom.new_union('UInnerUCrntiParams', name)
        self.syscom.u32('raCrntiReuseT')
        self.syscom.u32('dcmCrntiTimer')
        self.syscom.end_union()

    def UInnerUDedicRaPreParams(self, name):
        self.syscom.new_union('UInnerUDedicRaPreParams', name)
        self.syscom.u32('dedicRaPreExpT')
        self.SDcmDedicRaParams('dcmDedicRaParams')
        self.syscom.end_union()

    def UInnerUIpAddr(self, name):
        self.syscom.new_union('UInnerUIpAddr', name)
        self.SIpV4('ipv4')
        self.SIpV6('ipv6')
        self.syscom.end_union()

    def UInnerUL2CaParamsContainer(self, name):
        self.syscom.new_union('UInnerUL2CaParamsContainer', name)
        self.SL2CaParamsContainer('l2CaParamsContainer')
        self.syscom.end_union()

    def UInnerUMeasGapOffset(self, name):
        self.syscom.new_union('UInnerUMeasGapOffset', name)
        self.syscom.u32('measGapOffset1')
        self.syscom.u32('measGapOffset2')
        self.syscom.end_union()

    def UInnerUUeInfo(self, name):
        self.syscom.new_union('UInnerUUeInfo', name)
        self.syscom.u32('timingAdvanceType2')
        self.syscom.end_union()

    def UInnerUUlCtrlChannelParams(self, name):
        self.syscom.new_union('UInnerUUlCtrlChannelParams', name)
        self.SUlCtrlChannelPucchAckParams('ulCtrlChannelPucchAckParams')
        self.SUlCtrlChannelPrachParams('ulCtrlChannelPrachParams')
        self.SUlCtrlChannelPucchCqiParams('ulCtrlChannelPucchCqiParams')
        self.SUlCtrlChannelPuschHarqAckParams('ulCtrlChannelPuschHarqAckParams')
        self.syscom.end_union()

    def UInnerUUlResCtrlParamContainer(self, name):
        self.syscom.new_union('UInnerUUlResCtrlParamContainer', name)
        self.SWmpUlResCtrlParams('wmpUlResCtrlParams')
        self.SDcmUlResCtrlParamContainerDcm('dcmUlResCtrlParamContainerDcm')
        self.syscom.end_union()

    def UInnerUUlTfrParamContainer(self, name):
        self.syscom.new_union('UInnerUUlTfrParamContainer', name)
        self.SDcmUlTfrParamContainerDcm('dcmUlTfrParamContainerDcm')
        self.syscom.end_union()

    def UInnerUWmpDcmCaParamsContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmCaParamsContainer', name)
        self.SWmpCellInfoContainer('wmpCellInfoContainer')
        self.SDcmCellPoolContainer('dcmCellPoolContainer')
        self.syscom.end_union()

    def UInnerUWmpDcmCellContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmCellContainer', name)
        self.SWmpCellContainer('wmpCellContainer')
        self.SDcmCellContainerDcm('dcmCellContainerDcm')
        self.SReservedAreaForCellContainer('reservedAreaForCellContainer')
        self.syscom.end_union()

    def UInnerUWmpDcmCellReconfigurationContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmCellReconfigurationContainer', name)
        self.SDcmCellReconfigurationContainerDcm('dcmCellReconfigurationContainerDcm')
        self.syscom.end_union()

    def UInnerUWmpDcmRbContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmRbContainer', name)
        self.SWmpRbInfo('wmpRbInfo')
        self.SDcmRbContainerDcm('dcmRbContainerDcm')
        self.syscom.end_union()

    def UInnerUWmpDcmSrbContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmSrbContainer', name)
        self.SWmpSrbInfo('wmpSrbInfo')
        self.SDcmRbContainerDcm('dcmRbContainerDcm')
        self.syscom.end_union()

    def UInnerUWmpDcmUserContainer(self, name):
        self.syscom.new_union('UInnerUWmpDcmUserContainer', name)
        self.SWmpUserContainer('wmpUserContainer')
        self.SDcmUserContainerDcm('dcmUserContainerDcm')
        self.syscom.end_union()

    def UInnerUlCtrlChannelMeasReportContainer(self, name):
        self.syscom.new_union('UInnerUlCtrlChannelMeasReportContainer', name)
        self.SUlCtrlChannelMeasCountersMissedPrach('ulCtrlChannelMeasCountersMissedPrachWmp')
        self.syscom.end_union()

    def UIpAddr(self, name):
        self.syscom.new_struct('UIpAddr', name)
        self.syscom.u32('discriminator')
        self.UInnerUIpAddr('u')
        self.syscom.end_struct()

    def UL2CaParamsContainer(self, name):
        self.syscom.new_struct('UL2CaParamsContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUL2CaParamsContainer('u')
        self.syscom.end_struct()

    def UMeasGapOffset(self, name):
        self.syscom.new_struct('UMeasGapOffset', name)
        self.syscom.u32('discriminator')
        self.UInnerUMeasGapOffset('u')
        self.syscom.end_struct()

    def UTxRxSyncStatus(self, name):
        self.syscom.new_union('UTxRxSyncStatus', name)
        self.syscom.u32('rxChnlSyncStatus')
        self.syscom.u32('txChnlSyncStatus')
        self.syscom.end_union()

    def UUeInfo(self, name):
        self.syscom.new_struct('UUeInfo', name)
        self.syscom.u32('discriminator')
        self.UInnerUUeInfo('u')
        self.syscom.end_struct()

    def UUlCtrlChannelParams(self, name):
        self.syscom.new_struct('UUlCtrlChannelParams', name)
        self.syscom.u32('discriminator')
        self.UInnerUUlCtrlChannelParams('u')
        self.syscom.end_struct()

    def UUlResCtrlParamContainer(self, name):
        self.syscom.new_struct('UUlResCtrlParamContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUUlResCtrlParamContainer('u')
        self.syscom.end_struct()

    def UUlTfrParamContainer(self, name):
        self.syscom.new_struct('UUlTfrParamContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUUlTfrParamContainer('u')
        self.syscom.end_struct()

    def UWmpDcmCaParamsContainer(self, name):
        self.syscom.new_struct('UWmpDcmCaParamsContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmCaParamsContainer('u')
        self.syscom.end_struct()

    def UWmpDcmCellContainer(self, name):
        self.syscom.new_struct('UWmpDcmCellContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmCellContainer('u')
        self.syscom.end_struct()

    def UWmpDcmCellReconfigurationContainer(self, name):
        self.syscom.new_struct('UWmpDcmCellReconfigurationContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmCellReconfigurationContainer('u')
        self.syscom.end_struct()

    def UWmpDcmRbContainer(self, name):
        self.syscom.new_struct('UWmpDcmRbContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmRbContainer('u')
        self.syscom.end_struct()

    def UWmpDcmSrbContainer(self, name):
        self.syscom.new_struct('UWmpDcmSrbContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmSrbContainer('u')
        self.syscom.end_struct()

    def UWmpDcmUserContainer(self, name):
        self.syscom.new_struct('UWmpDcmUserContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUWmpDcmUserContainer('u')
        self.syscom.end_struct()

    def UlCtrlChannelMeasReportContainer(self, name):
        self.syscom.new_struct('UlCtrlChannelMeasReportContainer', name)
        self.syscom.u32('discriminator')
        self.UInnerUlCtrlChannelMeasReportContainer('u')
        self.syscom.end_struct()

    def LomFm_MinimalFaultInd(self, name):
        self.syscom.new_struct('LomFm_MinimalFaultInd', name)
        self.syscom.u32('id')
        self.syscom.u32('state')
        self.syscom.array('14', 'u32', 'info')
        self.syscom.end_struct()

