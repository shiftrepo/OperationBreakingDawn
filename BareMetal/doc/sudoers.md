sudo�����͂��ׂẴ��[�U�ɕt�^���Ȃ��̂ŁAsudoers�̐ݒ������B  

## wheel
sudo��������O���[�v�̓f�t�H���g��wheel�ɂ���B  
`%wheel  ALL=(ALL)       ALL`  

## ansible���s���[�U����
ansible���s���[�U�͑Θb�`���ł̓��͂������Ȃ����߂�sudo�ł̃p�X���[�h�͕s�v�ɂ���B  
`ansible ALL=(ALL) NOPASSWD:ALL`  

sudo���[�U�ȊO����X�C�b�`�����Ȃ��悤��wheel�O���[�v�ɋ�����R�}���h���w�肷��B  
`%wheel  ALL=(ALL) /usr/bin/su - ansible`  

