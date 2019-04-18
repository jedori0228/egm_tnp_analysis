from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eos2018Data_102X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180920/2018Data_1/'

Data2018_102X = {
    ### MiniAOD TnP for IDs scale 
    'DY_madgraph_100X_part012' : tnpSample('DY_madgraph_100X_part012', 
                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8-AOD-100X_part012.root',
                                       isMC = True, nEvts =  -1 ),

    'DY_powheg_102X_part01' : tnpSample('DY_powheg_102X_part01', 
                                       eos2018Data_102X + 'mc/DYToEE_M-50_NNPDF31_TuneCP5_13TeV-powheg-pythia8-AOD-102X_part01.root',
                                       isMC = True, nEvts =  -1 ),


    'data_Run2018Av123' : tnpSample('data_Run2018Av123' , eos2018Data_102X + 'data/Prompt2018_RunA_v13.root' , lumi = 13.53),  # LIVIA: 22/9: for some reason do not manage to run on RunAv2

    'data_Run2018Bv12' : tnpSample('data_Run2018Bv12' , eos2018Data_102X + 'data/Prompt2018_RunB_v12.root' , lumi = 6.78),

    'data_Run2018Cv12' : tnpSample('data_Run2018Cv12' , eos2018Data_102X + 'data/Prompt2018_RunC_v12.root' , lumi = 6.61),

    'data_Run2018Dv2' : tnpSample('data_Run2018Dv2' , eos2018Data_102X + 'data/Prompt2018_RunD_v2.root' , lumi = 12.78), # LIVIA: 22/9: lumi to be verified


    }



##about lumi: thse ntuples are done with /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt = with recorded luminosity : 31.71 /fb but ~20% are crashed. Also we need to update the single runs lumi

TempSamples = {
    'Temp2017DATA' : tnpSample('Temp2017DATA', '/data9/Users/jskim/EGammaTnP/egm_tnp_analysis/testsamples/2017/TnPTree_data.root'),
    'Temp2017MC1' : tnpSample('Temp2017MC1', '/data9/Users/jskim/EGammaTnP/egm_tnp_analysis/testsamples/2017/TnPTree_mc.root', isMC = True),
    'Temp2017MC2' : tnpSample('Temp2017MC2', '/data9/Users/jskim/EGammaTnP/egm_tnp_analysis/testsamples/2017/TnPTree_mc.root', isMC = True),
    'Temp2017MC3' : tnpSample('Temp2017MC3', '/data9/Users/jskim/EGammaTnP/egm_tnp_analysis/testsamples/2017/TnPTree_mc.root', isMC = True),
}

MySamples = {

    '2016DATA' : tnpSample('2016DATA', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DATA.root'),
    '2016DYLO1' : tnpSample('2016DYLO1', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_madgraphMLM.root', isMC = True),
    '2016DYLO2' : tnpSample('2016DYLO2', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_madgraphMLM.root', isMC = True),
    '2016DYLO3' : tnpSample('2016DYLO3', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_madgraphMLM.root', isMC = True),
    '2016DYNLO1' : tnpSample('2016DYNLO1', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_amcatnloFXFX.root', isMC = True),
    '2016DYNLO2' : tnpSample('2016DYNLO2', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_amcatnloFXFX.root', isMC = True),
    '2016DYNLO3' : tnpSample('2016DYNLO3', '/data9/Users/jskim/EGammaTnP/DATA/2016/2016_DY_amcatnloFXFX.root', isMC = True),

    '2017DATA' : tnpSample('2017DATA', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DATA.root'),
    '2017DYLO1' : tnpSample('2017DYLO1', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_madgraphMLM.root', isMC = True),
    '2017DYLO2' : tnpSample('2017DYLO2', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_madgraphMLM.root', isMC = True),
    '2017DYLO3' : tnpSample('2017DYLO3', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_madgraphMLM.root', isMC = True),
    '2017DYNLO1' : tnpSample('2017DYNLO1', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_amcatnloFXFX.root', isMC = True),
    '2017DYNLO2' : tnpSample('2017DYNLO2', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_amcatnloFXFX.root', isMC = True),
    '2017DYNLO3' : tnpSample('2017DYNLO3', '/data9/Users/jskim/EGammaTnP/DATA/2017/2017_DY_amcatnloFXFX.root', isMC = True),

}



