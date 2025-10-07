class Localization2D{
    /**
     * 
     * @param {string[][]} world 
     */
    constructor(world){
        this.world = world;
        this.believe = [[]];

        this.resetBelieve(); 
    }


    resetBelieve(){
        this.believe = this.createBelieve();
        this.render();
    }

    createBelieve(){
        const rows = this.world.length;
        const cols = this.world[0].length;
        const uniform = 1 / (rows * cols);
        return Array.from({ length: rows }, () => Array(cols).fill(uniform));
    }
    
    /**
     * 
     * @param {number[][]} bel 
     */
    normalize(bel){
        const sum = bel.flat().reduce((prev,curr) => prev + curr);
        return bel.map((r) => {
            return r.map((b) => {
                return b / sum;
            })
        });
    }

    /**
     * 
     * @param {string} measurement 
     * @param {number} pHit 
     * @param {number} pMiss 
     */
    sense(measurement, pHit = .7 , pMiss = .2){
        const newBel = this.believe.map((r,i) => {
            return r.map((b,j) => {
                return b * (measurement.toLowerCase() == this.world[i][j].toLowerCase() ? pHit : pMiss);
            })
        });

        this.believe = this.normalize(newBel);
        
        this.render();
        this.printBelieve();
    }

    /**
     * 
     * @param {number} stepX 
     * @param {number} stepY 
     * @param {number} pExact 
     * @param {number} pOvershoot 
     * @param {number} pUndershoot 
     */
    move(stepX, stepY, pExact = .8, pOvershoot = .1, pUndershoot = 0.1){
        const n = this.world.length;
        const m = this.world[0].length;
        
        let newBel = this.createBelieve();
        const mod = (v,limit) => ((v % limit) + limit) % limit;

        for(let i=0;i<n;i++){
            for(let j=0;j<m;j++){
                const bel = this.believe[i][j];
                // exact
                newBel[mod(i + stepY, n)][mod(j + stepX, m)] += pExact * bel;        

                // overshoot
                newBel[mod(i + stepY + 1, n)][mod(j + stepX + 1, m)] += pOvershoot * bel;

                // undershoot
                newBel[mod(i + stepY -1, n)][mod(j + stepX - 1, m)] += pUndershoot * bel;
            }
        }

        this.believe = this.normalize(newBel);
        this.render();
        this.printBelieve();
    }

    render() {
      const container = document.getElementById('world');
      container.innerHTML = '';

      const rows = this.world.length;
      const cols = this.world[0].length;

      // Make grid layout adapt to world size
      container.style.gridTemplateColumns = `repeat(${cols}, 100px)`;

      const maxBel = Math.max(...this.believe.flat());
      this.believe.forEach((row, i) => {
        row.forEach((b, j) => {
          const cell = document.createElement('div');
          cell.className = 'cell ' + this.world[i][j].toLowerCase();

          const bar = document.createElement('div');
          bar.className = 'bel-bar';
          bar.style.height = `${(b / maxBel) * 100}%`;

          const label = document.createElement('div');
          label.className = 'label';
          label.textContent = `(${i},${j}) ${this.world[i][j]}`;

          cell.appendChild(bar);
          cell.appendChild(label);
          container.appendChild(cell);
        });
      });
    }


    printBelieve() {
        console.log("Current belief:");
        this.believe.forEach((row, i) => {
            const rowStr = row.map(b => b.toFixed(4)).join("  ");
            console.log(`Row ${i}: [ ${rowStr} ]`);
        });
        const sum = this.believe.flat().reduce((a, b) => a + b, 0);
        console.log("Sum:", sum.toFixed(4));
    }
}

const world = [
  ['High', 'Low',  'High', 'Low'],
  ['Low',  'Low',  'High', 'High'],
  ['Low',  'High', 'Low',  'Low'],
  ['High', 'Low',  'Low',  'High']
];

window.localizer = new Localization2D(world);