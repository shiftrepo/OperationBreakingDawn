�f�t�H���g����ύX����ӏ��̂݋L��  

# sshd_config
* PermitRootLogin  
`no`  
�f�t�H���g��YES�����A��ʃ��[�U���̂ŕ��ʂɍl����no�ɂ��Ă���  
* PubkeyAuthentication  
`yes`  
* Match  
ansible���s���[�U�ւ�SSH���O�C�����Ƀp�X���[�h�F�؂ł͂Ȃ��A  
���ŔF�؂���������SSH�Œ����O�C���ł��Ȃ��悤�Ƀ��[�U�w��Őݒ�l��ς���  
```
Match User ansible  
 PasswordAuthentication no  
 AuthorizedKeysFile .ssh/authorized_keys  
```

# ���F��
�O������̃A�N�Z�X���Ȃ����߁A��ʃ��[�U�̃��O�C���̓p�X���[�h�F�؂Ƃ���B  
�������AAnsible���s���[�U�Ɋւ��Ă̓p�X���[�h�Ȃ��̌��F�ؕ����Ƃ��邱�ƂŁAAnsible���s�Ώۂ̃z�X�g�ւ�SSH���O�C�����ɑΘb�`���ł̓��͂��K�v�Ȃ��悤�ɂ���B  
���͈ȉ��̒ʂ�쐬����B  

| �p�[�~�b�V���� | ��΃p�X                           | ���e                   |
|----------------|------------------------------------|------------------------|
| 700            | /home/ansible/.ssh/id_rsa.pub      | ���J��                 |
| 600            | /home/ansible/.ssh/id_rsa          | �閧��                 |
| 600            | /home/ansible/.ssh/authorized_keys | �F�ؗp�Ɏg�p������J�� |

# Cipher  
���̈Í��A���S���Y����`ecdsa256`�ɂ���B  
RSA2048�͂��͂�Â��炵���BRSA��菭�Ȃ��r�b�g���ŋ��łő����B  
