function solution(m, musicinfos) {
    m = convertMusic(m);
    var answer = '';

    var correctMusic = [];

    musicinfos = musicinfos.map(x => {
        x = x.split(',');
        var playStart = x[0].split(':');
        var playEnd = x[1].split(':');
        var playTime = musicPlayTime(playStart, playEnd);
        var subtitle = x[2];
        var sound = x[3];
        sound = convertMusic(sound);
        var playSound = [];
        for (let i = 0; i < playTime; i++) {
            playSound.push(sound[i % sound.length]);
        }
        playSound = playSound.join('');
        if (playSound.includes(m)) {
            correctMusic.push([subtitle, playTime]);
        }
    })

    var maxtime = 0;
    correctMusic.map(x => {
        if (maxtime < x[1]) {
            maxtime = x[1];
            answer = x[0];
        }
    })
    if (answer === '') {
        return '(None)';
    }
    return answer;
}
function musicPlayTime(playStart, playEnd) {
    const start = new Date(2021, 5, 7, parseInt(playStart[0]), parseInt(playStart[1]), 0);
    const end = new Date(2021, 5, 7, parseInt(playEnd[0]), parseInt(playEnd[1]), 0);

    return ((end.getTime() - start.getTime()) / 1000 / 60);
}
function convertMusic(sound) {
    sound = sound.replace(/(C#)/g, 'H');
    sound = sound.replace(/(D#)/g, 'I');
    sound = sound.replace(/(F#)/g, 'J');
    sound = sound.replace(/(G#)/g, 'K');
    sound = sound.replace(/(A#)/g, 'L');
    return sound;
}
var m = "CC#BCC#BCC#BCC#B"
var musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"];

console.log(solution(m, musicinfos));