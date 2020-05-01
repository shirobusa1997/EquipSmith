from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum
import datetime

def generateEquipID():
		now = datetime.datetime.now()
		nowstr = now.strftime('%Y%m%d')
		equipcount = Equipments.objects.filter(registered_date__gte=datetime.date.today()).count()
		return nowstr + str(equipcount).zfill(2)


# Create your models here.
class Equipments(models.Model):
	class EQUIP_ATTRIBUTE(Enum):
		book 			= ('00', '書籍')
		desktopcomputer = ('01', 'デスクトップPC')
		laptopcomputer 	= ('02', 'ノートPC')
		workstation 	= ('03', 'ワークステーション')
		display 		= ('04', 'PCディスプレイ')
		pcsupply 		= ('05', 'PC周辺機器')
		vrdevice 		= ('06', 'VRデバイス')
		ardevice 		= ('07', 'ARデバイス')
		projector 		= ('08', 'プロジェクター')
		screen 			= ('09', 'スクリーン')
		smartphone 		= ('10', 'スマートフォン')
		tabletdevice 	= ('11', 'タブレット端末')
		toolkit 		= ('12', '工具類')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	class EQUIP_STATUS(Enum):
		available 	= ('avlb', '利用可能')
		lending 	= ('lend', '貸出中')
		assigning 	= ('asgn', '割当中')
		maintenance = ('mtnc', 'メンテナンス中')
		lost 		= ('lost', '紛失')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	class EQUIP_STORAGEPLACE(Enum):
		privatespace = ('10fprv', '10階プライベートスペース')
		openlabo 	 = ('09fopn', '9階オープンラボ')
		openspace 	 = ('08fopn', '8階オープンスペース')
		komeroom	 = ('komerm', '米谷先生個室')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	id = models.CharField('備品ID', max_length = 16, primary_key = True, default=generateEquipID)
	name = models.CharField('備品名', blank=False, max_length = 255)
	equip_attribute = models.CharField('種類', null=True, max_length = 4, choices = [x.value for x in EQUIP_ATTRIBUTE])
	equip_status = models.CharField('ステータス', null=True, max_length = 4, choices = [x.value for x in EQUIP_STATUS])
	equip_storagespace = models.CharField('保管場所', null = False, max_length = 6, choices = [x.value for x in EQUIP_STORAGEPLACE], default=1)
	author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, default = 1)
	registered_date = models.DateTimeField('登録年月日', auto_now = True)
	remarks = models.CharField('備考', max_length=255, blank=True)


class Records(models.Model):
	class RECORD_STATUS(Enum):
		green = ('green', '貸出中')
		blue = ('blue', '割当中')
		yellow = ('yellow', '延長貸出中')
		orange = ('orange', '返却期限間近')
		red = ('red', '返却期限切れ・延滞中')
		purple = ('purple', '返却済み・確認中')
		black = ('black', '返却承認済み')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	id = models.AutoField('処理ID', primary_key = True, editable=False)
	equipid = models.ForeignKey(Equipments, on_delete = models.CASCADE)
	userid = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, default = 1)
	status = models.CharField('ステータス', null = True, max_length = 6, choices = [x.value for x in RECORD_STATUS])
	recorded_date = models.DateTimeField('申請日時', auto_now = True)
	return_due = models.DateTimeField('貸出期限', null = True)
	returned_date = models.DateTimeField('返却日時', null = True, blank=True)