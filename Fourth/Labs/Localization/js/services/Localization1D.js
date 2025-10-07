export class Localization1D{
    /**
     * 
     * @param {string[]} world 
     */
    constructor(world){
        this.world = world;
        this.believe = [];

        this.resetBelieve(); 
    }

    resetBelieve(){
        this.believe = Array(this.world.length).fill(1 / this.world.length);
        return this.render();
    }
    
    /**
     * 
     * @param {string} measurement
     */
    sense(measurement, pHit = .7 , pMiss = .2){
        const newBel = this.believe.map((b,i) => {
           return b * (measurement.toLowerCase() == this.world[i].toLowerCase() ? pHit : pMiss);
        });

        const sum = newBel.reduce((prev, curr) => prev + curr);
        
        this.believe = newBel.map(b => b / sum);
        
        this.render();
        this.printBelieve();
    }


    /**
     * @param {number} step
     */
    move(step, pExact = .8, pOvershoot = .1, pUndershoot = 0.1){
        const n = this.world.length;
        let newBel = Array(n).fill(0);

        this.believe.forEach((b, i) => {
            newBel[this.#mod(i + step,n)] += b * pExact;
            newBel[this.#mod(i + step + 1,n)] += b * pOvershoot;
            newBel[this.#mod(i + step - 1,n)] += b * pUndershoot;
        });
        
        this.believe = newBel;
        
        this.render();
        this.printBelieve();
    }

    render(){
        const container = document.getElementById('world');
        container.innerHTML = '';

        const maxBel = Math.max(...this.believe);
        this.believe.forEach((b, i) => {
          const cell = document.createElement('div');
          cell.className = 'cell ' + this.world[i].toLowerCase();

          const bar = document.createElement('div');
          bar.className = 'bel-bar';
          bar.style.height = `${(b / maxBel) * 100}%`;

          const label = document.createElement('div');
          label.style.position = 'absolute';
          label.style.top = '5px';
          label.style.fontSize = '12px';
          label.textContent = `#${i}\n${this.world[i]}`;

          cell.appendChild(bar);
          cell.appendChild(label);
          container.appendChild(cell);
        });
    }

    printBelieve(){
        console.log("Current belief:");
        this.believe.forEach((b, i) => {
            console.log(`Cell ${i} (${this.world[i]}): ${b.toFixed(4)}`);
        });
        console.log("Sum:", this.believe.reduce((a, b) => a + b, 0).toFixed(4));
    }


    /**
     * 
     * @param {number} x 
     * @param {number} m 
     */
    #mod(x, m){
        const modelusResult = x % m;
        if(modelusResult < 0)
            return m + modelusResult;
        return modelusResult;
    }

}