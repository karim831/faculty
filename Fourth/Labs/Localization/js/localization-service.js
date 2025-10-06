class Localization{
    constructor(){
        this.world = ['High','Low','Low','High','Low','High','Low','Low'];
        
        /**
         * @property {number[]} bel
         */
        this.bel = [];

        this.resetBelieve(); 
    }

    resetBelieve(){
        this.bel = Array(this.world.length).fill(1 / this.world.length);
        this.render();
    }

    /**
     * 
     * @param {string} measurement
     */
    sense(measurement, pHit = .7 , pMiss = .2){
        const newBel = this.bel.map((b,i) => {
           return b * (measurement.toLowerCase() == this.world[i].toLowerCase() ? pHit : pMiss);
        });

        const sum = newBel.reduce((prev, curr) => prev + curr);
        
        this.bel = newBel.map(b => b / sum);

        this.render();
        this.printbel();
    }

    /**
     * @param {number} step
     */
    move(step, pExact = .8, pOvershoot = .1, pUndershoot = 0.1){
        const n = this.world.length;
        let newBel = Array(n).fill(0);

        this.bel.forEach((b, i) => {
            newBel[this.#mod(i + step,n)] += b * pExact;
            newBel[this.#mod(i + step + 1,n)] += b * pOvershoot;
            newBel[this.#mod(i + step - 1,n)] += b * pUndershoot;
        });
        
        this.bel = newBel;
        
        this.render();
        this.printbel();
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

    render(){
        const container = document.getElementById('world');
        container.innerHTML = '';

        const maxBel = Math.max(...this.bel);
        this.bel.forEach((b, i) => {
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

    printbel() {
        console.log("Current belief:");
        this.bel.forEach((b, i) => {
            console.log(`Cell ${i} (${this.world[i]}): ${b.toFixed(4)}`);
        });
        console.log("Sum:", this.bel.reduce((a, b) => a + b, 0).toFixed(4));
    }


}

let localizer = new Localization();