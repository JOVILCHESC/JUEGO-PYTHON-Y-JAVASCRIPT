class Character {
    constructor(name, hp, attack, defense) {
      this.name = name;
      this.hp = hp;
      this.attack = attack;
      this.defense = defense;
    }

    doDamage(){
        let lucky =  Math.round(Math.random()*10); // random value from 0..attack
        //let success =  1.5;
        return this.attack + (lucky) //* success; // 0...30...60
    }
    doDefense(){
        let shield =  Math.round(Math.random()*10); 
      
        return this.defense + (shield) 


    }
   
}

class Mage extends Character {
    constructor(name, hp, attack, defense) {
        super(name, hp, attack, defense);
    }
}

class Warrior extends Character {
    constructor(name, hp, attack, defense) {
        super(name, hp, attack, defense);
    }
}

class God extends Character {
    constructor(name, hp, attack, defense) {
        super(name, hp, attack, defense);
    }
}

class Spartan extends Character {
    constructor(name, hp, attack, defense) {
        super(name, hp, attack, defense);
    }
}

class Engine {

    combat(local, rival) {
        this.startFightComment();

        let localTempHP = local.hp;
        let rivalTempHP = rival.hp;
        let count = 0
        while (this.playerIsAlive(localTempHP) && this.playerIsAlive(rivalTempHP)) {
            if(count>30){
                this.eternalFightComment();
                break;
            }
            
            let localDamage = local.doDamage();
            let localDefense = local.doDefense();
            let rivalDefense = rival.doDefense();
            if(localDamage>rivalDefense){
                rivalTempHP -= localDamage-rivalDefense;
            }

            let rivalDamage = rival.doDamage();
            
            if(this.playerIsAlive(rivalTempHP)){
              
                if(rivalDamage>localDefense){
                    localTempHP -= rivalDamage-localDefense;
                } 
            }

            this.showRoundStatus(count, local, localTempHP, localDamage, rival, rivalTempHP, rivalDamage);
            count++;  
            
        }
        
        if(localTempHP>rivalTempHP){
            this.winnerIsComment(local);
        }else{
            this.winnerIsComment(rival);
        }
    }

    playerIsAlive(hp){
        return hp>0;
    }

    showRoundStatus(index, local, localHP, localDamage, rival, rivalHP, rivalDamage){
        document.writeln("<div style='margin-top: 5px; background: gainsboro; border:1px solid black; padding:2px'>");
        document.writeln("Round #"+index);
        this.showStatus(local, localHP, localDamage, localDamage-rival.defense);
        this.showStatus(rival, rivalHP, rivalDamage, rivalDamage-local.defense);
        document.writeln("</div>");
    }

    showStatus(player, currentHP, damage, realDamage){
        document.writeln("<div style='margin-top: 5px; padding-left: 10px'>");
        let formattedCurrentHP = 0;
        if(currentHP>0){
            formattedCurrentHP = currentHP;
        }
        let max_attack = player.attack+10 
        let max_defense = player.defense+10
        document.writeln("<b>"+player.name+" [HP:"+player.hp+" / AT:"+player.attack+" - "+max_attack+" / DF:"+player.defense+" - "+max_defense+"]</b>");
        document.writeln("</br>"); 

        let formattedRealDamage = 0;
        if(realDamage>0){
            formattedRealDamage = realDamage;
        }
        document.writeln("&nbsp;&nbsp;--> "+player.name+" attack with "+Math.round(damage)+" of power!. This do a real damage of "+Math.round(formattedRealDamage)+".");
        document.writeln("<div style='background:yellow; border: 1px solid black; margin-top: 5px; padding: 2px 1px 2px 2px; color: black; width: 200px; height:20px;'>");
        
        let widthDamage = 200*(1-currentHP/player.hp);
        if (widthDamage>=200){
            widthDamage = 199;
        }
        
        document.writeln("<div style='background: red; width: "+(widthDamage)+"px; height: 20px;'>");
        document.writeln(Math.round(formattedCurrentHP));
        document.writeln("</div>");    
        document.writeln("</div>");
        document.writeln("</div>");
    }

    startFightComment(){
        document.writeln("<div style='background: green; margin-top: 5px; color: white; padding: 5px 8px 2px 8px; height=20px;'>");
        document.writeln("Fight!!!");
        document.writeln("</div>");
    }

    winnerIsComment(player){
        document.writeln("<div style='background: green; margin-top: 10px; color: white; padding: 5px 8px 2px 8px; height=20px;'>");
        document.writeln("The winner is:"+player.name);
        document.writeln("</div>");
    }

    eternalFightComment(){
        document.writeln("<div style='background: yellow; margin-top: 10px; color: black; padding: 5px 8px 2px 8px; height=20px;'>");
        document.writeln("This is an eternal fight!!!");
        document.writeln("</div>");
    }
}

let characters = [
    new Mage("Mage",200 + Math.round(Math.random()*15), Math.round(Math.random()*40), Math.round(Math.random()*20)),
    new Warrior("Warrior",200 + Math.round(Math.random()*15), Math.round(Math.random()*40), Math.round(Math.random()*20)),
    new God("God",200 + Math.round(Math.random()*15), Math.round(Math.random()*40), Math.round(Math.random()*20)),
    new Spartan("Spartan",200 + Math.round(Math.random()*15), Math.round(Math.random()*40), Math.round(Math.random()*20)),
];