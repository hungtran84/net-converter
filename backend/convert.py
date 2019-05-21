# These functions need to be implemented
class CidrMaskConvert:

    def cidr_to_mask(self, cidr):
        mask = 'Invalid'
        if (32 >= int(cidr) >=1):
            mask = ''
            x = '1'*int(cidr) + '0'*(32-int(cidr))
            _mask = [x[i:i+8] for i in range(0,len(x),8)]
            for j in _mask:
                mask += str(int(j,2)) + '.'
            mask = mask[:-1]           
        return mask
        
       
    def mask_to_cidr(self, mask):
        valid_mask = (0, 128, 192, 224, 240, 248, 252, 254, 255)
        octets = mask.split('.')
        cidr = 'Invalid'
        if len(octets) == 4 and all(int(i) in valid_mask for i in octets):
            _cidr = ''
            for i in octets:
                j = '{0:08b}'.format(int(i))
                _cidr += j
            if '01' not in _cidr and _cidr.count('1') != 0:
                cidr = _cidr.count('1')
                if cidr == 0:
                    cidr = 'Invalid'
        return str(cidr)

class IpValidate:

    def ipv4_validation(self, ip):
        valid = False
        parts = ip.split('.')
        if all(part.isdigit() for part in parts):
            valid = (len(parts) == 4 and all(0 <= int(part) < 256 for part in parts))
        return valid
