function solution(files) {
    files = files.map(x => {
        x = x.replace(/([0-9])/, ".$1");
        x = x.split('.');
        return x;
    })

    files.sort((a, b) => {
        var aHead = a[0].toLowerCase();
        var bHead = b[0].toLowerCase();
        if (a === b) {
            return 0;
        }
        if (aHead === bHead) {
            var aNum = parseInt(a[1]);
            var bNum = parseInt(b[1]);
            if (aNum === bNum) return 0;
            return aNum - bNum;
        }
        return aHead < bHead ? -1 : aHead > bHead ? 1 : 0;
    })

    files = files.map(x => {
        x = x.join(".");
        x = x.replace(/([.])/, "");
        return x;
    })

    return files;

}

var files = ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"];
console.log(solution(files));
